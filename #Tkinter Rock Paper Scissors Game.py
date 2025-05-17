#Tkinter Rock Paper Scissors Game
import tkinter as tk
import random

def play(player_choice):
    choices=["rock","paper","scissors"]
    computer_choice=random.choice(choices)

    player_label.config(text=f"Your Choice: {player_choice}")
    computer_label.config(text=f"Computer Choice: {computer_choice}")

    if player_choice==computer_choice:
        result_label.config(text="It's A Tie !!")
    elif (player_choice=='rock' and computer_choice=='scissors') or (player_choice=='paper' and computer_choice=='rock') or (player_choice=='scissors' and computer_choice=='paper'):
        result_label.config(text="You Win!!")
    else:
        result_label.config(text="You Loose!! Better Luck Next Time!!")

window=tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("350x300")
window.resizable(False,False)

title_label=tk.Label(window,text="Rock Paper And Scissors Game", font=("arial",16,"bold"))
title_label.pack(pady=10)

player_label=tk.Label(window,text="Your Choice",font=("arial",12))
player_label.pack()

computer_label=tk.Label(window,text="Computer Choice", font=("arial",12))
computer_label.pack()

result_label=tk.Label(window,text="",font=("arial",14),fg="blue")
result_label.pack(pady=20)

button_frame=tk.Frame(window)
button_frame.pack(pady=20)

rock_btn=tk.Button(button_frame,text="Rock",width=10,command=lambda:play("rock"))
rock_btn.grid(row=0,column=0,padx=5)

paper_btn=tk.Button(button_frame,text="Paper",width=10,command=lambda:play("paper"))
paper_btn.grid(row=0,column=1,padx=5)

scissor_btn=tk.Button(button_frame,text="Scissors",width=10,command=lambda:play("scissors"))
scissor_btn.grid(row=0,column=2,padx=5)

window.mainloop()
