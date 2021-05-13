import pyttsx3     #step 1
import PyPDF2
book = open('a1.pdf','rb')                          #step 3 get pdf file
pdfReader = PyPDF2.PdfFileReader(book)              #for reading the book
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()                  #initilizing it step 2
for num in range(13,pages):                 # will start from page number 14 on the pdf
    page = pdfReader.getPage(13)           #step 4 for  to read from page no 14.
    text = page.extractText()                 #for extracting text from pdf
    speaker.say(text)
    speaker.runAndWait()                    #speaker.say('hey look i can talk') 


# use pip install pyttsx3 and pip install PyPDF2 to install these two files.


