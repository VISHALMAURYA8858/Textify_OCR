from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 

root = Tk(  )

def readFimage():
    path = PathTextBox.get('1.0','end-1c')
    if path:
        im = Image.open(path)
        text = pytesseract.image_to_string(im, lang = 'eng')
        ResultTextBox.delete('1.0',END)
        ResultTextBox.insert(END,text)
    else:
        ResultTextBox.delete('1.0',END)
        ResultTextBox.insert(END,"FILE CANNOT BE READ")
    

def OpenFile():
    name = askopenfilename(initialdir="/",
                           filetypes =(("PNG File", "*.png"),("BMP File", "*.bmp"),("JPEG File", "*.jpeg")),
                           title = "Choose a file."
                           ) 
    PathTextBox.delete("1.0",END)
    PathTextBox.insert(END,name)
Title = root.title("TEXTIFY:OCR")
path = StringVar()

Textify = PhotoImage(file="Textify_3_320x100.png")
HeadLabel1 = Label(image=Textify)
HeadLabel1.grid(row = 1,column = 1)

HeadLabel1 = Label(root,text="Image to Text Recogniser",fg="brown",font="Cookie 20 underline")
HeadLabel1.grid(row = 2,column = 1)

InputLabel = Label(root,text = "SELECT IMAGE",fg="black")
InputLabel.grid(row=4,column=1,pady=10)

Browse_btn = PhotoImage(file="BrowseF.png")
img_label =Label(image=Browse_btn)

BrowseButton = Button(root,image=Browse_btn,command = OpenFile)
BrowseButton.grid(row=5,column=1,pady=10)

PathLabel = Label(root,text = "PATH:",fg="blue")
PathLabel.grid(row = 6,column=1,sticky=(W))

PathTextBox = Text(root,height = 2)
PathTextBox.grid(row = 7,column = 1)

ReadButton = Button(root,text="GENERATE TEXTS",command = readFimage)
ReadButton.grid(row =8,column = 1,pady=50)

DataLabel = Label(root,text = "TEXTS IN IMAGE:",fg="blue")
DataLabel.grid(row = 9,column=1,sticky=(W))

ResultTextBox = Text(root,height =10,font="Consolas 11")
ResultTextBox.grid(row = 10,column = 1)

root.mainloop()
