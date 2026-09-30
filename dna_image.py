
# DNA Image Encoder and Decoder


# 1. We define the conversion tables

BITS_TO_BASE = {
    "00": "A",
    "01": "C",
    "10": "G",
    "11": "T"
}

BASE_TO_BITS = {
    "A": "00",
    "C": "01",
    "G": "10",
    "T": "11"
}



# 2. ENCODE FUNCTION
# from image to DNA sequence


def image_to_dna(image_path):

    # Open the image as binary data
    with open(image_path, "rb") as file:
        data = file.read()

    dna_sequence = ""

    # Go through every byte in the image
    for byte in data:

        # Convert the byte into 8 bits
        bits = format(byte, "08b")

        # Take 2 bits at a time
        for i in range(0, 8, 2):

            pair = bits[i:i+2]

            # Convert the pair into A, C, G, or T
            dna_sequence += BITS_TO_BASE[pair]

    return dna_sequence



# 3. DECODE FUNCTION
# from DNA sequence to image

def dna_to_image(dna_sequence, output_path):

    image_bytes = bytearray()

    # Take 4 DNA bases at a time
    for i in range(0, len(dna_sequence), 4):

        dna_chunk = dna_sequence[i:i+4]

        bits = ""

        # Convert each DNA base back into 2 bits
        for base in dna_chunk:
            bits += BASE_TO_BITS[base]

        # Convert the 8 bits back into a number
        byte = int(bits, 2)

        image_bytes.append(byte)

    # Save the reconstructed image
    with open(output_path, "wb") as file:
        file.write(image_bytes)


# 4. MAIN FUNCTION


def main():

    # Encode the original image
    dna = image_to_dna("image.png")   # please enter here the name of your image file, both png and jpg fromats are accepted

    print("Image encoded successfully!")
    print("DNA length:", len(dna))

    # Save the DNA sequence
    with open("encoded_dna.txt", "w") as file:
        file.write(dna)

    # Decode the DNA back into an image
    # Read ONLY the DNA sequence
    with open("encoded_dna.txt", "r") as file:
        dna = file.read()
    dna_to_image(dna, "reconstructed.jpg")

    print("Image decoded successfully!")



# 5. START THE PROGRAM


if __name__ == "__main__":
    main()
