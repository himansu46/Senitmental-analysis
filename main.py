
import tkinter as tk

# Function for clearing the
# contents of all entry boxes
# And label area.
def clearAll() :
    stringclr = ''
    string1.set(stringclr)
    label2 = tk.Label(positiveframe, text='')
    label2.place(relwidth=1, relheight=1)
    label3 = tk.Label(negativeframe, text='')
    label3.place(relwidth=1, relheight=1)
    label4 = tk.Label(overallframe, text='')
    label4.place(relwidth=1, relheight=1)

def sent_analysis():
    global sentence
    sentence = string1.get()
    listing = sentence.split()

    """ file handling """
    import os, sys
    fname1 = 'neutral.txt'
    fname2 = 'positive.txt'
    fname3 = 'negative.txt'
    if os.path.isfile(fname1):
        f1 = open(fname1,'r')
    else:
        print(fname1 + ' does not exist')
        sys.exit()
    if os.path.isfile(fname2):
        f2 = open(fname2,'r')
    else:
        print(fname2 + ' does not exist')
        sys.exit()
    if os.path.isfile(fname3):
        f3 = open(fname3,'r')
    else:
        print(fname3 + ' does not exist')
        sys.exit()

    pst=ngt=ntr=0    # initialise counters
    for word in listing:
        word1 = word.lower()
        f1.seek(0)
        f2.seek(0)
        f3.seek(0)
        ntr=0
        for word_neutral in f1:
            if word1 in word_neutral:
                ntr = 1
                break
        if(ntr>0):
            continue
        else:
            flag = 0
            for word_positive in f2:     # read one line at a time from file
                if word1 in word_positive:
                    pst=pst+1
                    flag = 1
                else: continue
            if(flag == 0):
                for word_negative in f3:     # read one line at a time from file
                    if word1 in word_negative:
                        ngt=ngt+1
                    else: continue

    f1.close()
    f2.close()
    f3.close()

    if(pst+ngt == 0):
        label4 = tk.Label(overallframe, text='⭐',fg='#2C2891',font=(12))
        label4.place(relwidth=1, relheight=1)
        display(0,0)

    else:

        p_percent = round((pst/(pst+ngt) * 100),2)
        n_percent = round((ngt/(pst+ngt) * 100),2)

        display(p_percent,n_percent)

        if((p_percent-n_percent)>80):
            label4 = tk.Label(overallframe, text='⭐⭐⭐⭐⭐',fg='#49FF00',font=(12))
            label4.place(relwidth=1, relheight=1)

        elif((p_percent-n_percent)>60):
            label4 = tk.Label(overallframe, text='⭐⭐⭐⭐',font=(12),fg='#49FF00')
            label4.place(relwidth=1, relheight=1)
        elif((p_percent-n_percent)>40):
            label4 = tk.Label(overallframe, text='⭐⭐⭐',font=(12),fg='#49FF00')
            label4.place(relwidth=1, relheight=1)
        elif((p_percent-n_percent)>20):
            label4 = tk.Label(overallframe, text='⭐⭐',font=(12),fg='#49FF00')
            label4.place(relwidth=1, relheight=1)
        else:
            label4 = tk.Label(overallframe, text='⭐',fg='#FF5403',font=(12))
            label4.place(relwidth=1, relheight=1)

def display(p_percent,n_percent):
        label2 = tk.Label(positiveframe, text=str(p_percent)+' %',font=(10))
        label2.place(relwidth=1, relheight=1)
        label3 = tk.Label(negativeframe, text=str(n_percent)+' %',font=(10))
        label3.place(relwidth=1, relheight=1)



root = tk.Tk()
root.title('Movie Review Sentiment')
root.geometry('600x500')

bgimage = tk.PhotoImage(file='photo.png')
bglabel = tk.Label(root, image=bgimage)
bglabel.place(relwidth=1, relheight=1)

label= tk.Label(bglabel,text='Movie Review Sentiment',fg='#79018C',font=("Courier", 15))
label.pack()

string1 = tk.StringVar()


inputframe = tk.Frame(root ,bg='#80c1ff', bd=5)
inputframe.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

label_entry = tk.Label(inputframe,text='Enter text here',font=("Courier", 9))
label_entry.place(relx=0.015,rely=0.1)
entry = tk.Entry(inputframe, font=60, textvariable=string1)
entry.place(relx=0.01,rely=0.3,relwidth=0.65, relheight=0.8)


button = tk.Button(inputframe, text="CHECK", font=40,bg='#9AE66E', command = sent_analysis)
button.place(relx=0.68,rely=0.30, relheight=0.35, relwidth=0.3)

clear = tk.Button(inputframe, text = "CLEAR",font=40, fg = "Black",bg = "Red", command = clearAll)
clear.place(relx=0.68,rely=0.70, relheight=0.35, relwidth=0.3)

resultframe = tk.Frame(root, bg='#80c1ff', bd=10 )
resultframe.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.65, anchor='n')
label1 = tk.Label(resultframe)
label1.place(relwidth=1, relheight=1)

label2_text= tk.Label(resultframe,text='Positivity %age :',font=("Courier", 12))
label2_text.place(relx=0.01,rely=0.15)

positiveframe = tk.Frame(resultframe, bg='#71DFE7', bd=10 )
positiveframe.place(relx=0.7, rely=0.1, relwidth=0.50, relheight=0.15, anchor='n')
label2 = tk.Label(positiveframe)
label2.place(relx=-0.02,rely=-0.1,relwidth=1.04, relheight=1.21)

label3_text= tk.Label(resultframe,text='Negativity %age :',font=("Courier", 12))
label3_text.place(relx=0.01,rely=0.4)

negativeframe = tk.Frame(resultframe, bg='#71DFE7', bd=10 )
negativeframe.place(relx=0.7, rely=0.35, relwidth=0.50, relheight=0.15, anchor='n')
label3 = tk.Label(negativeframe)
label3.place(relx=-0.02,rely=-0.1,relwidth=1.04, relheight=1.21)

label4_text= tk.Label(resultframe,text='Overall Rating :',font=("Courier", 12))
label4_text.place(relx=0.01,rely=0.7)

overallframe = tk.Frame(resultframe, bg='#71DFE7', bd=10 )
overallframe.place(relx=0.7, rely=0.65, relwidth=0.50, relheight=0.15, anchor='n')
label4 = tk.Label(overallframe)
label4.place(relx=-0.02,rely=-0.1,relwidth=1.04, relheight=1.21)


root.mainloop()
