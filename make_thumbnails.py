####
 #
#  GOOD VIBES DEVELOPMENT :)
 #
####
from PIL import Image
import glob, os

size = 400, 400

directory = os.path.dirname( os.path.realpath(__file__) ) + "\\thumb"

if not os.path.exists(directory):
    os.makedirs(directory)

for infile in glob.glob("*"):
	file, ext = os.path.splitext(infile)
	try:
		im = Image.open(infile)
		im.thumbnail(size)
		im.save(directory + "\\" + file + ".thumbnail.jpg", "JPEG")
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)	
	
	except:
		print "Unexpected error..."
		raise	