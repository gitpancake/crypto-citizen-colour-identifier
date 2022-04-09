from PIL import Image
import ntpath
import os

basePath = './colours/'

if not os.path.exists(basePath):
	os.makedirs(basePath)

def identifyImageColour(filePath):
	fileName = ntpath.basename(filePath)
	fileName = fileName.replace('.png', '')

	im = Image.open(filePath) # Can be many different formats.

	rgb_im = im.convert('RGB')
	r, g, b = rgb_im.getpixel((0, 0))
	coloursArray = [r,g,b]
	
	largestNum = max(coloursArray)
	numberPosition = (coloursArray.index(largestNum))

	#array = [r,g,b], so position 2 = blue
	if (numberPosition == 2):
		# if blue shade < 150, then lighter variant
		if (b < 145):
			im.save(basePath + 'a_' + fileName + '.png')
		# otherwise, darker variant
		else:
			im.save(basePath + 'b_' + fileName + '.png')

	if (numberPosition == 0):
		# green = the colour must be grey
		if (g > 0):
			im.save(basePath + 'c_' + fileName + '.png')
		# no green = the colour must be red
		else:
			im.save(basePath + 'd_' + fileName + '.png')

files = (os.listdir('./files'))

for file in files:
	identifyImageColour('./files/' + file)
