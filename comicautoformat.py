AUTHOR = "Alana Tran"
TITLE = "Assimilation"
DESCRIPTION = "Life Goes On"
PATH = "./art/"
WIDTH = 9
HEIGHT = 7
FIRSTPAGE = 1
PAGECOUNT = 0 # number of pages in folder
LEFTBIND = .25
RIGHTBIND = -.25

def format(number, pageCount):
    zeros = len(str(pageCount)) - len(str(number))
    return "0"*zeros + str(number)



def main():
    try:
        document = Scripter.openDoc(DESCRIPTION.replace(" ", ""))
    except:
        document = Scripter.newDocument((WIDTH,HEIGHT),(0,0,0,0),PORTRAIT, FIRSTPAGE, PAGECOUNT)
        document.setDocType(FACINGPAGES,FIRSTPAGERIGHT)
        document.setInformation(AUTHOR, TITLE, DESCRIPTION)
        document.saveAs(DESCRIPTION.replace(" ", ""))
    PAGECOUNT = document.pageCount()

    for p in range(FIRSTPAGE, PAGECOUNT+FIRSTPAGE):
        scribus.gotoPage(p)
        imageItem.load(PATH + format(p) + ".png")
            #imageItem.yOffset =
        if p%2 == 1: #image on right
            imageItem.xOffset = LEFTBIND
        else: #even; image on left
            imageItem.xOffset = RIGHTBIND
    
    print("Saved: ", document.save())
    


