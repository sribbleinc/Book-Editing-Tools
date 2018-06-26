def format(number, pageCount):
    """
    Takes page [number] and returns the corresponding filename.
    Default: Images are sorted by sequential numbers with the same number of chars.
        - Modify this method to insert images in a custom order.
    """
    zeros=len(str(pageCount))-len(str(int(number)))
    return "0"*zeros+str(number)+FILETYPE