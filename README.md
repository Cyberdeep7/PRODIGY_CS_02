# PRODIGY_CS_02

# Pixel Manipulation for Image Encryption

## Overview
This project is a simple image encryption tool that uses pixel manipulation techniques to securely transform images. The tool allows users to **encrypt and decrypt** images using basic operations like swapping pixel values or applying mathematical transformations to each pixel. 

## Features
- Encrypt images by manipulating pixel values.
- Decrypt encrypted images back to their original form.
- Support for common image formats (PNG, JPEG, BMP, etc.).
- User-friendly command-line interface.

## How It Works
1. **Encryption**: The tool modifies pixel values using a predefined algorithm, making the image unreadable without decryption.
2. **Decryption**: The tool reverses the encryption process to reconstruct the original image.

## Installation
Ensure you have Python installed, then clone this repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/your-username/pixel-image-encryption.git
cd pixel-image-encryption

# Install dependencies
pip install -r requirements.txt
```

## Usage
### Encrypt an Image
```bash
python encrypt.py --input input_image.png --output encrypted_image.png --key your_secret_key
```

### Decrypt an Image
```bash
python decrypt.py --input encrypted_image.png --output decrypted_image.png --key your_secret_key
```

## Example
Original Image → Encrypted Image → Decrypted Image


## Technologies Used
- Python
- OpenCV / PIL (Pillow) for image processing
- NumPy for efficient numerical operations

## Future Enhancements
- Implement stronger encryption techniques
- Add a GUI for ease of use
- Support for batch image encryption
