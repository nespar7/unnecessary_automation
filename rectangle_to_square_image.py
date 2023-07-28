from PIL import Image, ImageFilter
import sys


def make_square_image(input_path, output_path):
    # Open input image
    input_img = Image.open(input_path)

    # Get size of the bounding square
    square_size = max(input_img.width, input_img.height)

    # Create a canvas of size of the bounding square
    canvas = Image.new("RGB", (square_size, square_size))

    # For placing the actual image in middle of the canvas, we calculate the offset in x and y directions 
    x_offset = (square_size - input_img.width) // 2
    y_offset = (square_size - input_img.height) // 2
  
    # take the blurred image, resize it to the square size and make it the background
    blurred_img = input_img.filter(ImageFilter.GaussianBlur(5))
    blurred_img = blurred_img.resize((square_size, square_size))
    canvas.paste(blurred_img, (0, 0), mask=blurred_img)
  
    # Take the input image and paste it in the center
    canvas.paste(input_img, (x_offset, y_offset))

    canvas.save(output_path)


if __name__ == "__main__":
    # if length of args is not 3, then exit
    if len(sys.argv) != 3:
        print("Usage: python squarer.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    make_square_image(input_path, output_path)
