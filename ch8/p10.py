"""
Paint Fill: Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color, fill in the surrounding area until the color changes from the original color. 
"""
from enum import Enum


class Color(Enum):
	Black = 1
	White = 2
	Red = 3
	Yellow = 4
	Green = 5

def paintFill(image, x, y, newC):
	currColor = image[x][y]
	if currColor == newC: 
		return False
	return paintFillHelper(image, x, y, newC, currColor)

def paintFillHelper(image, x, y , newC, oldC):

	if y >= len(image) or y < 0 or x >= len(image[0]) or x < 0:
		return False

	currColor = image[x][y]
	if currColor == oldC:
	   image[x][y] = newC
	   paintFillHelper(image, x-1, y, newC, oldC)
	   paintFillHelper(image, x+1, y, newC, oldC)
	   paintFillHelper(image, x, y-1, newC, oldC)
	   paintFillHelper(image, x, y+1, newC, oldC)

	return True

