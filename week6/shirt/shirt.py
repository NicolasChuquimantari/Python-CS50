import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) or not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

if splitext(input_filepath)[1] != splitext(output_filepath)[1]:
        sys.exit("Input and output have different extensions")

    
