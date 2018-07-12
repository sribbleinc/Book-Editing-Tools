import os, os.path
try:
    from scribus import *
except ImportError:
    print("This script can only be run inside Scribus.")

REPLACE

############################
##    HELPER FUNCTIONS    ##
############################

def createDocument():
    """
    Create a new .ska file from SCRIPT ARGUMENTS above.
    """
    newDocument((WIDTH, HEIGHT), MARGINS, PORTRAIT, FIRSTPAGE, UNIT_INCHES, PAGE_2, 0, PAGECOUNT)
    saveDocAs(FILENAME)
    setDocType(FACINGPAGES, FIRSTPAGERIGHT)
    setInfo(AUTHOR, TITLE, DESCRIPTION)

def getObjectName(p, index=0):
    """
    Get object from page p.
    """
    gotoPage(p)
    return getPageItems()[index][0]

def insertImages():
    """
    Insert images into the document.
    """
    for p in range(pageCount(),PAGECOUNT+FIRSTPAGE-1,-1):
        gotoPage(p)
        setNewName(str(p), getObjectName(p))
        moveObjectAbs(-BIND*-1**(p%2), 0, str(p))
    for p in range(FIRSTPAGE, PAGECOUNT+FIRSTPAGE):
        gotoPage(p)
        frame=style(p)
        loadImage(SOURCE+IMAGES[p], str(p))

def reorderPages():
    """
    Insert pages into the document for desired order.
    """
    old_pagecount=pageCount()
    if FIRSTPAGE <= old_pagecount:
        for i in range(PAGECOUNT):
            newPage(FIRSTPAGE)
    else:
        for i in range(PAGECOUNT):
            newPage(-1)

def style(p):
    """
    Formats the image frame for a page.
    """
    if p%2 == 1: #image on right
        frame=scribus.createImage(BIND, 0, WIDTH-BIND-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], str(p))
    else: #even; image on left
        frame=scribus.createImage(-BIND, 0, WIDTH-BIND-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], str(p))
    return frame

#######################
##    MAIN METHOD    ##
#######################

def main():
    """
    (1) Opens Scribus .sla file from path if it exists, creates a .sla file if it doesn't.
    (2) Loads images into the pages.
    """
    if os.path.isfile(FILENAME): 
        openDoc(FILENAME)
        reorderPages()
    else:
        createDocument()
    try:
        insertImages()
        print("Saved: ", saveDoc())
    except:
        print "Problem with creating pages."
    finally: 
        closeDoc()

# main()