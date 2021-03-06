from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Ready to hang? or to win?")
window.geometry("800x700")
chances=4;
image_paths=['hang.jpg','fourth-err.jpg','third-err.jpg','second-err.jpg','first-err.jpg']
img = Image.open(image_paths[chances])
img = img.resize((200, 200), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(window, image = img)
panel.grid(column=0, row=0)

def clicked(letter):
    global chances
    answer= "CODE";
    if letter in answer: #Its checks whether the letter is there in the answer
        if letter=="C":
            btn01["text"] = letter;
        elif letter=="O":
            btn02["text"] = letter;
        elif letter=="D":
            btn03["text"] = letter;
        elif letter=="E":
            btn04["text"] = letter;

    else:
        txt="Chances remaining "+str(chances);
        label1.configure(text=txt)
        image = Image.open(image_paths[chances])
        image = image.resize((200, 200), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        chances = chances - 1;
        if chances<0:
            messagebox.showinfo("Ran out of guesses","Hanged!")
            window.destroy()

    if btn01["text"]=="C" and btn02["text"]=="O" and btn03["text"]=="D" and btn04["text"]=="E":
        messagebox.showinfo("Congratulations", "You won!")
        window.destroy()
    print(chances)



btn01 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn01.grid(column=2, row=0)
btn02 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn02.grid(column=3, row=0)
btn03 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn03.grid(column=4, row=0)
btn04 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn04.grid(column=5, row=0)


btn1 = Button(window, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
btn1.grid(column=1, row=1)
btn2 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
btn2.grid(column=2, row=1)
btn3 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
btn3.grid(column=3, row=1)
btn4 = Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
btn4.grid(column=4, row=1)
btn5 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
btn5.grid(column=5, row=1)
btn6 = Button(window, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
btn6.grid(column=6, row=1)
btn7 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
btn7.grid(column=7, row=1)
btn8 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
btn8.grid(column=8, row=1)

btn9 = Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
btn9.grid(column=2, row=2)
btn10 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
btn10.grid(column=3, row=2)
btn11= Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
btn11.grid(column=4, row=2)
btn12 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
btn12.grid(column=5, row=2)
btn13 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
btn13.grid(column=6, row=2)
btn14 = Button(window, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
btn14.grid(column=7, row=2)

btn15= Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
btn15.grid(column=3, row=3)
btn16 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
btn16.grid(column=4, row=3)
btn17 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
btn17.grid(column=5, row=3)
btn18 = Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
btn18.grid(column=6, row=3)

btn19 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
btn19.grid(column=4, row=4)
btn20 = Button(window, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
btn20.grid(column=5, row=4)

label1=Label(window,text="Total Chances are : 5")
label1.grid(row=5,column=0)
window.mainloop()