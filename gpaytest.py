#importing tkinter package
from tkinter import *
#declaring global variables
limit=0
balance=0
sum=0
#creating a GUI page
root = Tk()
root.geometry("400x400")
root.title("LIMITATION OF PAYMENTS")
bg=PhotoImage(file="background.png")
labelbg=Label(root,image=bg)
labelbg.place(x=0,y=0,relwidth=1,relheight=1)
#code for the setting limit
def limitfunc():
    t1=Tk()
    t1.geometry("400x400")
    t1.title("Limit setting")
    mylabel = Label(t1, text="Enter the amount you want to set limit for:",font=("Courier",11))
    mylabel.place(x=10,y=100)
    # Taking input from the usee for maximum limit
    e = Entry(t1)
    e.place(x=130,y=130)

    def limitset():
        global limit,sum
        sum=0
        limit = int(e.get())
        label2 = Label(t1, text="Limit set to: " + str(limit),font=("Courier",11))
        label2.place(x=110,y=200)
        t1.after(3000,lambda:t1.destroy())

    button1 = Button(t1, text="Enter",font=("Courier",11), command=limitset)
    button1.place(x=170,y=160)
    t1.mainloop()
limitbutton=Button(root,text="SET LIMIT",command=limitfunc,width=10,font=("Courier",20))
limitbutton.place(x=110,y=100)
def addfunc():
    t2=Tk()
    t2.geometry("400x400")
    t2.title("Add Amount")
    #adding balance to account
    label3 = Label(t2, text="Enter the amount you want to deposit :",font=("Courier",11))
    label3.place(x=10,y=100)
    #taking user entery
    x = Entry(t2)
    x.place(x=130,y=130)

    def addamt():
        global balance
        balance = balance + int(x.get())
        #printing balance
        label4 = Label(t2, text="Balance: " + str(balance),font=("Courier",11))
        label4.place(x=110,y=200)
        t2.after(3000, lambda: t2.destroy())

    button2 = Button(t2, text="Enter", command=addamt)
    button2.place(x=170,y=160)
addbutton=Button(root,text="DEPOSIT",command=addfunc,width=10,font=("Courier",20))
addbutton.place(x=110,y=160)
def withdrawfunc():
    t3=Tk()
    t3.geometry("400x400")
    label5=Label(t3,text="Enter the amount you want to withdraw:",font=("Courier",11))
    label5.place(x=30,y=100)
    a=Entry(t3)
    a.place(x=130,y=130)
    prevsum=0
    def withdrawamt():
        global sum,balance
        #adding input to sum to check with limit
        prevsum=sum
        sum = sum + int(a.get())
        if sum >= limit or limit<int(a.get()):
            #if user exceeds limit
            sum=prevsum
            z="You exceeded the limit"
        elif int(a.get()) > balance:
            z="Greater than current balance"
        else:
            # the else case where user still has amount to spent
            balance=balance-int(a.get())
            z="Remaining balance is: "+ str(balance)
        inslabel=Label(t3,text=z,font=("Courier",11))
        inslabel.place(x=90,y=200)
        t3.after(3000, lambda: t3.destroy())

    enter2=Button(t3,text="enter",font=("Courier",11),command=withdrawamt)
    enter2.place(x=170,y=160)
withdraw= Button(root,text="WITHDRAW",command=withdrawfunc,width=10,font=("Courier",20))
withdraw.place(x=110,y=220)



root.mainloop()