import tkinter
from tkinter import *
from tkinter.ttk import *

# import our file
import Similarity

def main():
    # Create main window that is called root
    root = Tk()
    root.geometry("800x600")
    root.configure(background="white")
    # frame that contains elements text,button....
    frame1 = Frame(root)
    frame2=Frame(root)
    similarity=Similarity.SimilarityClass()

    # this function will get text from both input and do calculation for us
    def run_check_function():
        text1 = input1.get(1.0, "end-1c")
        text2 = input2.get(1.0, "end-1c")
        #returns Model for result
        resultModel = similarity.run(text1,text2)

        #create lables
        label_result = Label(frame2, text='Results:')
        label_length1 = Label(frame2, text='input 1 length:'+str(resultModel.length1))
        label_length2 = Label(frame2, text='input 2 length:' + str(resultModel.length2))
        label_similarity=Label(frame2, text='similarity :' + str(resultModel.similarity))

        label_result.grid(row=0, column=0)
        label_length1.grid(row=1, column=0)
        label_length2.grid(row=2, column=0)
        label_similarity.grid(row=3, column=0)

    # padx from x size opposite would be ipadx
    frame1.grid(row=0, column=0, padx=50, pady=50)
    #to display result data
    frame2.grid(row=1, column=0, padx=50, pady=0)
    # display first input
    label_input1 = Label(frame1, text='input 1')
    label_input1.grid(row=0, column=0)
    input1 = Text(frame1, highlightbackground='grey',
                  highlightthickness=1, height=9, width=30,
                  font=25, bg="silver", fg="black")
    input1.config(wrap=WORD)
    input1.grid(row=1, column=0)
    # display second input
    label_input2 = Label(frame1, text='input 2')
    label_input2.grid(row=0, column=2)

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
