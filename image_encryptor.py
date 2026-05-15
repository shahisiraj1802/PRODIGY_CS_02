from PIL import Image

def encrypt_decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    width, height = image.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            r = r ^ key
            g = g ^ key
            b = b ^ key

            pixels[i, j] = (r, g, b)

    image.save(output_path)
    print(f"Image saved as {output_path}")

print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter your choice: ")

key = int(input("Enter encryption key (0-255): "))

if choice == "1":
    encrypt_decrypt_image("sample.jpg", "encrypted.jpg", key)

elif choice == "2":
    encrypt_decrypt_image("encrypted.jpg", "decrypted.jpg", key)

else:
    print("Invalid choice")