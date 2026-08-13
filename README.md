
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

## Example

An image is first encoded into a sequence such as:

`ACGTGCAATCG...`

The stored DNA sequence can then be read independently and decoded to
reconstruct the original image.

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

## Future Work

Future improvements may include:

- DNA sequence validation
- Error correction
- Sequence chunking
- GC-content optimization
- Exploring DNA origami as a potential structural platform for organizing
  DNA-encoded information

## Author

Btoul Alkhalil
