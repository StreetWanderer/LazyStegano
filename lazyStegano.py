from math import sqrt, ceil
from random import randint
from PIL import Image

def encode(secretTextFile, outputTarget):

	with open (secretTextFile, "r") as secretFile:
		secretText = secretFile.read()

	charNumbers = []

	for c in secretText:
		charNumbers.append(ord(c))

	## DECODE TESTING ##
	#with open ('decode.txt', "w+") as decoded:
	#	for n in charNumbers:
	#		decoded.write(unichr(n))
	##

	imgSize = int(ceil(sqrt(len(charNumbers) - 1)))
	print imgSize
	canvas = Image.new("L", (imgSize,imgSize))
	strPos = 0
	for x in range(imgSize):
		for y in range(imgSize):
			if strPos < len(charNumbers):
				canvas.putpixel((x, y), charNumbers[strPos])
				strPos += 1
			else:
				canvas.putpixel((x, y), randint(32, 126))

	canvas.save(outputTarget)
	print 'DONE : Created '+outputTarget+' from '+secretTextFile

def decode(encodedImage, outputTarget):
	canvas = Image.open(encodedImage)
	print canvas.size
	with open ('decode.txt', "w+") as decoded:
		for x in range(canvas.size[0]):
			for y in range(canvas.size[1]):
				pixel = canvas.getpixel((x,y))
				decoded.write(unichr(pixel))

	print 'DONE : Created '+outputTarget+' from '+encodedImage

encode('README.md', 'message.png')
decode('message.png', 'decode.txt')