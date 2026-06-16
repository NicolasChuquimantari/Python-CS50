from pyfiglet import Figlet
import sys
import random

fig = Figlet()
fonts = fig.getFonts()


if len(sys.argv) == 1:
    text = input("Enter text: ")
    font = random.choice(fonts)
    fig.setFont(font=font)

elif len(sys.argv) == 3:
    text = input("Enter text: ")
    if sys.argv[1] not in ["-f", "--font"]:
        if sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
    fig.setFont(font=sys.argv[2])

else:
    sys.exit("Invalid usage")

print(figlet.renderText(text))






