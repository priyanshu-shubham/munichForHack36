import tkinter as tk
from tkinter import *
import mysql.connector
import easygui

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hola123",
    database="municipal"
    )

govt = tk.Tk()
govt.title('Choose your department')

l1 = Label(govt , text="Choose your department")
l1.pack()

cats = ["CLEANLINESS" , "TRANSPORT" , "HOUSING","ANIMAL HUSBANDRY","AYURVEDA","COOPERATION","ELECTION","ELEMENTARY EDUCATION","ENVIRONMENT, SCIENCE AND TECHNOLOGY","EXCISE AND TAXATION","FISHERIES","FINANCIAL COMMISSIONER (REVENUE)","FOOD,CIVIL SUPPLIES AND CONSUMER AFFAIRS","FOREST","HEALTH AND FAMILY WELFARE","HIGHER EDUCATION","HORTICULTURE","INDUSTRIES","INFORMATION AND PUBLIC RELATIONS","INFORMATION TECHNOLOGY","IRRIGATION AND PUBLIC HEALTH","LABOUR AND EMPLOYMENT","LANGUAGE AND CULTURE","PANCHAYATI RAJ","POLICE DEPARTMENT","PRINTING AND STATIONERY","PUBLIC WORKS","RURAL DEVELOPMENT","SETTLEMENT","SOCIAL JUSTICE & EMPOWERMENT","TECHNICAL EDUCATION,VOCATIONAL AND INDUSTRIAL TRAINING","TOURISM AND CIVIL AVIATION","TOWN AND COUNTARY PLANNING","TRANSPORT","TRIBAL DEVELOPMENT","YOUTH SERVICES AND SPORTS","URBAN DEVELOPMENT"]

var = StringVar(govt)
var.set("Choose a category")
catmenu = OptionMenu(govt , var , cats[0] ,cats[1] ,cats[2] ,cats[3] ,cats[4] ,cats[5] ,cats[6] ,cats[7] ,cats[8] ,cats[9] ,cats[10] ,cats[11] ,cats[12] ,cats[13] ,cats[14] ,cats[15] ,cats[16] ,cats[17] ,cats[18] ,cats[19] ,cats[20] ,cats[21] ,cats[22] ,cats[23] ,cats[24] ,cats[25] ,cats[26] ,cats[27] ,cats[28] ,cats[29] ,cats[30] ,cats[31] ,cats[32] ,cats[33] ,cats[34] ,cats[35] ,cats[36] )
catmenu.pack()


def nextbut():
    choice = var.get()
    _lis=[]
    mycursor = mydb.cursor()
    mycursor.execute("select * from Mandi where category=\"{}\"".format(choice))
    for i in mycursor:
        _lis.append(i)
    if len(_lis)==0:
        easygui.msgbox("NO GRIEVANCE RELATED WITH THIS DEPARTMENT FOUND", title="INFORMATION!")
        quit()
    titles=[]
    snos=[]
    titlesi=[]

    catgovt = tk.Tk()
    catgovt.title('Grievances')

    for i in range(len(_lis)):
        sno,category,nm,title,date,complaint,location,status,reply=_lis[i]
        s = StringVar(catgovt)
        s.set(sno)
        snos.append(s)
        titlesi.append(title)

        t = StringVar(catgovt)
        t.set(title)
        titles.append(t)


    options=[]
    def showtkt():
        var=v.get()
        global sno

        tktgovt = tk.Tk()
        tktgovt.title('Ticket Details')

        catgovt.destroy()

        sno,category,nm,title,date,complaint,location,status,reply=_lis[var]
        titlet = tk.StringVar(tktgovt)
        titlet.set(title)
        snot = tk.StringVar(tktgovt)
        snot.set(sno)
        namet = tk.StringVar(tktgovt)
        namet.set(nm)
        complaintt = tk.StringVar(tktgovt)
        complaintt.set(complaint)
        statust = tk.StringVar(tktgovt)
        statust.set(status)
        datet = tk.StringVar(tktgovt)
        datet.set(date)
        locationt = tk.StringVar(tktgovt)
        locationt.set(location)
        replyt = tk.StringVar(tktgovt)
        replyt.set(reply)
        categoryt = tk.StringVar(tktgovt)
        categoryt.set(category)

        frame1 = Frame(tktgovt)
        frame1.pack()

        l1 = Label(frame1 , text = 'Serial No : ')
        l1.grid(row = 0 , column = 0)
        snolabel = Label(frame1 , textvariable= snot)
        snolabel.grid(row = 0 , column = 1)

        l2 = Label(frame1 , text = 'Title : ')
        l2.grid(row = 1 , column = 0)
        titlelabel = Label(frame1 , textvariable = titlet)
        titlelabel.grid(row = 1 , column = 1)

        l3 = Label(frame1 , text = 'Category : ')
        l3.grid(row = 2 , column = 0)
        categorylabel = Label(frame1 , textvariable = categoryt)
        categorylabel.grid(row = 2 , column = 1)

        l4 = Label(frame1 , text = 'Complaint : ')
        l4.grid(row = 3 , column = 0)
        complaintlabel = Label(frame1 , textvariable = complaintt)
        complaintlabel.grid(row = 3 , column = 1)

        l5 = Label(frame1 , text = 'Date : ')
        l5.grid(row = 4 , column = 0)
        datelabel = Label(frame1 , textvariable = datet)
        datelabel.grid(row = 4 , column = 1)

        l6 = Label(frame1 , text = 'Location : ')
        l6.grid(row = 5 , column = 0)
        locationlabel = Label(frame1 , textvariable = locationt)
        locationlabel.grid(row = 5 , column = 1)

        frame2 = Frame(tktgovt)
        frame2.pack()

        l9 = Label(frame2 , text = 'Current Reply : ')
        l9.grid(row = 0 , column = 0)
        replylabel = Label(frame2 , textvariable = replyt)
        replylabel.grid(row = 0 , column = 1)

        l7 = Label(frame2 , text = 'Update Reply : ')
        l7.grid(row = 1 , column = 0)
        e1 = Entry(frame2)
        e1.grid(row = 1 , column = 1)

        l10 = Label(frame2 , text = 'Current Status : ')
        l10.grid(row = 2 , column = 0)
        statuslabel = Label(frame2 , textvariable = statust)
        statuslabel.grid(row = 2 , column = 1)

        l8 = Label(frame2 , text = 'Update Status : ')
        l8.grid(row = 3 , column = 0)
        e2 = Entry(frame2)
        e2.grid(row = 3 , column = 1)

        def updatevals():
            reply = e1.get()
            status = e2.get()
            mycursor = mydb.cursor()
            mycursor.execute("update mandi set reply=\'{}\', status=\'{}\' where no=\'{}\'".format(reply,status,sno))
            mydb.commit()
            easygui.msgbox("RECORD SUCCESSFULLY UPDATED!", title="SUCCESS!")

        updtbut = Button(tktgovt , text = 'Update' , command = updatevals)
        updtbut.pack()
        tktgovt.mainloop()
    for i in range(len(titles)):
        options.append((titlesi[i],i))
    tk.Label(catgovt,
         text="""Tap to view ticket""",
         justify = tk.LEFT,
         padx = 20).pack()
    v=tk.IntVar()
    v.set(0)

    for tit, val in enumerate(titlesi):
        tk.Radiobutton(catgovt,
                  text=val,
                  indicatoron=0,
                  width=20,
                  padx = 20,
                  variable=v,
                  command=showtkt,
                  value=tit,
                  background="light blue").pack(anchor=tk.W)
    catgovt.mainloop()


but1 = Button(govt , text = "NEXT >" , command = nextbut)
but1.pack()

govt.mainloop()
