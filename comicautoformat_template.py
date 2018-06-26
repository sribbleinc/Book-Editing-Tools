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

def getObjectName(p, index=0):
    gotoPage(p)
    return getPageItems()[index][0]

def style(p):
    """
    Formats the image frame for a page.
    """
    if p%2 == 1: #image on right
        frame=scribus.createImage(BIND, 0, WIDTH-BIND-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], str(p))
    else: #even; image on left
        frame=scribus.createImage(0, 0, WIDTH-BIND-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], str(p))
    return frame

def reorderPages():
    """
    Move pages to make room for new ones.
    """
    old_pagecount=pageCount()
    gotoPage(FIRSTPAGE)
    if FIRSTPAGE <= old_pagecount:
        importPage(filename, (FIRSTPAGE, old_pagecount), 1, old_pagecount, 1)
    else:
        for i in range(PAGECOUNT):
            newPage(-1)

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
        reorderPages()
    except:
        newDocument((WIDTH, HEIGHT), MARGINS, PORTRAIT, FIRSTPAGE, UNIT_INCHES, PAGE_2, 0, PAGECOUNT)
        saveDocAs(filename)
        openDoc(filename)
        setDocType(FACINGPAGES, FIRSTPAGERIGHT)
        setInfo(AUTHOR, TITLE, DESCRIPTION)
    try:
        for p in range(FIRSTPAGE, PAGECOUNT+FIRSTPAGE):
            gotoPage(p)
            if getPageItems(): #Is not blank page.
                deleteObject(str(p))
            frame=style(p)
            loadImage(SOURCE+IMAGES[p], str(p))
        print("Saved: ", saveDoc())
        for p in range(PAGECOUNT+FIRSTPAGE,PAGECOUNT()+1):
            gotoPage(p)
            setNewName(str(p), getObjectName(p))
            moveObjectAbs(BIND*(p%2), 0, str(p))
    except:
        print "Problem with creating pages."
    finally: 
        closeDoc()

# main()