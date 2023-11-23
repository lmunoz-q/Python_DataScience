from PIL import Image


def ft_load(path: str) -> list:
    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("File must be .jpg or .jpeg")


    try:
        image = Image.open(path)
    except IOError:
        raise IOError("Impossible to open file, make sure it's a .jpg or .jpeg valid")


    pixel = image.load()
    ret = [[]]
    rgb_im = image.convert('RGB')
    print(f"The shape of image is: ({image.size[1]}, {image.size[0]}, {len(image.mode)})")

    for y in range((image.size[1])):
        for x in range((image.size[0])):
            for color in rgb_im.getpixel((x, y)), 3:
                if color != 3:
                    ret[0].append(color)

    ret_str = str(ret).replace("(", "[").replace(")", "]").replace(",", "").replace("] ", "]\n")
    return (ret_str)
