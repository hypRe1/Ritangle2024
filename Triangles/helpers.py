"""
Some helper functions
"""

from math import isqrt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def valid_triangle(a: int, b: int, c: int) -> bool:
    """
    Check if triangle can be formed from side lengths
    """
    return (a + b > c) and (a + c > b) and (b + c > a) 

def is_triangular(n: int) -> bool:
    """
    Checks if a number is triangular
    """
    if n < 0:
        return False
    m = isqrt(8 * n + 1)
    return m * m == 8 * n + 1 and (m - 1) % 2 == 0

def validate_crossword(c: list[int]) -> bool:
    starts = [0,2,3,4,5,6,7,9,10,12,14,17,18,21]
    for s in starts:
        if c[s] == 0:
            return False
    
    return True

def crossword_str(c: list[int]) -> str:
    w = ""
    for i, n in enumerate(c):
        if n == -1:
            w += "| "
        else:
            w += f"|{n}"

        if (i + 1) % 6 == 0:
            w += "|\n\n"
    return w

def display_crossword(c: list[int]):
    """
    Display crossword as image
    """

    img = Image.open("crossword.jpg").convert('RGB')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("OpenSans-Bold.ttf", 50)

    for i, n in enumerate(c):
        coords = (45+((i%6) * 103), 35+((i//6)*103))
        draw.text(coords,str(n),(0,0,0),font=font)
    img.save('solution.jpg')
    img.show(title="Crossword")
