import tkinter
from tkinter import *
from tkinter.ttk import *

# import our file
import spacy

import Similarity

model = "en_core_web_sm"
def main():

    # Create main window that is called root
    root = Tk()
    root.geometry("800x600")
    root.configure(background="white")
    # frame that contains elements text,button....
    inputFrame = Frame(root)
    buttonFrame=Frame(root)
    resultFrame=Frame(root)
    similarity=Similarity.SimilarityClass()

    # this function will get text from both input and do calculation for us
    def chnageModel(value):
        print(value)
        global model
        model =value
    def run_check_function():
        text1 = input1.get(1.0, "end-1c")
        text2 = input2.get(1.0, "end-1c")
        #returns Model for result
        resultModel = similarity.run(text1,text2,model)
        #create lables
        label_result = Label(resultFrame, text='Results:')
        label_length1 = Label(resultFrame, text='input 1 length:'+str(resultModel.length1))
        label_length2 = Label(resultFrame, text='input 2 length:' + str(resultModel.length2))
        label_similarity=Label(resultFrame, text='similarity :' + str(resultModel.similarity))
        label_model = Label(resultFrame, text='Model :' + str(resultModel.model))

        label_result.grid(row=0, column=0)
        label_length1.grid(row=1, column=0)
        label_length2.grid(row=2, column=0)
        label_similarity.grid(row=3, column=0)
        label_model.grid(row=4, column=0)

    # padx from x size opposite would be ipadx
    inputFrame.grid(row=0, column=0, padx=50, pady=50)

    #to display result data
    resultFrame.grid(row=2, column=0, padx=50, pady=0)
    # display first input
    label_input1 = Label(inputFrame, text='input 1')
    label_input1.grid(row=0, column=0)
    input1 = Text(inputFrame, highlightbackground='grey',
                  highlightthickness=1, height=9, width=30,
                  font=25, bg="silver", fg="black")
    input1.config(wrap=WORD)
    input1.grid(row=1, column=0)
    # display second input
    label_input2 = Label(inputFrame, text='input 2')
    label_input2.grid(row=0, column=2)

    input2 = Text(inputFrame, highlightbackground='grey',
                  highlightthickness=1, height=9, width=30,
                  font=25, bg="silver", fg="black")
    input2.grid(row=1, column=2)
    # as Button clicked it will start to count number of words, similarity in percentage
    buttonFrame.grid(row=1, column=0)
    check_button = Button(buttonFrame, text="Run", command=run_check_function)
    check_button.grid(row=0, column=1)

    #we will be having correct and wrong button to give feedback to program
    #and it will be saving to its corpus to next time give better result.
    #if the user clicks Correct that means the program found correct and it will save both sentences
   # to database and give the label accordingly

    #--
    # input 1= Hello, Input2=Hello
    # the similarity is high so it means app says it is same then if we want
    # to save this to corpus we will click Correct.
    # in corpus Hello, Hello,1 will be saved paramters are
    # respectively input1,input2,label
    # if we click Wrong the value will be saved is
    # Hello,Hello,0 that is why we have to teach correctly, other wise it may learn wrong.--#

    sm_button = Button(buttonFrame, text="en_core_web_sm", command=lambda :chnageModel("en_core_web_sm"))
    sm_button.grid(row=1, column=0)
    md_button = Button(buttonFrame, text="en_core_web_md", command=lambda :chnageModel("en_core_web_md"))
    md_button.grid(row=1, column=1)
    lg_button = Button(buttonFrame, text="en_core_web_lg", command=lambda :chnageModel("en_core_web_lg"))
    lg_button.grid(row=1, column=2)
    # keep display Tk window which is  main window
    root.mainloop()
if __name__ == '__main__':
    main()
