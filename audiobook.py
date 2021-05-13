import pyttsx3     #step 1
import PyPDF2
book = open('a1.pdf','rb') #step 3 get pdf file
pdfReader = PyPDF2.PdfFileReader(book) #for reading the book
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()              #initilizing it step 2
page = pdfReader.getPage(28)           #step 4 for  to read page no.29
text = page.extractText()                 #for extracting text from pdf
speaker.say(text)
speaker.runAndWait()                    #speaker.say('hey look i can talk') step 1

# use pip install pyttsx3 and pip install PyPDF2 to install these two files.


