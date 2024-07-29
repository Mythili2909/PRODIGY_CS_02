from PIL import Image
import numpy as np
import os

def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No such file or directory: '{image_path}'")
    image = Image.open(image_path)
    return image

def save_image(image, path):
    image.save(path)

def encrypt_image(image, key):
    np_image = np.array(image)
    encrypted_image = np_image ^ key  # XOR operation with the key
    return Image.fromarray(encrypted_image)

def decrypt_image(encrypted_image, key):
    np_image = np.array(encrypted_image)
    decrypted_image = np_image ^ key  # XOR operation with the key
    return Image.fromarray(decrypted_image)

# Paths for the input and output images
input_image_path = r'c:\Users\91739\Downloads\avanta QR code.png'  # Raw string to avoid unicode error
encrypted_image_path = r'C:\Users\91739\Desktop\prodigy intern 2\encrypted_image.png'
decrypted_image_path = r'C:\Users\91739\Desktop\prodigy intern 2\decrypted_image.png'

# Load the image
try:
    image = load_image(input_image_path)

    # Encryption key (it should be the same for encryption and decryption)
    key = 123  # Example key

    # Encrypt the image
    encrypted_image = encrypt_image(image, key)
    save_image(encrypted_image, encrypted_image_path)

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)
    save_image(decrypted_image, decrypted_image_path)

    print("Image encryption and decryption completed successfully.")

except FileNotFoundError as e:
    print(e)
