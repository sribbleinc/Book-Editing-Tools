#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, os.path
try:
    from scribus import *
except ImportError:
    print("This script can only be run inside Scribus.")

REPLACE

############################
##    HELPER FUNCTIONS    ##
############################
def format(number, pageCount):
    """
    Takes page [number] and returns the corresponding filename.
    Default: Images are sorted by sequential numbers with the same number of chars.
        - Modify this method to insert images in a custom order.
    """
    zeros=len(str(pageCount))-len(str(int(number)))
    return "0"*zeros+str(number)+FILETYPE

#######################
##    MAIN METHOD    ##
#######################
def main():
    """
    (1) Opens Scribus .sla file from path if it exists, creates a .sla file if it doesn't.
    (2) Loads images into the pages.
    """
    filename=FILENAME
    try:
        openDoc(filename)
    except:
        newDocument((WIDTH, HEIGHT), MARGINS, PORTRAIT, FIRSTPAGE, UNIT_INCHES, PAGE_2, 0, PAGECOUNT)
        saveDocAs(filename)
        openDoc(filename)
        setDocType(FACINGPAGES, FIRSTPAGERIGHT)
        setInfo(AUTHOR, TITLE, DESCRIPTION)
    try:
        for p in range(FIRSTPAGE, PAGECOUNT+FIRSTPAGE):
            gotoPage(p)
            pid=str(p)
            if p%2 == 1: #image on right
                frame=scribus.createImage(BIND, 0, WIDTH-BIND-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], pid)
            else: #even; image on left
                frame=scribus.createImage(0, 0, WIDTH-BIND-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], pid)
            loadImage(SOURCE+format(p, PAGECOUNT), pid)
        print("Saved: ", saveDoc())
    except:
        print "Problem with creating pages."
    finally: 
        closeDoc()

main()