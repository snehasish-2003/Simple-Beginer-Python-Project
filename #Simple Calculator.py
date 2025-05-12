#Simple Calculator 
from tkinter import *

window=Tk()
window.title('Simple Calculator')
window.geometry("312x324") #Size Of The Window
window.resizable(0,0) #Prevent from Maximize

#btn_click = continiously update the input field whenever you enters a number 
def btn_click(item):
    global expression
    expression= expression + str(item)
    input_text.set(expression)

#Btn_clear = To Clear The Input Field :-)
def btn_clear():
    global expression
    expression=""
    input_text.set(expression)

#btn_equal = For Result
def btn_equal():
    global expression
    result=str(eval(expression)) #eval is used to Evaluate the string Function :-)
    input_text.set(result)
    expression=""

expression=""
input_text=StringVar() #StringVar() is Used for get the Instace of the Input Field

#Creating A Frame for input field
input_frame=Frame(window,width=312,height=50,highlightbackground="black",highlightcolor="black",highlightthickness=2)
input_frame.pack(side=TOP)

#Creating a input field in the Frame
input_field=Entry(input_frame,font=('arial',18,'bold'),textvariable=input_text,width=50,background="#eee",border=0,justify="center")
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

#Creating Another Frame For The Buttons Below
btn_frame=Frame(window,width=312,height=272.5,background="grey")
btn_frame.pack()

#First Row
clear=Button(btn_frame,text="C",fg="black",bg="#eee",width=32,height=3,bd=0,cursor="hand2",command=lambda:btn_clear())

divide=Button(btn_frame,text="/",fg="black",bg="#eee",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("/"))


#Second Row
seven=Button(btn_frame,text="7",fg="black",bg="#fff",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("7"))

eight=Button(btn_frame,text="8",fg="black",bg="#fff",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("8"))

nine=Button(btn_frame,text="9",fg="black",bg="#fff",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("9"))

multiply=Button(btn_frame,text="*",fg="black",bg="#eee",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("*"))


#Third Row
four=Button(btn_frame,text="4",fg="black",bg="#fff",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("4"))

five=Button(btn_frame,text="5",fg="black",bg="#fff",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("5"))

six=Button(btn_frame,text="6",fg="black",bg="#fff",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("6"))

minus=Button(btn_frame,text="-",fg="black",bg="#eee",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("-"))

#Fourth Row
one=Button(btn_frame,text="1",fg="black",bg="#fff",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("1"))

two=Button(btn_frame,text="2",fg="black",bg="#fff",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("2"))

three=Button(btn_frame,text="3",fg="black",bg="#fff",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("3"))

addition=Button(btn_frame,text="+",fg="black",bg="#eee",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("+"))

#Fifth Row
zero=Button(btn_frame,text="0",fg="black",bg="#fff",width=21,height=3,bd=0,cursor="hand2",command=lambda:btn_click("0"))

point=Button(btn_frame,text=".",fg="black",bg="#fff",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_click("."))

equal=Button(btn_frame,text="=",fg="black",bg="#eee",width=10,height=3,bd=0,cursor="hand2",command=lambda:btn_equal())


clear.grid(row=0, column=0, columnspan=3)
divide.grid(row=0, column=3)

seven.grid(row=1, column=0)
eight.grid(row=1, column=1)
nine.grid(row=1, column=2)
multiply.grid(row=1, column=3)

four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
minus.grid(row=2, column=3)

one.grid(row=3, column=0)
two.grid(row=3, column=1)
three.grid(row=3, column=2)
addition.grid(row=3, column=3)

zero.grid(row=4, column=0, columnspan=2)
point.grid(row=4, column=2)
equal.grid(row=4, column=3)

window.mainloop()





