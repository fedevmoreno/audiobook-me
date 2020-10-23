import pyttsx3
import PyPDF2

book = open('books/the_art_of_war.pdf', 'rb') # Here you need to replace the path name of your book.

book_reader = pyttsx3.init()
book_reader.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

pdf_reader = PyPDF2.PdfFileReader(book)

first_page_to_read = 3 # Here you have to put the first page number you want to listen to (number of array'index, if it is page number 4, so you have to put 3).

pages = pdf_reader.numPages

for num in range(first_page_to_read, pages):
   page = pdf_reader.getPage(num)
   text = page.extractText()
   book_reader.say(text)
   book_reader.runAndWait()

'''
You can change the book reader voice.

Here are some Apple voice ids (if you use Windows or Linux, you have to find the right ids):

es_AR (Spanish voice with Argentinian accent):

com.apple.speech.synthesis.voice.diego

es_ES (Spanish voice with Spanish accent):

com.apple.speech.synthesis.voice.monica

en_US (English voices with American accent):

com.apple.speech.synthesis.voice.Alex
com.apple.speech.synthesis.voice.daniel
com.apple.speech.synthesis.voice.Fred
com.apple.speech.synthesis.voice.samantha
com.apple.speech.synthesis.voice.Victoria
'''
