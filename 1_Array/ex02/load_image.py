from PIL import Image


def ft_load(path: str) -> list:
    image = Image.open(path)
    pixel = image.load
    ret = []
    rgb_im = image.convert('RGB')
    print(f"The shape of image is: ({image.size[1]}, {image.size[0]}, {len(image.mode)})")
    for y in range((image.size[1]) // 99):
        for x in range((image.size[0]) // 99):
            for i in image.getpixel((x,y)):
                
    return(ret)


def main():
    path = "landscape.jpg"
    ft_load(path)

if __name__ == "__main__":
    main()
