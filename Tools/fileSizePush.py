import os
for root, dirs, files in os.walk(os.getcwd()):
	for fn in files:
	      path = os.path.join(root, fn)
	      size = os.stat(path).st_size
	      if (size>100000000):
		      print "{} (Size: {})".format(path, size)
