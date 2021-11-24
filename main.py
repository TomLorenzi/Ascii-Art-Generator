import PIL.Image
import sys

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def main():
    path = sys.argv[1]
    size = int(sys.argv[2])
    try:
        image = PIL.Image.open(path)
    except:
        print(path, 'Unable to find file')

    image = resize(image, size)
    greyscale_image = to_greyscale(image)
    ascii_str = pixel_to_ascii(greyscale_image)

    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    with open("/var/www/thomasdl/ascii/result.txt", "w") as file:
        file.write(ascii_img)

def resize(image, new_width):
    width, height = image.size
    new_height = new_width * height / width
    return image.resize((int(new_width), int(new_height)))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str

main()