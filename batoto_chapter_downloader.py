import os
from sys import argv

def numberize(n, k=6):
   return '0'*(k-len(str(n)))+str(n)

image_path, number = argv[1:]

for i in xrange(1,int(number)+1):
    os.system("wget {0}/img{1}.jpg".format(image_path, numberize(i)))
