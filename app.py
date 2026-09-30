# Streamlit web interface for the DNA Image Encoder and Decoder
# Run it with:  streamlit run app.py

import io
from collections import Counter

import streamlit as st
from PIL import Image, UnidentifiedImageError

from dna_image import bytes_to_dna, dna_to_bytes


MAX_UPLOAD_MB = 5
PREVIEW_CHARS = 2000


st.set_page_config(page_title="Image to DNA", page_icon="🧬", layout="centered")

st.title("🧬 Image to DNA")
st.write(
    "Upload an image and turn it into a DNA sequence made of the four "
    "nucleotides **A**, **C**, **G** and **T**, or paste a DNA sequence to "
    "get the image back."
)

with st.expander("How does it work?"):
    st.markdown(
        "Every byte of the image file is split into four pairs of bits, "
        "and each pair becomes one DNA base:\n\n"
        "| Binary | Base |\n|---|---|\n"
        "| 00 | A |\n| 01 | C |\n| 10 | G |\n| 11 | T |\n\n"
        "**Image → Bytes → Binary → DNA sequence**, and decoding reverses it."
    )


def show_image(data, caption):

    # Show the image if the bytes are a valid image file
    try:
        Image.open(io.BytesIO(data)).verify()
    except (UnidentifiedImageError, OSError):
        st.warning("These bytes don't look like a valid image file.")
        return False

    st.image(data, caption=caption, width=350)
    return True


def detect_extension(data):

    # Guess the file type from the decoded bytes
    try:
        image_format = Image.open(io.BytesIO(data)).format
    except (UnidentifiedImageError, OSError):
        return "bin"

    return {"JPEG": "jpg"}.get(image_format, (image_format or "bin").lower())


encode_tab, decode_tab = st.tabs(["Image → DNA", "DNA → Image"])


# ENCODE TAB

with encode_tab:

    uploaded = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg", "gif", "bmp", "webp"],
        help="Maximum size: " + str(MAX_UPLOAD_MB) + " MB",
    )

    if uploaded is not None:

        data = uploaded.getvalue()

        if len(data) > MAX_UPLOAD_MB * 1024 * 1024:
            st.error("The image is larger than " + str(MAX_UPLOAD_MB) + " MB.")

        elif show_image(data, uploaded.name):

            with st.spinner("Encoding into DNA..."):
                dna = bytes_to_dna(data)

            st.success("Image encoded successfully!")

            counts = Counter(dna)
            gc_content = (counts["G"] + counts["C"]) / len(dna) * 100

            col1, col2, col3 = st.columns(3)
            col1.metric("Image size", f"{len(data):,} bytes")
            col2.metric("DNA length", f"{len(dna):,} bases")
            col3.metric("GC content", f"{gc_content:.1f}%")

            st.caption("Number of each base")
            st.bar_chart({base: counts[base] for base in "ACGT"}, height=220)

            st.subheader("DNA sequence")
            if len(dna) > PREVIEW_CHARS:
                st.caption(
                    f"Showing the first {PREVIEW_CHARS:,} of {len(dna):,} bases. "
                    "Download the file for the full sequence."
                )
            st.code(dna[:PREVIEW_CHARS], language=None, wrap_lines=True)

            base_name = uploaded.name.rsplit(".", 1)[0]
            st.download_button(
                "⬇️ Download DNA sequence (.txt)",
                data=dna,
                file_name=base_name + "_dna.txt",
                mime="text/plain",
            )


# DECODE TAB

with decode_tab:

    dna_file = st.file_uploader("Upload a DNA sequence file", type=["txt"])
    dna_text = st.text_area("...or paste a DNA sequence", height=150)

    dna_input = dna_file.getvalue().decode("utf-8", errors="replace") if dna_file else dna_text

    if st.button("Decode to image", type="primary", disabled=not dna_input.strip()):

        try:
            with st.spinner("Decoding DNA..."):
                image_bytes = dna_to_bytes(dna_input)
        except ValueError as error:
            st.error(str(error))
        else:
            if show_image(image_bytes, "Reconstructed image"):
                st.success("Image decoded successfully!")

            st.download_button(
                "⬇️ Download reconstructed image",
                data=image_bytes,
                file_name="reconstructed." + detect_extension(image_bytes),
            )
