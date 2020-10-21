# import libraries
import pyttsx3
import PyPDF2

# load PDF to be read
content = open('TheRaven.pdf', 'rb')
#print(type(content))

Reader = PyPDF2.PdfFileReader(content)

# get number of pages in document
pages = Reader.numPages
print(pages)

read_out = pyttsx3.init()

# set Japanese voice
voices = read_out.getProperty('voices')
read_out.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0')

# loop through the pages and read out 
for num in range(1, pages):
    page = Reader.getPage(num)

    text = page.extractText()
    read_out.say(text)

    read_out.runAndWait()