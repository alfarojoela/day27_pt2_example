from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")

window.minsize(width=500, height = 300)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
#button.pack()  #if pack method not used button will not appear in window when program is run
button.grid(row=1, column=1)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(row=2, column=3)

#New Button
new_button = Button(text="New Button to Click", command=button_clicked)
new_button.grid(row=0, column=2)

#pack places widgets.  places at top and then adds entries below.  lacks precision
#place has better precision uses x and y coordinates.
#grid layout is columns and rows.  relative to other components.






window.mainloop()
