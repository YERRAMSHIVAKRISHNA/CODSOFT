from tkinter import *
sky=Tk()
sky.geometry("500x500")
Label(sky,text="enter the text",padx=10,font="lucida").grid(row=0,sticky=W)
a=StringVar()

b=[]
def openfile() :
    try:
            with open('file.txt','r') as file:
                tasks=file.readlines()
            for a in tasks:
                if a!='\n':
                    b.append(a)
                    listbox.insert(END,a)
    except:
            file=open('a.txt','w')
            file.close()

def edit(event) :
   a=et.get()
   et.delete(0,END)
   if a :
           with open('file.txt','a') as file:
            file.write(f'\n{a}') 
            b.append(a) 
            listbox.insert(END,a) 
                     
def cut(event) :
    global b
    a=str(listbox.get(ANCHOR))
    if a in b:
        b.remove(a)
        with open('file.txt','w') as file:
            for a in b:
                file.write(a+'\n')
        listbox.delete(ANCHOR)

heading=Label(sky,text="All Tasks",font="lucida 40 bold" )
heading.grid(row=0,column=0)

et=Entry(sky,font="lucida 30 bold")
et.grid(row=0,column=1,ipadx=150,ipady=30)

but=Button(sky,text="add",bg="green",font="lucida" )
but.grid(row=1,column=1,pady=20)

but.bind("<Button-1>",edit)
but=Button(sky,text="Delete",bg="red",font="lucida")

but.grid(row=1,column=0,pady=20)
but.bind("<Button-1>",cut)

listbox=Listbox(sky,font="lucida 30 bold")
listbox.grid(row=2,column=1,pady=200,ipadx=200,ipady=200)
openfile()
sky.mainloop()