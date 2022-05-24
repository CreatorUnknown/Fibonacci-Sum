from tkinter import *
root = Tk()

root.title("Fibonacci Series")
root.geometry("400x400")

label = Label(root, text = "How long do you want the fibonacci series?")
text_input = Entry(root)
label1 = Label(root)


def Fibonacci():
    num = int(text_input.get())
    first_no = 0
    second_no = 1
    sum = 0
    sum2 = 0
    counter = 1
    while(counter<= num):
        counter = counter+1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum
    label1["text"] = "Fibonacci sum = " + str(sum2)

btn = Button(root, text = "Show Fibonacci series", command = Fibonacci, bg = "black", fg = "white")
btn.pack()
label.pack();
text_input.pack()
label1.pack()


root.mainloop()