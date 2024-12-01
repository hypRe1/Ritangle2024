"""
Some helper functions
"""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def validate(c: list[int]):
    """
    Validate crossword based on the following constraints:
    - There are no zeros and each digit present appears the same number of times in the completed puzzle.
    - Top row digits are all different as are those in the bottom row.

    We can infer from this that the top and bottom rows contain each digit once
    and the middle two rows contain two of each digit.
    """
    if 0 in c:
        return False

    t = c[0:9]
    m = c[9:27]
    b = c[27:36]
    for n in range(1, 10):
        tc = t.count(n)
        mc = m.count(n)
        bc = b.count(n)
        if tc > 1 or mc > 2 or bc > 1:
            return False

    return True


def crossword_str(c: list[int]):
    """
    Crossword string representation
    """
    w = ""
    for i, n in enumerate(c):
        if n == -1:
            w += "| "
        else:
            w += f"|{n}"

        if (i + 1) % 9 == 0:
            w += "|\n"
    return w


def print_crossword(c: list[int]):
    """
    Display crossword in console
    """
    print(crossword_str(c))

def display_crossword(c: list[int]):
    """
    Display crossword as image
    """

    img = Image.open("crossword.jpg").convert('RGB')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("OpenSans-Bold.ttf", 50)

    for i, n in enumerate(c):
        coords = (41+((i%9) * 85), 35+((i//9)*94))
        draw.text(coords,str(n),(0,0,0),font=font)
    img.save('solution.jpg')
    img.show(title="Crossword")
