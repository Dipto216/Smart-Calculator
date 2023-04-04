from tkinter import *
import math
from pygame import mixer  #mixer any  music play korte help kore
import speech_recognition  #audio ke text e convert kore

mixer.init() # audio function


def click(value):
    ex = entryField.get()
    answer = ''

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]  # 78
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mul(a, b):
    return a * b
def div(a, b):
    return a / b



operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
             } # can you divide 64 divide 4
               # can you multiply 35 divide 5
            # multiply 35 and 4
            # divide  35 and 4
            #deferous 25 minus 4
            #addition 34 + 4


def findNumbers(t):
    l=[]  # 2 ta nmbr ke list e add kore
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

def audio():
    mixer.music.load('music1.mp3')# first of all i will in load music
    mixer.music.play() # this methord i will call music
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m: #object in microphone
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)  #duita sentence er modde time
            voice=sr.listen(m)  # voice sune
            text=sr.recognize_google(voice)  # voice ke text e convert kore

            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:  # Operation er uppercase
                if word.upper() in operations.keys():
                    l=findNumbers(text_list)
                    print(l)
                    result=operations[word.upper()](l[0],l[1]) # list e 2 ta nmbr ke 2 ta index e rakbe
                    entryField.delete(0,END)
                    entryField.insert(END,result) # result dekhabe

                else:
                    pass  # condition sara onno kono voice sunle pass korbe


        except:
            pass



root = Tk()
root.title('Smart Calculator')
root.config(bg='darkseagreen3')
root.geometry('600x486+100+100')

logoImage = PhotoImage(file='logo1.png')
logoLabel = Label(root, image=logoImage, bg='darkseagreen3')
logoLabel.grid(row=0, column=0)

entryField = Entry(root, font=('arial', 20, 'bold'), bg='dimgray', fg='white', bd=10, relief=SUNKEN, width=25)
entryField.grid(row=0, column=0, columnspan=8)

micImage = PhotoImage(file='micro.png')
micButton = Button(root, image=micImage, bd=0, bg='darkseagreen3', activebackground='black'
                   ,command=audio)
micButton.grid(row=0, column=5)

button_text_list = ["C", "CE", "%", "+", "π", "cosθ",
                     "1", "2", "3", "-", "2π", "tanθ",
                    "4", "5", "6", "*","log₁₀" , "sinθ",
                     "7", "8", "9", chr(247), "(", ")",
                        "0", ".", "√", chr(8731), "ln", "="]

rowvalue = 1
columnvalue = 0
for i in button_text_list:

    button = Button(root, width=6, height=2, bd=2, relief=SUNKEN, text=i, bg='darkseagreen3', fg='black',
                    font=('arial', 18, 'bold'), activebackground='darkseagreen3', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 5:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
