import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import *
import mysql.connector
from datetime import date as datetoday
import easygui
from tkinter import font
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hola123",
    database="municipal"
    )
grvno=0

window = ThemedTk(theme='arc')
window.title("Public Grievance Portal")
window.geometry('300x220')

def getticket():

    global category
    global title
    global issue
    global name
    global location
    gettkt = ThemedTk(theme='arc')
    gettkt.title("Submit a ticket")
    gettkt.geometry('300x200')

    frame15 = Frame(gettkt)
    frame15.pack()
    l1 = Label(frame15 , text="    Title : " )
    l1.grid(row = 0 , column = 0)
    l2 = Label(frame15 , text="     Name : " )
    l2.grid(row = 1 , column = 0)
    l3 = Label(frame15 , text="Grievance : " )
    l3.grid(row = 2 , column = 0)
    l5 = Label(frame15 , text=" Category : " )
    l5.grid(row = 3 , column = 0)

    titleentry = Entry(frame15)
    titleentry.grid(row = 0 , column = 1)
    nameentry = Entry(frame15)
    nameentry.grid(row = 1 , column = 1)
    issueentry = Entry(frame15)
    issueentry.grid(row = 2 , column = 1)

    cats = ["CLEANLINESS" , "TRANSPORT" , "HOUSING","ANIMAL HUSBANDRY","AYURVEDA","COOPERATION","ELECTION","ELEMENTARY EDUCATION","ENVIRONMENT, SCIENCE AND TECHNOLOGY","EXCISE AND TAXATION","FISHERIES","FINANCIAL COMMISSIONER (REVENUE)","FOOD,CIVIL SUPPLIES AND CONSUMER AFFAIRS","FOREST","HEALTH AND FAMILY WELFARE","HIGHER EDUCATION","HORTICULTURE","INDUSTRIES","INFORMATION AND PUBLIC RELATIONS","INFORMATION TECHNOLOGY","IRRIGATION AND PUBLIC HEALTH","LABOUR AND EMPLOYMENT","LANGUAGE AND CULTURE","PANCHAYATI RAJ","POLICE DEPARTMENT","PRINTING AND STATIONERY","PUBLIC WORKS","RURAL DEVELOPMENT","SETTLEMENT","SOCIAL JUSTICE & EMPOWERMENT","TECHNICAL EDUCATION,VOCATIONAL AND INDUSTRIAL TRAINING","TOURISM AND CIVIL AVIATION","TOWN AND COUNTARY PLANNING","TRANSPORT","TRIBAL DEVELOPMENT","YOUTH SERVICES AND SPORTS","URBAN DEVELOPMENT"]
    var = StringVar(gettkt)
    var.set("Choose a category")
    catmenu = OptionMenu(frame15 , var , cats[0] ,cats[1] ,cats[2] ,cats[3] ,cats[4] ,cats[5] ,cats[6] ,cats[7] ,cats[8] ,cats[9] ,cats[10] ,cats[11] ,cats[12] ,cats[13] ,cats[14] ,cats[15] ,cats[16] ,cats[17] ,cats[18] ,cats[19] ,cats[20] ,cats[21] ,cats[22] ,cats[23] ,cats[24] ,cats[25] ,cats[26] ,cats[27] ,cats[28] ,cats[29] ,cats[30] ,cats[31] ,cats[32] ,cats[33] ,cats[34] ,cats[35] ,cats[36] )
    catmenu.grid(row = 3 , column = 1)

    category = var.get()
    title = titleentry.get()
    name = nameentry.get()
    issue = issueentry.get()
    def submit():
        mycursor = mydb.cursor()
        status="Unresolved"
        reply="Not Available"
        mycursor = mydb.cursor()
        ls_=[]
        mycursor.execute("select no from mandi")
        for i in mycursor:
            ls_.append(int(i[0]))
        no=max(ls_)+1
        today=datetoday.today()
        Date=today
        category = var.get()
        title = titleentry.get()
        name = nameentry.get()
        issue = issueentry.get()
        import geocoder
        g = geocoder.ip('me')
        location=g.latlng
        mycursor.execute("INSERT INTO MANDI VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(no,category,name ,title,Date, issue, location, status, reply))
        mydb.commit()
        gettkt.destroy()
        easygui.msgbox("TICKET GENERATED WITH SERIAL NO:{}".format(no), title="SUCCESS!")

    subbut = Button(gettkt , text="Submit",command=submit)
    subbut.pack()
    gettkt.mainloop()

def viewticket():
    _lis=[]
    mycursor = mydb.cursor()
    mycursor.execute("select * from Mandi where name=\"{}\"".format(nme))
    for i in mycursor:
        _lis.append(i)
    viewtkt = ThemedTk(theme='arc')
    viewtkt.title("View your tickets")
    #viewtkt.geometry('200x200')

    #Insert code here to fetch the variables one by one
    #Variables are Title , Sno , Name , Complaint , Status , Date , Location , Reply , Category
    #lexp = Label(viewtkt , textvariable = snot)
    #lexp.pack()

    titlet = tk.StringVar(viewtkt)
    titlet.set(title)
    snot = tk.StringVar(viewtkt)
    snot.set(sno)
    namet = tk.StringVar(viewtkt)
    namet.set(name)
    complaintt = tk.StringVar(viewtkt)
    complaintt.set(complaint)
    statust = tk.StringVar(viewtkt)
    statust.set(status)
    datet = tk.StringVar(viewtkt)
    datet.set(date)
    locationt = tk.StringVar(viewtkt)
    locationt.set(location)
    replyt = tk.StringVar(viewtkt)
    replyt.set(reply)
    categoryt = tk.StringVar(viewtkt)
    categoryt.set(category)

    frame1 = Frame(viewtkt)
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

    l7 = Label(frame1 , text = 'Status : ')
    l7.grid(row = 6 , column = 0)
    statuslabel = Label(frame1 , textvariable = statust)
    statuslabel.grid(row = 6 , column = 1)

    l8 = Label(frame1 , text = 'Reply : ')
    l8.grid(row = 7 , column = 0)
    replylabel = Label(frame1 , textvariable = replyt)
    replylabel.grid(row = 7 , column = 1)

    nextbutton = Button(viewtkt , text="NEXT")
    nextbutton.pack()

    viewtkt.mainloop()

def namewindow():
    name = ThemedTk(theme='arc')
    name.title("Enter your name")
    #name.geometry('150x150')

    def button():
        global viewtkt
        global nme
        global grvno
        global _lis
        nme=e1.get()
        name.destroy()
        _lis=[]
        mycursor = mydb.cursor()
        mycursor.execute("select * from Mandi where name=\"{}\"".format(nme))
        for i in mycursor:
            _lis.append(i)
        if len(_lis)==0:
            easygui.msgbox("NO GRIEVANCE WITH THIS NAME FOUND", title="INFORMATION!")
            quit()


        viewtkt = ThemedTk(theme='arc')
        viewtkt.title("View your tickets")
        #viewtkt.geometry('200x200')

        #Insert code here to fetch the variables one by one
        #Variables are Title , Sno , Name , Complaint , Status , Date , Location , Reply , Category
        #lexp = Label(viewtkt , textvariable = snot)
        #lexp.pack()
        sno,category,nm,title,date,complaint,location,status,reply=_lis[grvno]
        titlet = tk.StringVar(viewtkt)
        titlet.set(title)
        snot = tk.StringVar(viewtkt)
        snot.set(sno)
        namet = tk.StringVar(viewtkt)
        namet.set(nm)
        complaintt = tk.StringVar(viewtkt)
        complaintt.set(complaint)
        statust = tk.StringVar(viewtkt)
        statust.set(status)
        datet = tk.StringVar(viewtkt)
        datet.set(date)
        locationt = tk.StringVar(viewtkt)
        locationt.set(location)
        replyt = tk.StringVar(viewtkt)
        replyt.set(reply)
        categoryt = tk.StringVar(viewtkt)
        categoryt.set(category)

        frame1 = Frame(viewtkt)
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

        l7 = Label(frame1 , text = 'Status : ')
        l7.grid(row = 6 , column = 0)
        statuslabel = Label(frame1 , textvariable = statust)
        statuslabel.grid(row = 6 , column = 1)

        l8 = Label(frame1 , text = 'Reply : ')
        l8.grid(row = 7 , column = 0)
        replylabel = Label(frame1 , textvariable = replyt)
        replylabel.grid(row = 7 , column = 1)

        def nextbutt():
            global grvno
            global viewtkt
            if len(_lis)-1>grvno:
                grvno+=1
            viewtkt.destroy()
            viewtkt = ThemedTk(theme='arc')
            viewtkt.title("View your tickets")
            #viewtkt.geometry('200x200')

            #Insert code here to fetch the variables one by one
            #Variables are Title , Sno , Name , Complaint , Status , Date , Location , Reply , Category
            #lexp = Label(viewtkt , textvariable = snot)
            #lexp.pack()
            sno,category,nm,title,date,complaint,location,status,reply=_lis[grvno]
            titlet = tk.StringVar(viewtkt)
            titlet.set(title)
            snot = tk.StringVar(viewtkt)
            snot.set(sno)
            namet = tk.StringVar(viewtkt)
            namet.set(nm)
            complaintt = tk.StringVar(viewtkt)
            complaintt.set(complaint)
            statust = tk.StringVar(viewtkt)
            statust.set(status)
            datet = tk.StringVar(viewtkt)
            datet.set(date)
            locationt = tk.StringVar(viewtkt)
            locationt.set(location)
            replyt = tk.StringVar(viewtkt)
            replyt.set(reply)
            categoryt = tk.StringVar(viewtkt)
            categoryt.set(category)

            frame1 = Frame(viewtkt)
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

            l7 = Label(frame1 , text = 'Status : ')
            l7.grid(row = 6 , column = 0)
            statuslabel = Label(frame1 , textvariable = statust)
            statuslabel.grid(row = 6 , column = 1)

            l8 = Label(frame1 , text = 'Reply : ')
            l8.grid(row = 7 , column = 0)
            replylabel = Label(frame1 , textvariable = replyt)
            replylabel.grid(row = 7 , column = 1)

            frame9 = Frame(viewtkt)
            frame9.pack()

            nextbutton = Button(frame9 , text="NEXT", command=nextbutt)
            nextbutton.grid(row = 0 , column = 1)

            prevbutton=Button(frame9, text="PREV", command=prevbutt)
            prevbutton.grid(row = 0 , column = 0)

            delbutton=Button(frame9, text="DEL", command=delbutt)
            delbutton.grid(row = 0 , column = 2)
        def delbutt():
            mycursor = mydb.cursor()
            mycursor.execute("delete from Mandi where no=\"{}\"".format(sno))
            mydb.commit()
            viewtkt.destroy()
            easygui.msgbox("RECORD SUCCESSFULLY DELETED!", title="SUCCESS!")

            viewtkt.mainloop()

        def prevbutt():
            global grvno
            global viewtkt
            if grvno>0:
                grvno-=1
            viewtkt.destroy()
            viewtkt = tk.Tk()
            viewtkt.title("View your tickets")
            #viewtkt.geometry('200x200')

            #Insert code here to fetch the variables one by one
            #Variables are Title , Sno , Name , Complaint , Status , Date , Location , Reply , Category
            #lexp = Label(viewtkt , textvariable = snot)
            #lexp.pack()
            sno,category,nm,title,date,complaint,location,status,reply=_lis[grvno]
            titlet = tk.StringVar(viewtkt)
            titlet.set(title)
            snot = tk.StringVar(viewtkt)
            snot.set(sno)
            namet = tk.StringVar(viewtkt)
            namet.set(nm)
            complaintt = tk.StringVar(viewtkt)
            complaintt.set(complaint)
            statust = tk.StringVar(viewtkt)
            statust.set(status)
            datet = tk.StringVar(viewtkt)
            datet.set(date)
            locationt = tk.StringVar(viewtkt)
            locationt.set(location)
            replyt = tk.StringVar(viewtkt)
            replyt.set(reply)
            categoryt = tk.StringVar(viewtkt)
            categoryt.set(category)

            frame1 = Frame(viewtkt)
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

            l7 = Label(frame1 , text = 'Status : ')
            l7.grid(row = 6 , column = 0)
            statuslabel = Label(frame1 , textvariable = statust)
            statuslabel.grid(row = 6 , column = 1)

            l8 = Label(frame1 , text = 'Reply : ')
            l8.grid(row = 7 , column = 0)
            replylabel = Label(frame1 , textvariable = replyt)
            replylabel.grid(row = 7 , column = 1)

            frame9 = Frame(viewtkt)
            frame9.pack()

            nextbutton = Button(frame9 , text="NEXT", command=nextbutt)
            nextbutton.grid(row = 0 , column = 1)

            prevbutton=Button(frame9, text="PREV", command=prevbutt)
            prevbutton.grid(row = 0 , column = 0)

            delbutton=Button(frame9, text="DEL", command=delbutt)
            delbutton.grid(row = 0 , column = 2)

            viewtkt.mainloop()



        frame9 = Frame(viewtkt)
        frame9.pack()

        nextbutton = Button(frame9 , text="NEXT", command=nextbutt)
        nextbutton.grid(row = 0 , column = 1)

        prevbutton=Button(frame9, text="PREV", command=prevbutt)
        prevbutton.grid(row = 0 , column = 0)

        delbutton=Button(frame9, text="DEL", command=delbutt)
        delbutton.grid(row = 0 , column = 2)

        viewtkt.mainloop()

    frame1 = Frame(name)
    frame1.pack()
    l1 = Label(frame1 , text="Enter your name : ")
    l1.pack(side = LEFT)
    e1 = Entry(frame1)
    e1.pack(side = LEFT)

    but = Button(name , text="Submit" , command = button)
    but.pack()

    name.mainloop()


f1 = Frame(window , padx = 10 , pady =  10)
f1.pack()

f2 = Frame(window , padx = 10 , pady = 10)
f2.pack()

#fontstyle = font.Font(family = 'Helvetica' , size=36 , weight = 'bold')
raiseticket = Button(f1 , text="Raise a ticket" , activeforeground = 'Black' , command=getticket , height = 5 , width = 50 , bg='black' , fg = 'white')
raiseticket.pack()

viewticket = Button(f2 , text="View your tickets" , activeforeground = 'Black' , command=namewindow , height = 5 , width = 50 , bg='black' , fg = 'white')
viewticket.pack()

window.mainloop()
