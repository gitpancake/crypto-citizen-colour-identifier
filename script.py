from PIL import Image
import ntpath
import os

def identifyImageColour(filePath):
	fileName = ntpath.basename(filePath)
	fileName = fileName.replace('.png', '')

	im = Image.open(filePath) # Can be many different formats.

	rgb_im = im.convert('RGB')
	r, g, b = rgb_im.getpixel((0, 0))
	coloursArray = [r,g,b]
	
	largestNum = max(coloursArray)
	numberPosition = (coloursArray.index(largestNum))

	basePath = './colours/'

	#array = [r,g,b], so position 2 = blue
	if (numberPosition == 2):
		# if blue shade > 145 then darker, so variant b
		if (b > 145):
			im.save(basePath + 'b_' + fileName + '.png')
		# otherwise, lighter, so variant a
		else:
			im.save(basePath + 'a_' + fileName + '.png')

	if (numberPosition == 0):
		# no green = the colour must be red
		if (g == 0):
			im.save(basePath + 'd_' + fileName + '.png')
		# green = the colour must be grey
		else:
			im.save(basePath + 'c_' + fileName + '.png')

files = (os.listdir('./files'))

for file in files:
	identifyImageColour('./files/' + file)
