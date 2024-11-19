import os
from PIL import Image

folder = os.path.dirname(os.getcwd()) + "\\assets\\need conversion"


def from_webp_to_png(img_path=None, name=''):
    print(img_path)
    if img_path and name:
        # Open a WEBP image
        image = Image.open(f"{img_path}")

        # Convert to JPG
        # image.convert("RGB").save("output.jpg", "JPEG")

        # Convert to PNG
        image.save(f"{os.path.dirname(folder)}\\" + name + '.png', "PNG")


def run_conversion_folder():

    for file in os.listdir(folder):
        if file.endswith(".webp"):
            full_path = os.path.join(folder, file)
            from_webp_to_png(img_path=full_path, name=file[0:-5])


run_conversion_folder()
