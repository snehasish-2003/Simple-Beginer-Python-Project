#Tkinter Wikipedia Search
import tkinter as tk
import wikipedia
from tkinter import messagebox

def seacrh_wikipedia():
    query=entry.get()
    try:
        summary=wikipedia.summary(query, sentences=10)
        text_area.delete("1.0",tk.END)
        text_area.insert(tk.END,summary)
    except wikipedia.exceptions.DisambiguationError as e:
        messagebox.showerror("Disambguitor Error",f"Multiple Results Found {e.options[:5]}")
    except wikipedia.exceptions.PageError:
        messagebox.showerror("Page Error","Page Not Found!!")
    except Exception as e:
        messagebox.showerror("Error",str(e))

window=tk.Tk()
window.title("Wiki Peaky Search")
window.geometry("400x400")
window.resizable(False,False)

tk.Label(window,text="WIKIPEDIA SEARCH",font=('Hellvetica',18,'bold')).pack(pady=10)

entry=tk.Entry(window,font=('Hellvetica',16),width=40)
entry.pack(pady=10)

tk.Button(window,text='SEARCH',command=seacrh_wikipedia,font=('Hellvetica',14)).pack(pady=5)

text_area=tk.Text(window,wrap=tk.WORD,font=('Hellvetica',12))
text_area.pack(padx=10,pady=10,expand=True,fill=tk.BOTH)

window.mainloop()