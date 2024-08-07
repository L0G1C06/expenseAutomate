from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='pt')

def print_all_words(result):
    for sublist in result:
        if isinstance(sublist, list):
            print_all_words(sublist)
        elif isinstance(sublist, tuple):
            word = sublist[0]
            print(word)

def makeOCR(image):
    result = ocr.ocr(image)
    words = print_all_words(result=result)
    return words