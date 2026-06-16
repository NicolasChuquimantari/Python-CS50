from pyfiglet import Figlet
import sys
import random

fig = Figlet()
fonts = fig.getFonts()


if len(sys.argv) == 1:
    font = random.choice(fonts)
    fig.setFont(font=font)

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        if sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
    fig.setFont(font=sys.argv[2])

else:
    sys.exit("Invalid usage")

text = input("Enter text: ")
print(figlet.renderText(text))






