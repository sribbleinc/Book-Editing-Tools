import os, os.path
try:
    from scribus import *
except ImportError:
    print("This script can only be run inside Scribus.")

FILENAME="test.sla"

def makeTextFrame(p):
    gotoPage(p)
    createText(4, 5.5, 2, 2, str(p))
    setText(str(p), str(p))

def create_file_test():
    print "running create_file_test..."
    newDocument((8, 11), (.5,.5,.5,.5), PORTRAIT, 1, UNIT_INCHES, PAGE_2, 0, 5)
    saveDocAs(FILENAME)
    openDoc(FILENAME)
    closeDoc()
    return os.path.isfile(FILENAME)

def insert_frames_test():
    print "running insert_frames_test..."
    openDoc(FILENAME)
    for p in range(1,6):
        makeTextFrame(p)
        if not getPageItems():
            return False
    saveDoc()
    closeDoc()
    return True

def append_pages_test():
    print "running append_pages_test..."
    openDoc(FILENAME)
    for p in range(6,8):
        newPage(-1)
        makeTextFrame(p)
    saveDoc()
    total = pageCount()
    print "pagecount: " + str(total)
    closeDoc()
    return total == 7

def insert_pages_test():
    print "running insert_pages_test..."
    openDoc(FILENAME)
    for p in range(3,5):
        newPage(3)
    for p in range(9,4,-1):
        gotoPage(p)
        setNewName(str(p), getPageItems()[0][0])
    for p in range(3,5):
        gotoPage(p)
        makeTextFrame(p)
    for p in range(1, pageCount()+1):
        gotoPage(p)
        print getPageItems()
    saveDoc()
    total = pageCount()
    print "pagecount: " + str(total)
    closeDoc()
    return total == 9

def main():
    results = []
    create_file_test_result = create_file_test()
    results.append(create_file_test_result)
    print "result: " + str(create_file_test_result)
    insert_frames_test_result = insert_frames_test()
    results.append(insert_frames_test_result)
    print "result: " + str(insert_frames_test_result)
    append_pages_test_result = append_pages_test()
    results.append(append_pages_test_result)
    print "result: " + str(append_pages_test_result)
    insert_pages_test_result = insert_pages_test()
    results.append(insert_pages_test_result)
    print "result: " + str(insert_pages_test_result)
    print str(len(filter(lambda v: v == True, results))) + " tests passed out of " + str(len(results)) +"."
    os.remove(FILENAME)

main()


