from PIL import Image
import numpy as np
import argparse

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)
    encrypted_pixels = (pixels + key) % 256  # Simple encryption logic
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to input image')
    parser.add_argument('--output', required=True, help='Path to save encrypted image')
    parser.add_argument('--key', type=int, required=True, help='Encryption key')
    args = parser.parse_args()
    encrypt_image(args.input, args.output, args.key)

if __name__ == '__main__':
    main()
