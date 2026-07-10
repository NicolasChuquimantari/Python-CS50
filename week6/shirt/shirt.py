import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
    sys.exit("Input and output have different extensions")

if not sys.argv[1].endswith((".jpg", ".jpeg", ".png")) or not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

try:
     shirt = Image.open("shirt.png")
     picture = Image.open(sys.argv[1])
     size = shirt.size
     picture = ImageOps.fit(picture, size)
     picture.paste(shirt, shirt)
     picture.save(sys.argv[2])

except FileNotFoundError:
     sys.exit("input does not exist")



