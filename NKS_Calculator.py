import tkinter as t
window = t.Tk()
#model
first_val=t.IntVar()
second_val=t.IntVar()
result=t.IntVar()
first_val.set(0)
second_val.set(0)
result.set(0)
#control
def add():
    result.set(first_val.get()+second_val.get())
    print("Addition of ",first_val.get(),second_val.get(),"is = ",result.get(),file=open("calculator.txt",'a'))
def sub():
    result.set(first_val.get()-second_val.get())
    #print(" subtraction is ", first_val(), second_val(),"= ",result.get(), file=open("calculator.txt", 'a'))
    print("Subtraction of ", first_val.get(), second_val.get(), "is = ", result.get(), file=open("calculator.txt", 'a'))
def multi():
    result.set(first_val.get()*second_val.get())
    #print(" multiplication is ", first_val(), second_val(),"= ",result.get(), file=open("calculator.txt", 'a'))
    print("Multiplication of ", first_val.get(), second_val.get(), "is = ", result.get(), file=open("calculator.txt", 'a'))
def div():
    if second_val.get()>0:
        result.set(first_val.get()/second_val.get())
        #print(" div is ", first_val(), second_val(),"= ",result.get(), file=open("calculator.txt", 'a'))
        print("Div. of ", first_val.get(), second_val.get(), "is = ", result.get(),
              file=open("calculator.txt", 'a'))
    else:
        result.set('Error')
def power():
    if second_val.get() < 100:
        result.set(first_val.get()**second_val.get())
        #print(" addition is ", first_val(), second_val(),"= ",result.get(), file=open("calculator.txt", 'a'))
        print("power of ", first_val.get(), second_val.get(), "is = ", result.get(),
              file=open("calculator.txt", 'a'))
    else:
        result.set('Enter below 100 in second window')
def clear():
    first_val.set(0)
    second_val.set(0)
    result.set(0)
#View
window.title("Calculator")
frame=t.Frame(window,borderwidth=15,relief=t.GROOVE,bg='#10686b')
frame.pack()
#first value
entry1=t.Entry(frame,borderwidth=15,font=('Comic Sans MS',30,'bold'),relief=t.GROOVE,bg='white',textvariable=first_val)
entry1.grid(row=0,column=2)
#second value
entry2=t.Entry(frame,borderwidth=15,font=('Comic Sans MS',30,'bold'),relief=t.GROOVE,bg='white',textvariable=second_val)
entry2.grid(row=1,column=2)
#making botton add
button1=t.Button(frame,borderwidth=8,text="add",font=('Comic Sans MS',30,'bold'),command = add,bg="#001254",fg="green")
button1.grid(row=0,column=3)
#making botton sub
button1=t.Button(frame,borderwidth=8,text="sub",font=('Comic Sans MS',30,'bold'),command = sub,bg="#001254",fg="green")
button1.grid(row=0,column=4)
#making botton multi
button1=t.Button(frame,borderwidth=8,text="multi",font=('Comic Sans MS',30,'bold'),command = multi,bg="#001254",fg="green")
button1.grid(row=0,column=5)
#making botton div
button1=t.Button(frame,borderwidth=8,text="div",font=('Comic Sans MS',30,'bold'),command = div,bg="#001254",fg="green")
button1.grid(row=1,column=3)
#making botton power
button1=t.Button(frame,borderwidth=8,text="power",font=('Comic Sans MS',30,'bold'),command = power,bg="#001254",fg="green")
button1.grid(row=1,column=4)
#making botton clear
button1=t.Button(frame,borderwidth=8,text="clear",font=('Comic Sans MS',30,'bold'),command = clear,bg="#001254",fg="green")
button1.grid(row=1,column=5)
#label
label=t.Label(window,borderwidth=8,font=('Comic Sans MS',45,'bold'),textvariable=result,bg="white",fg="black")
#label.grid(row=4,column=0)
label.pack()
window.mainloop()


