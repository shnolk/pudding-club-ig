import os
from PIL import Image, ImageDraw
from PIL import ImageFilter, ImageEnhance
from PIL.ImageFilter import (
    GaussianBlur, MaxFilter
    )
import numpy as np
import PostOnIg
import random
import json
import randomWords
from bing_image_downloader import downloader
import randomWords
import randomObjects
import time
import math


# Resources
# https://pythontic.com/image-processing/pillow/sharpen-filter

paletteRGBCMYK = [ 
	0, 0, 0, # black
	255, 0, 0, # R
	0, 255, 0, # G
	0, 0, 255, # B
	255, 255, 0, # Y
	0, 255, 255, # C
	255, 0, 255, # M
	255,255,255
	# 180,180,180 # w

	]
noColors = random.randint(2,8)

def quantizetopalette(silf, palette = paletteRGBCMYK, dither=Image.FLOYDSTEINBERG):
    """Convert an RGB or L mode image to use a given P image's palette."""

    silf.load()

    # use palette from reference image made below
    palette.load()

    # silf = silf.convert('RGB').convert(mode = "P", matrix = None, dither, Image.WEB)

    im = silf.im.convert("P", 0, palette.im)
    # the 0 above means turn OFF dithering making solid colors
    return silf._new(im)




# ------ counter for image ID -----
def get_var_value(filename="varstore.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

your_counter = get_var_value()
print("Run No. {}".format(your_counter))



mainSearchWord = randomWords.generateWord()

def bingQuery(searchWord):

	downloader.download(searchWord, 
		limit=1,  
		output_dir='dataset', 
		adult_filter_off=True, 
		force_replace=True)

	# image_path = filenames[0]
	try:
		image_path = './dataset/'+ searchWord + '/Image_1.jpg'
		return read_image(image_path)
	except FileNotFoundError:
		image_path = './dataset/'+ searchWord + '/Image_1.png'

	



def read_image(path):
	try: 
		image = Image.open(path)
		return image
	except Exception as e: 
		print(e)
		# need to figure out a way to loop back


# if random.choice([True,False]):
# 	# ------- low res ----------
# 	cropSize = (your_counter % 5) * 50
	
# else:
# cropSize = 500
cropSize = random.randint(50,750)
# shapeSize = int(cropSize/4)
shapeSize = int(cropSize/random.randint(1,12))

def transformImage(dimg):

	dimg = dimg.resize(random.randint(1,cropSize), random.randint(1,cropSize))

	return dimg

def drawSpine(dimg, color):
	
	xy = [(random.randint(-cropSize,cropSize),\
			random.randint(-cropSize,cropSize))
			for i in range(random.randint(3,6))] 
	dctx = ImageDraw.Draw(dimg)  # create drawing context
	dctx.polygon(xy, fill=color)  # draw polygon without outline
	del dctx
	return dimg

def drawSplotch(dimg, color):
	xy = [(random.randint(-cropSize,cropSize),random.randint(-cropSize,cropSize)),\
			(random.randint(-cropSize,cropSize),random.randint(-cropSize,cropSize)) ] 
	dctx = ImageDraw.Draw(dimg)
	dctx.ellipse(xy, fill=color)
	del dctx
	return dimg

def drawScribble(dimg, color, scale):
	x, y = random.randint(-cropSize, cropSize), random.randint(-cropSize, cropSize)
	xyA = [(x, y)]
	status = True
	while status:
		if x <= 0 or x >= cropSize or y <= 0 or y >= cropSize:
			status = False
		else:
			xDirect = random.randint(-scale, scale)
			yDirect = random.randint(-scale, scale)
			for i in range(random.randint(0, cropSize)):
				x += xDirect
				y += yDirect
				xyA.append((x, y))
	xy = tuple(xyA) # convert array of points to tuple

	dctx = ImageDraw.Draw(dimg)  # create drawing context
	dctx.point(xy, fill=color)  # draw points
	del dctx  # destroy drawing context
	return dimg

listOfObjects = []

def drawObjects(dimg, position = [random.randint(-cropSize, cropSize), 
								  random.randint(-cropSize, cropSize)], object="tree-1"):
	try: 
		fgPre = Image.open('./objects/'+ object + '.png')
	except Exception as e: 
		print(e)
	x, y= position[0], position[1]
	resizeSize = [random.randint(1, int(cropSize/2)),
					random.randint(1, int(cropSize/2))]

	fg = fgPre.resize(list(resizeSize))
	dimg.paste(fg, (x,y), fg)
	return dimg

def drawImages(dimg, simg):
	x, y= random.randint(-cropSize, cropSize), random.randint(-cropSize, cropSize)
	# resizeSize = random.randint(1, int(cropSize/2))
	resizeSize = [random.randint(1, int(cropSize/2)),
					random.randint(1, int(cropSize/2))]

	simg = simg.resize(list(resizeSize))
	dimg.paste(simg, (x,y))
	return dimg


def createObjects(dimg):
	scene = randomObjects.generateScene()
	clumpAmount = 1
	for i in scene[1]:
		for j in range(random.randint(0, 14)):
			# drawing a clump / cluster of items
			xA, yA = random.randint(-cropSize, cropSize), random.randint(-cropSize, cropSize)
			print("----- Making a "+ i + " -----")
			dimg = drawObjects(dimg, [xA + (random.randint(-clumpAmount,clumpAmount) * 2), 
												yA + (random.randint(-clumpAmount,clumpAmount) * 2)], i)

	return [dimg, scene[0]]




# ----- main process ------





def process(dimg, blurAmount=random.randint(1,5)):
	xsize, ysize = dimg.size
	randomAnchorX, randomAnchorY = 0, 0
	try: 
		randomAnchorX = random.randint(cropSize, xsize)
		randomAnchorY = random.randint(cropSize, ysize)
	except ValueError:
		dimg = Image.new('RGB', (cropSize, cropSize), (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	box = (randomAnchorX - cropSize, randomAnchorY - cropSize, randomAnchorX, randomAnchorY)
	# dimg = dimg.filter(GaussianBlur(blurAmount))
	if random.choice((True, False, False, False)):
		dimg = dimg.filter(GaussianBlur(blurAmount))
	dimg = dimg.crop(box)
	# max filter (bright-colored boxes)
	# rimg = simg.filter(MaxFilter(size=9))

	# edge enhance
	# if random.randint(0,7) == 1:
	# 	dimg = dimg.filter(ImageFilter.EDGE_ENHANCE)

	# if random.randint(0,50) == 1:
	# 	dimg  = dimg.transpose(Image.ROTATE_90)
	# if random.randint(0,50) == 1:
	# 	dimg  = dimg.transpose(Image.ROTATE_180)
	# if random.randint(0,10) == 1:
	dimg = dimg.convert('RGB').convert(mode = "P", matrix = None, dither = Image.FLOYDSTEINBERG,
		palette = Image.WEB, colors = noColors)

	if dimg.mode != 'RGB': dimg = dimg.convert('RGB')


	
	return dimg

runQuery = True
while(runQuery):
	img = bingQuery(mainSearchWord)
	try:
		testX, textY = img.size
	except AttributeError:
		runQuery = True
	else:
		runQuery = False


img = process(img,1)

outputScene = []
script = ""
# procedure
for y in range(random.randint(1, 4)):
	colorInstance = randomWords.generateColor()
	for x in range(random.randint(1, 3)):
		img = drawSplotch(img, colorInstance)
		pick = random.randint(0, 6)
		if pick == 0:
		    img = drawSpine(img, colorInstance)
		# if pick == 1:
		#     img = drawSplotch(img, colorInstance)
		if pick == 2:
			img = drawScribble(img, colorInstance, random.randint(1,3))
		if pick == 3:
			img = process(img)
		else: 
			for z in range(random.randint(1,2)):
				outputScene = createObjects(img)
			# if random.choice([True, False, False, False]):
			script += outputScene[1] + ". "
			img = outputScene[0]
		# if pick == 5:

		# 	search = randomWords.generateWord()
		# 	img = drawImages(img, bingQuery(search))



# ----- display image ------
# img.show()

# resizeSize = 900
# img = img.resize((resizeSize,resizeSize))

# img = img.convert("1", 8)
# img = img.convert('RGB').convert(mode = "P", matrix = None, dither = Image.FLOYDSTEINBERG,
# 				 palette = random.choice([Image.ADAPTIVE, paletteRGBCMYK]), colors = noColors)
# img = img.convert('RGB').convert(mode = "P", matrix = None, dither = Image.FLOYDSTEINBERG,
# 				 palette = Image.ADAPTIVE, colors = noColors)


palimage = Image.new('P', (16, 16))
palimage.putpalette(paletteRGBCMYK * 32)
img = quantizetopalette(img, palimage, dither=Image.FLOYDSTEINBERG)
# img = img.quantize(noColors, Image.MEDIANCUT, random.randint(0,6), paletteRGBCMYK, dither = Image.FLOYDSTEINBERG)

if img.mode != 'RGB':
    img = img.convert('RGB')

# caption the image
def createCaption():

	hardwareFile = open("hardware.dat", "r")
	if hardwareFile.mode == "r":
		hardware = hardwareFile.read()
	# unused caption content:
	# + randomWords.generateFlowers() + "\n-----------------------------------------------------" \
	captionString = script + "\nQuery: " + mainSearchWord + " \n" + \
					time.strftime("%H:%M:%S %d-%m-%y ") + \
					"\nHardware: " + hardware + "\nAttempt " + str(your_counter)
	print(captionString)

	return captionString


# save the image
png_save_name = "pudd" + str(your_counter) + '.png'
img.save('./dataset/'+ mainSearchWord + '/' + png_save_name)


imgRSZ = Image.open('./dataset/'+ mainSearchWord + '/' + png_save_name)
imgRSZ = imgRSZ.resize((700,700))

save_name = "pudd" + str(your_counter) + '.jpg'
imgRSZ.save('./dataset/'+ mainSearchWord + '/' + save_name, optimize = True, quality = 100)


# img.show()

# upload the image
PostOnIg.upload('./dataset/'+ mainSearchWord + '/' + save_name, createCaption())

# os.remove('./dataset/')


