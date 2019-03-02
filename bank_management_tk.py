import numpy as np
import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

# from matplotlib import pyplot as plt
# from numpy.random import randn


acc = 0


def import_ac():
    global acc
    if (os.path.isfile('accounts.csv')):
        acc = pd.read_csv('accounts.csv')

    else:
        res = messagebox.askyesno('Database does not exist !', 'do you want to install new database')

        if (res):
            acc = pd.DataFrame(np.array([['_', '_', '_', 0]]), columns=['f_name', 'l_name', 'email', 'balence'])
            acc.to_csv('accounts.csv', index=False)
            acc = pd.read_csv('accounts.csv')
            messagebox.showinfo('Status', 'database installed successfully')

        else:
            # exit()  \uncomment this line and import os line if you are compile this program  on pyinstaller
            pass


import_ac()  # importing csv DataFrame  in global 'acc' variable

window = Tk()
window.geometry('800x600')
window.title("Bank Management system -Shubham Badgujar")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Account details')
tab_control.add(tab2, text='Create Account')
tab_control.add(tab3, text='Deposit Amount')
tab_control.add(tab4, text='Withdraw Amount')

# tab 1 start
lbl1 = Label(tab1, text='Get Account details', font=("Arial Bold", 20))
lbl1.grid(row=1, column=1)

l3 = Label(tab1, text="Account No", font=("Arial Bold", 20))

l3.grid(row=8)

c = Entry(tab1, font=("Arial Bold", 30))
c.grid(row=8, column=1)


def getdet():
    if (not (int(c.get()) > 0 and int(c.get()) < acc.index.shape[0])):
        messagebox.showinfo('invalid input', 'Invalid Acount Number')
        return
    fnm = acc.loc[int(c.get())]['f_name']
    lnm = acc.loc[int(c.get())]['l_name']
    eml = acc.loc[int(c.get())]['email']
    amt = acc.loc[int(c.get())]['balence']
    messagebox.showinfo('Account No ' + str(c.get()),
                        '\n\n\tFull Name  : ' + fnm + ' ' + lnm + '\n\n\tEmail : ' + eml + '\n\n\tBalence : ' + str(
                            amt))


Button(tab1, text='Get Details', command=getdet).grid(row=8, column=2, sticky=W, pady=4)

# teb 1 end


###tab 2 start

lbl1 = Label(tab2, text="signup", font=("Arial Bold", 30))
lbl2 = Label(tab2, text="First Name", font=("Arial Bold", 20))
lbl3 = Label(tab2, text="Last Name", font=("Arial Bold", 20))
lbl4 = Label(tab2, text="Email", font=("Arial Bold", 20))

lbl1.grid(row=1, column=1)

lbl2.grid(row=2)
lbl3.grid(row=4)
lbl4.grid(row=6)

e1 = Entry(tab2)
e2 = Entry(tab2)
e3 = Entry(tab2)

e1.grid(row=2, column=2)
e2.grid(row=4, column=2)
e3.grid(row=6, column=2)


def show_entry_fields():
    if ((e1.get() == '') or (e2.get() == '')):
        messagebox.showinfo('invalid input', 'Enter valid details')
        return
    global acc
    x = acc.index.shape[0]
    acc.loc[x] = [e1.get(), e2.get(), e3.get(), 0.0]
    ##    save_ac()
    messagebox.showinfo('Status',
                        'Account created successfully\nPlease Note your account details\n\nName :' + e1.get() + ' ' + e2.get() + '\nEmail :' + e3.get() + '\n\nACCOUNT NO : ' + str(
                            x))


# Button(tab2, text='Quit', command=tab2.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(tab2, text='create Account', command=show_entry_fields).grid(row=7, column=1, sticky=W, pady=4)

###tab 2 end


###tab 3 start


ll1 = Label(tab3, text="Deposit Amount", font=("Arial Bold", 30))
ll2 = Label(tab3, text="Account Number", font=("Arial Bold", 20))
ll3 = Label(tab3, text="Amount", font=("Arial Bold", 20))

ll1.grid(row=1, column=1)
ll2.grid(row=2)
ll3.grid(row=4)

t1 = Entry(tab3)
t2 = Entry(tab3)

t1.grid(row=2, column=2)
t2.grid(row=4, column=2)


def deposite_amt():
    if ((t1.get() == '') or (t2.get() == '')):
        messagebox.showinfo('invalid input', 'Enter valid details')
        return
    ###code for deposite_amt


Button(tab3, text='Deposite', command=deposite_amt).grid(row=7, column=1, sticky=W, pady=4)

###tab 3 end


###tab 4 start
lbl4 = Label(tab4, text='label4')

lbl4.grid(column=0, row=0)

###tab 4 end


tab_control.pack(expand=1, fill='both')

window.mainloop()
# END OF FILE
