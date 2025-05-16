from tkinter import *
import math
window=Tk()
window.title("Simple Calculator")
window.geometry("312x324")
window.resizable(1,1)

def btn_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression=""
    input_text.set(expression)

def btn_equal():
    global expression
    try:
        allowed_names = math.__dict__.copy()
        allowed_names["log"] = math.log
        allowed_names["log10"] = math.log10
        result = str(eval(expression, {"__builtins__": None}, allowed_names))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""


expression=""
input_text=StringVar()

input_frame=Frame(window,width=312,height=50,highlightbackground="black",highlightcolor="black",highlightthickness=2)
input_frame.pack(side=TOP)

input_field=Entry(input_frame,font=('arial',18,'bold'),width=50,background="#eee",textvariable=input_text,border=2,justify="right")
input_field.pack(ipady=10)


btn_frame=Frame(window,width=312,height=272.5,background="grey")
btn_frame.pack()

clear=Button(btn_frame,text="C",width=21,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_clear())
division=Button(btn_frame,text="/",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("/"))
log=Button(btn_frame,text="log",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("log("))

seven=Button(btn_frame,text="7",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("7"))
eight=Button(btn_frame,text="8",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("8"))
nine=Button(btn_frame,text="9",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("9"))
multiply=Button(btn_frame,text="*",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("*"))

four=Button(btn_frame,text="4",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("4"))
five=Button(btn_frame,text="5",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("5"))
six=Button(btn_frame,text="6",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("6"))
minus=Button(btn_frame,text="-",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("-"))

one=Button(btn_frame,text="1",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("1"))
two=Button(btn_frame,text="2",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("2"))
three=Button(btn_frame,text="3",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("3"))
plus=Button(btn_frame,text="+",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("+"))

zero=Button(btn_frame,text="0",width=21,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("0"))
point=Button(btn_frame,text=".",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_click("."))
equal=Button(btn_frame,text="=",width=10,height=3,fg="black",bg="#eee",bd=0,cursor="hand2",command=lambda:btn_equal())

log10_btn = Button(btn_frame, text="log10", width=21, height=3, fg="black", bg="#eee", bd=0, cursor="hand2", command=lambda: btn_click("log10("))
log10_btn.grid(row=5, column=0, columnspan=2)
rparen = Button(btn_frame, text=")", width=10, height=3, fg="black", bg="#eee", bd=0, cursor="hand2", command=lambda: btn_click(")"))
rparen.grid(row=5, column=2)

# Empty button to fill grid
empty = Button(btn_frame, text="", width=10, height=3, bg="grey", state=DISABLED, relief=FLAT, bd=0)
empty.grid(row=5, column=3)

clear.grid(row=0, column=0, columnspan=2)
division.grid(row=0, column=2)
log.grid(row=0, column=3)

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
plus.grid(row=3, column=3)

zero.grid(row=4, column=0, columnspan=2)
point.grid(row=4, column=2)
equal.grid(row=4, column=3)

window.mainloop()





