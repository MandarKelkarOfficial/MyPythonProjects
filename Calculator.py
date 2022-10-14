#CREATING A CALCULATOR USING TKINTER MODULE  by MANDAR:
from tkinter import*

#creating a main window
root=Tk()
root.geometry("250x400")
root.minsize(250,400)
root.title("Calculator by MK")
root.configure(background="beige")
frame=Frame(root)
frame.pack()

#Creating a function

num1=StringVar()
operator=""

def clickbut(number): #lamda:clickbut(1)
    global operator
    operator=operator+str(number)
    num1.set(operator)
    
def clear():  #To clear the String
    global operator
    operator=""
    num1.set("")
    
def opbut():  #For output
    global operator
    op=str(eval(operator))
    num1.set(op)
    operator=""

#Frame for entry

topframe=Frame(root)
topframe.pack(side=TOP)
textdisplay=Entry(frame,textvariable=num1,bd=20,insertwidth=1,font=30,bg="powder blue").pack(side=TOP)

b1=Button(topframe,padx=16,pady=16,bd=8,text="(",fg="black",bg="powder blue",command=lambda:clickbut("("))
b1.pack(side=LEFT)
b2=Button(topframe,padx=16,pady=16,bd=8,text=")",fg="black",bg="powder blue",command=lambda:clickbut(")"))
b2.pack(side=LEFT)
b3=Button(topframe,padx=16,pady=16,bd=8,text="C",fg="black",bg="powder blue",command=lambda:clear())
b3.pack(side=LEFT)
b4=Button(topframe,padx=16,pady=16,bd=8,text="AC",fg="black",bg="powder blue",command=lambda:clear())
b4.pack(side=LEFT)

#Creating second frame

frame1=Frame(root)
frame1.pack(side=TOP)

b5=Button(frame1,padx=16,pady=16,bd=8,text="7",fg="black",bg="powder blue",command=lambda:clickbut("7"))
b5.pack(side=LEFT)
b6=Button(frame1,padx=16,pady=16,bd=8,text="8",fg="black",bg="powder blue",command=lambda:clickbut("8"))
b6.pack(side=LEFT)
b7=Button(frame1,padx=16,pady=16,bd=8,text="9",fg="black",bg="powder blue",command=lambda:clickbut("9"))
b7.pack(side=LEFT)
b8=Button(frame1,padx=16,pady=16,bd=8,text="/",fg="black",bg="powder blue",command=lambda:clickbut("/"))
b8.pack(side=LEFT)

#Creating a third frame

frame2=Frame(root)
frame2.pack(side= TOP)

b9=Button(frame2,padx=16,pady=16,bd=8,text="4",fg="black",bg="powder blue",command=lambda:clickbut("4"))
b9.pack(side=LEFT)
b10=Button(frame2,padx=16,pady=16,bd=8,text="5",fg="black",bg="powder blue",command=lambda:clickbut("5"))
b10.pack(side=LEFT)
b11=Button(frame2,padx=16,pady=16,bd=8,text="6",fg="black",bg="powder blue",command=lambda:clickbut("6"))
b11.pack(side=LEFT)
b12=Button(frame2,padx=16,pady=16,bd=8,text="*",fg="black",bg="powder blue",command=lambda:clickbut("*"))
b12.pack(side=LEFT)

#Creating fourth frame
frame3=Frame(root)
frame3.pack(side=TOP)

b13=Button(frame3,padx=16,pady=16,bd=8,text="1",fg="black",bg="powder blue",command=lambda:clickbut("1"))
b13.pack(side=LEFT)
b14=Button(frame3,padx=16,pady=16,bd=8,text="2",fg="black",bg="powder blue",command=lambda:clickbut("2"))
b14.pack(side=LEFT)
b15=Button(frame3,padx=16,pady=16,bd=8,text="3",fg="black",bg="powder blue",command=lambda:clickbut("3"))
b15.pack(side=LEFT)
b16=Button(frame3,padx=16,pady=16,bd=8,text="-",fg="black",bg="powder blue",command=lambda:clickbut("-"))
b16.pack(side=LEFT)

#Creating fifth frame

frame4=Frame(root)
frame4.pack(side=TOP)

b17=Button(frame4,padx=16,pady=16,bd=8,text="0",fg="black",bg="powder blue",command=lambda:clickbut("0"))
b17.pack(side=LEFT)
b18=Button(frame4,padx=16,pady=16,bd=8,text=".",fg="black",bg="powder blue",command=lambda:clickbut("."))
b18.pack(side=LEFT)
b19=Button(frame4,padx=16,pady=16,bd=8,text="=",fg="black",bg="powder blue",command=lambda:opbut())
b19.pack(side=LEFT)
b20=Button(frame4,padx=16,pady=16,bd=8,text="+",fg="black",bg="powder blue",command=lambda:clickbut("+"))
b20.pack(side=LEFT)

root.mainloop()