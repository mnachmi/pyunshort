#!/usr/bin/env python
import pdb
import urllib2 as urllib
import time;
import logging
import sys, getopt, os

def main():
        if sys.version_info < (2, 7):
            print "please upgrade your python !!"
            sys.exit(0)
	logging.basicConfig(filename='file.log',level=logging.DEBUG, 
                     format='%(asctime)s %(message)s')
	input = ''
	try:
  	    opts, args = getopt.getopt(sys.argv[1:], 'hf:', ['help', 'file='])
 	except getopt.GetoptError as err:
 		print (err)
 	 	sys.exit()

	for o,a in opts:
		if o in ('-h', '--help'):
   			usage()
   			sys.exit()
  		elif o in ('-f', '--file'):
   			#pdb.set_trace()
                        if os.path.isfile(a):
   				input = a
  			else:
  				print "{0} is not a file".format(a)
                                sys.exit(0)

	infile  = open(input,'r')
	outfile = open('unshort.txt','a')
	i=1
	for url in infile:
		shortned(url, outfile, i)
		i = i + 1
	print('Done')
	infile.close()
        outfile.close()

def usage():
	print "unshort twitter urls !\nand save them to file."

def shortned(url, outfile, i):

	try:
		resp = urllib.urlopen(url, timeout = 20)
		code = resp.getcode()
		print i, resp.url
		outfile.write("{0}\t{1}".format((resp.url),url))
		outfile.flush()
	except Exception as e  :
		logging.error(str(e).rstrip('\n') + ' ' + str(url))


if __name__ == "__main__" : main()
