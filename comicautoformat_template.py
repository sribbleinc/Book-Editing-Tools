import os, os.path
try:
    from scribus import *
except ImportError:
    print("This script can only be run inside Scribus.")

#REPLACE

###########################
##        METHODS        ##
###########################

def createDocument():
    """
    Create a new .ska file from SCRIPT ARGUMENTS above.
    """
    newDocument((WIDTH, HEIGHT), MARGINS, ORIENTATION, FIRSTPAGE, UNIT_INCHES, PAGETYPE, POSITION, PAGECOUNT)
    setDocType(FACING, SIDE)
    setInfo(AUTHOR, TITLE, DESCRIPTION)
    saveDocAs(FILENAME)

def insertFiles(files, f=scribus.createImage):
    """
    Insert files into the document using frame function f.
    """
    for p in range(pageCount(),PAGECOUNT+FIRSTPAGE-1,-1):
        gotoPage(p)
        setNewName(str(p), getObjectName(p))
        new_bind = -BIND+MARGINS[0]+MARGINS[1] if isRightPage(p) else -BIND+MARGINS[0]
        moveObjectAbs(new_bind, 0, str(p))
    for p in range(FIRSTPAGE, PAGECOUNT+FIRSTPAGE):
        gotoPage(p)
        frame=createFrame(p, f)
        loadImage(SOURCE+files[p], str(p))

def createFrame(p, f):
    """
    Creates frame with format function f for a page p.
    """
    if isRightPage(p):
        frame=f(-BIND+MARGINS[0]+MARGINS[1], 0, WIDTH-BIND-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], str(p))
    elif isLeftPage(p): #page on left
        frame=f(-BIND+MARGINS[0], 0, WIDTH-BIND-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], str(p))
    else: #page in middle
        frame=f(0, 0, WIDTH-MARGINS[0]-MARGINS[1], HEIGHT-MARGINS[2]-MARGINS[3], str(p))
    return frame

def format(files):
    global FIRSTPAGE
    if os.path.isfile(FILENAME):
        openDoc(FILENAME)
        if FIRSTPAGE == -1:
            FIRSTPAGE = pageCount() + 1
        reorderPages()
    else:
        createDocument()
        if FIRSTPAGE == -1:
            FIRSTPAGE = 1
    f=dict(zip(range(FIRSTPAGE, FIRSTPAGE+PAGECOUNT), files))
    try:
        insertFiles(f)
        print("Saved: ", saveDoc())
    except:
        print "Problem with creating pages."
    finally: 
        closeDoc()

############################
##    HELPER FUNCTIONS    ##
############################

def getObjectName(p, index=0):
    """
    Get object from page p.
    """
    gotoPage(p)
    return getPageItems()[index][0]

def isLeftPage(p):
    """
    Checks if page is left page.
    """
    return getPageType(p) == 0

def isRightPage(p):
    """
    Checks if page is right page.
    """
    return getPageType(p) == 2

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

#######################
##    MAIN METHOD    ##
#######################

def main():
    """
    (1) Opens Scribus .sla file from path if it exists, creates a .sla file if it doesn't.
    (2) Loads images into the pages.
    """
    format(FILES)

main()