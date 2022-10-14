#Tic-Tac-Toe Game
from tkinter import*
from tkinter import messagebox

#Creating a window
root=Tk()
root.title("Tic-Tac-Toe")
root.geometry("260x340")
root.minsize(260,340)
root.maxsize(260,340)
root.configure(borderwidth=15,background="aqua")

#Function fow "X" and "0"

clicked=True
count=0

def b_click(b):
    global clicked,count
    if b["text"]=="" and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        checkifwon()
        
    elif b["text"]=="" and clicked==False:
        b["text"]="0"
        clicked=True
        count+=1
        checkifwon()
        
    else:
        messagebox.showerror("TicTacToe","Already clicked")

# X Win condition

def checkifwon():
    global winner 
    winner=False
    if  b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("TTT","You Won")
        disable_all_buttons()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
         b4.config(bg="red")
         b5.config(bg="red")
         b6.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 1 Won")
         disable_all_buttons()
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
         b7.config(bg="red")
         b8.config(bg="red")
         b9.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 1 Won")
         disable_all_buttons()
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
         b1.config(bg="red")
         b4.config(bg="red")
         b7.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 1 Won") 
         disable_all_buttons() 
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
         b2.config(bg="red")
         b5.config(bg="red")
         b8.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 1 Won")
         disable_all_buttons()  
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
         b3.config(bg="red")
         b6.config(bg="red")
         b9.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 1 Won")
         disable_all_buttons()
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
         b1.config(bg="red")
         b5.config(bg="red")
         b9.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 1 Won")
         disable_all_buttons()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
         b3.config(bg="red")
         b5.config(bg="red")
         b7.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 1 Won")
         disable_all_buttons()
    
    # 0 win condition
    
    if  b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("TTT","Player 2 Won")
        disable_all_buttons()
    elif b4["text"]=="0" and b5["text"]=="0" and b6["text"]=="0":
         b4.config(bg="red")
         b5.config(bg="red")
         b6.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 2 Won")
         disable_all_buttons()
    elif b7["text"]=="0" and b8["text"]=="0" and b9["text"]=="0":
         b7.config(bg="red")
         b8.config(bg="red")
         b9.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 2 Won")
         disable_all_buttons()
    elif b1["text"]=="0" and b4["text"]=="0" and b7["text"]=="0":
         b1.config(bg="red")
         b4.config(bg="red")
         b7.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 2 Won")
         disable_all_buttons()  
    elif b2["text"]=="0" and b5["text"]=="0" and b8["text"]=="0":
         b2.config(bg="red")
         b5.config(bg="red")
         b8.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 2 Won")
         disable_all_buttons()  
    elif b3["text"]=="0" and b6["text"]=="0" and b9["text"]=="0":
         b3.config(bg="red")
         b6.config(bg="red")
         b9.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 2 Won")
         disable_all_buttons()
    elif b1["text"]=="0" and b5["text"]=="0" and b9["text"]=="0":
         b1.config(bg="red")
         b5.config(bg="red")
         b9.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 2 Won")
         disable_all_buttons()
    elif b3["text"]=="0" and b5["text"]=="0" and b7["text"]=="0":
         b3.config(bg="red")
         b5.config(bg="red")
         b7.config(bg="red")
         winner=True
         messagebox.showinfo("TTT","Player 2 Won")
         disable_all_buttons()
         
     #Tie condition
     
    if winner==False and count==9:
          messagebox.showinfo("TTT","It's a tie")
        

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    
    
#Reset function

          
         
         
    
#creating buttons

b1=Button(root,text="",foreground="dark red",background="#9400D3",activebackground="#FF1493",font="arial",height=3,width=6,command=lambda:b_click(b1))
b2=Button(root,text="",foreground="dark red",background="#9400D3",activebackground="#FF1493",font="arial",height=3,width=6,command=lambda:b_click(b2))
b3=Button(root,text="",foreground="dark red",background="#9400D3",activebackground="#FF1493",font="arial",height=3,width=6,command=lambda:b_click(b3))
b4=Button(root,text="",foreground="dark red",background="#9400D3",activebackground="#FF1493",font="arial",height=3,width=6,command=lambda:b_click(b4))
b5=Button(root,text="",foreground="dark red",background="#9400D3",activebackground="#FF1493",font="arial",height=3,width=6,command=lambda:b_click(b5))
b6=Button(root,text="",foreground="dark red",background="#9400D3",activebackground="#FF1493",font="arial",height=3,width=6,command=lambda:b_click(b6))
b7=Button(root,text="",foreground="dark red",background="#9400D3",activebackground="#FF1493",font="arial",height=3,width=6,command=lambda:b_click(b7))
b8=Button(root,text="",foreground="dark red",background="#9400D3",activebackground="#FF1493",font="arial",height=3,width=6,command=lambda:b_click(b8))
b9=Button(root,text="",foreground="dark red",background="#9400D3",activebackground="#FF1493",font="arial",height=3,width=6,command=lambda:b_click(b9))

#Placing the buttons on screen

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

#clear button

b10=Button(root,text="QUIT",activebackground="red",background="beige",foreground="black",command=lambda:root.quit()).place(x=95,y=280)


root.mainloop()