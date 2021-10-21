import PIL.Image

ASCII_CHARS = ['@', '#', '$', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resize_image = image.size(new_width, new_height)
    return resize_image

def gratify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(ASCII_CHARS[pixels//25] for pixel in pixels)
    return (characters)

def main():
    path = input("Masukkan lokasi gambar yang benar: ")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Lokasi gambar tidak ditemukan")

    new_image_data = pixels_to_ascii(gratify(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()


