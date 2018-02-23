#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
try:
    from scribus import *
except ImportError:
    print("This script can only be run inside Scribus.")

############################
##    SCRIPT ARGUMENTS    ##
############################
AUTHOR = "Alana Tran" # Creator(s) of document's contents.
TITLE = "Assimilation" # Name of document.
DESCRIPTION = "Life Goes On" # Description of document.
WIDTH = 9 # Width of page.
HEIGHT = 7 # Height of page.
MARGINS = (0,0,0,0) # Page Margins of document. (left, right, top, bottom)
BIND = .25 # Gap for where document is physically bound.

### NOTE: Script assumes all images are the same filetype. ###
SOURCE = "/Users/Alana.Tran/Desktop/Book-Editing-Tools/art/" # Location of image files. 
FILETYPE = ".png" # Filetype of images in SOURCE.
PAGECOUNT = len(os.listdir(SOURCE)) # Number of images in SOURCE.
FIRSTPAGE = 1 # Starting number of images in source.
TARGET = "/Users/Alana.Tran/Desktop/Book-Editing-Tools/" # Location of Scribus (.sla) file.

### Add or remove variables here as needed. ###
FILENAME = TARGET + DESCRIPTION.replace(" ", "") + ".sla" # Name of Scribus .sla file.

############################
##    HELPER FUNCTIONS    ##
############################
def format(number, pageCount):
    """
    Takes page [number] and returns the corresponding filename.
    Default: Images are sorted by sequential numbers with the same number of chars.
        - Modify this method to insert images in a custom order.
    """
    zeros = len(str(pageCount)) - len(str(int(number)))
    return "0"*zeros + str(number) + FILETYPE

#######################
##    MAIN METHOD    ##
#######################
def main():
    """
    (1) Opens Scribus .sla file from path if it exists, creates a .sla file if it doesn't.
    (2) Loads images into the pages.
    """
    filename = FILENAME
    try:
        openDoc(filename)
    except:
        newDocument((WIDTH,HEIGHT),MARGINS, PORTRAIT, FIRSTPAGE, UNIT_INCHES, PAGE_2, 0, PAGECOUNT)
        saveDocAs(filename)
        openDoc(filename)
        setDocType(FACINGPAGES,FIRSTPAGERIGHT)
        setInfo(AUTHOR, TITLE, DESCRIPTION)
    try:
        for p in range(FIRSTPAGE, PAGECOUNT+FIRSTPAGE):
            gotoPage(p)
            pid = str(p)
            if p%2 == 1: #image on right
                frame = scribus.createImage(BIND, 0, WIDTH-BIND-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], pid)
            else: #even; image on left
                frame = scribus.createImage(0, 0, WIDTH-BIND-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], pid)
            loadImage(SOURCE + format(p, PAGECOUNT), pid)
        print("Saved: ", saveDoc())
    except:
        print "Problem with creating pages."
    finally: 
        closeDoc()

main()