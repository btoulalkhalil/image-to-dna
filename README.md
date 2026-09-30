
# Image-to-DNA Encoder

A Python project exploring the basic concept of DNA-based data storage by
converting image data into sequences composed of the four DNA nucleotides:
A, C, G, and T.

## How It Works

The program reads the binary data of an image and converts every pair of
bits into a DNA nucleotide using the following mapping:

| Binary | DNA Base |
|--------|----------|
| 00 | A |
| 01 | C |
| 10 | G |
| 11 | T |

Therefore, the overall process is:

Image → Bytes → Binary → DNA Sequence

The decoding process reverses these steps:

DNA Sequence → Binary → Bytes → Reconstructed Image

## Features

- Encode an image into a DNA sequence
- Save the DNA sequence as a text file
- Decode the DNA sequence
- Reconstruct the original image

## Web Platform

The project includes a web interface built with [Streamlit](https://streamlit.io)
(`app.py`) where users can:

- Upload an image (PNG, JPG, GIF, BMP or WebP, up to 5 MB) and get its DNA sequence
- See the image size, DNA length, GC content and base counts
- Download the DNA sequence as a `.txt` file
- Upload or paste a DNA sequence and reconstruct the original image

### Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

### Put it online (free)

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
2. Click **Create app**, choose this repository, the `main` branch and `app.py`.
3. Click **Deploy**. You will get a public link you can share with users.

### Run the script only

```bash
python dna_image.py
```

(Edit the image file name in `main()` first.)

## Example

Here is a simple example demonstrating the complete encoding and decoding process.

### Original Image

![Original image](examples/Happy%20Face.png)

### DNA-Encoded Data

The image is converted into binary data and mapped to DNA nucleotides (A, C, G, and T).

A complete example of the generated DNA sequence is available in:
[`encoded_dna.txt`](examples/encoded_dna.txt)

### Reconstructed Image

The DNA sequence can then be decoded back into the original image data.

![Reconstructed image](examples/reconstructed.jpg)

## Limitations

This project is a computational demonstration of DNA data encoding.
The generated sequences are not currently optimized for physical DNA
synthesis or storage.

Real DNA data-storage systems may require additional considerations such as:

- GC content
- Homopolymer avoidance
- Error correction
- Sequence length
- DNA synthesis and sequencing errors

## Upcoming Features

Future improvements will include:
- DNA sequence validation
- Error correction
- Sequence chunking
- GC-content optimization
- Exploring DNA origami as a potential structural platform for organizing
  DNA-encoded information

## Author

Btoul Alkhalil
