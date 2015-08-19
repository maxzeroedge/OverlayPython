from PIL import Image
import sys

def getColor(rep):
	if rep == 0:
		return (255,255,255)
	elif rep == 1:
		# Light Red
		return (255,69,40)
	elif rep == 2:
		# Dark Red
		return (153,20,0)
	elif rep == 3:
		# Light Pink
		return (255,153,192)
	elif rep == 4:
		# Dark Pink
		return (224,0,86)
	elif rep == 5:
		# Light Purple
		return (254,163,249)
	elif rep == 6:
		# Dark Purple
		return (214,0,200)
	elif rep == 7:
		# Light Blue
		return (188,153,255)
	elif rep == 8:
		# Dark Blue
		return (85,0,244)
	elif rep == 9:
		# Light Light Blue
		return (153,223,255)
	elif rep == 10:
		# Dark Light Blue
		return (0,148,214)
	elif rep == 11:
		# Light Grenn
		return (112,255,187)
	elif rep == 12:
		# Dark Green
		return (0,102,53)
	elif rep == 13:
		# Light Yellow
		return (252,255,153)
	elif rep == 14:
		#Dark Yellow
		return (179,183,0)
	else:
		return (188,188,188)

fileList = [] #Populate this with the URL or the path of files 
imList = []
newdat = []
# oldcol = 0
size = [0,0]

for f in fileList:
	imList.append(Image.open(f))
	if size == [0,0]:
		size = [Image.open(f).size[0], Image.open(f).size[1]]
	elif size != [Image.open(f).size[0], Image.open(f).size[1]]:
		print "Size Mismatching. Please keep the size of images same"
		sys.exit(1)

newimg = Image.new('RGB',(imList[0].size[0], imList[0].size[1]))

for x in range(0, imList[0].size[0]):
	temp = []
	for y in range(0, imList[1].size[1]):
		temp.append(0)
	newdat.append(temp)
for i in range(0, len(imList)):
	im = imList[i]
	for x in range(0, im.size[0]):
		for y in range(0, im.size[1]):
			# Compare pixels at x,y
			coord = x,y
			if im.getpixel(coord) != (255,255,255) :
					newdat[x][y] += 1
					
for x in range(0,len(newdat) ):
	for y in range(0, len(newdat[x])):
		color = newdat[x][y]
		coord = x,y
		newimg.putpixel(coord, getColor(color))
		# if color != oldcol:
			# print str(color)
			# oldcol = color

output = "" # Populate this with the location of where to save the file 
newimg.save(output, "TIFF")
# newimg.show()

