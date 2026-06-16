from pyfiglet import Figlet
import sys
import random

fig = Figlet()
fonts = fig.getFonts()


if len(sys.argv) == 1:
    font = random.choice(fonts)
    


