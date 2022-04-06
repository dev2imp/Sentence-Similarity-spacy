import tkinter
from tkinter import *
from tkinter.ttk import *

# import our file
import Similarity
def main():
    # this function will get text from both input and do calculation for us
    def run_check_function():
        text1 = input1.get(1.0, "end-1c")
        text2 = input2.get(1.0, "end-1c")
        Similarity.SimilarityClass(text1, text2)
        print(Similarity.SimilarityClass.length1)
        print(Similarity.SimilarityClass.length2)

    # Create main window that is called root
    root = Tk()
    root.geometry("800x600")
    root.configure(background="white")
    # frame that contains elements text,button....
    frame1 = Frame(root)
    # padx from x size opposite would be ipadx
    frame1.grid(row=0, column=0, padx=50, pady=50)
    # display first input
    label1 = Label(frame1, text='input 1')
    label1.grid(row=0, column=0)
    input1 = Text(frame1, highlightbackground='grey',
                  highlightthickness=1, height=9, width=30,
                  font=25, bg="silver", fg="black")
    input1.config(wrap=WORD)
    input1.grid(row=1, column=0)
    # display second input
    label2 = Label(frame1, text='input 2')
    label2.grid(row=0, column=2)

    input2 = Text(frame1, highlightbackground='grey',
                  highlightthickness=1, height=9, width=30,
                  font=25, bg="silver", fg="black")
    input2.grid(row=1, column=2)
    # as Button clicked it will start to count number of words, similarity in percentage
    check_button = Button(frame1, text="Check", command=run_check_function)
    check_button.grid(row=2, column=1)

    # keep display Tk which is  main window
    root.mainloop()


if __name__ == '__main__':
    main()
