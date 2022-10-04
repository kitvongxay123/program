from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import mysql.connector as mysql
class unit:
    def __init__(self,root):
        self.root=root
        self.root.title('Unit frame')
        self.root.geometry('480x800+300+50')
        unitid=StringVar()
        unitname=StringVar()
        def ShowData():
            conn=mysql.connect(host='localhost',user='root',password='',
                               database='bsp5a')
            cursor=conn.cursor()
            cursor.execute('select * from bsp5a')
            result=cursor.fetchall()
            if(len(result)!=0):
                self.member_record.delete(*self.member_record.get_children())
                for row in result:
                    self.member_record.insert('',END,values=row)
                    cursor.execute('commit')
            conn.close()

        def SaveData():
            conn = mysql.connect(host='localhost', user='root', password='',
                                 database='bsp5a')
            cursor = conn.cursor()
            cursor.execute('Insert into bsp5a values(%s,%s)',
                           (unitid.get(), unitname.get()))
            cursor.execute('commit')
            conn.close()
            ShowData()

        #fonts=font('Time News Roman',16)
        # create mainframe
        mainframe = Frame(self.root, bd=10, width=700, height=700, bg='cadetblue')
        mainframe.grid()
        # create titleframe
        titleframe = Frame(mainframe, bd=7, width=700, height=100, relief=RIDGE)
        titleframe.grid(row=0, column=0)
        # create middleframe
        middleframe = Frame(mainframe, bd=7, width=700, height=300, bg='cadetblue', relief=RIDGE)
        middleframe.grid(row=1, column=0)
        # create buttonframe
        buttonframe = Frame(mainframe, bd=7, width=700, height=100, bg='cadetblue', relief=RIDGE)
        buttonframe.grid(row=2, column=0)
        # create detailframe
        detailframe = Frame(mainframe, bd=7, width=700, height=100, bg='cadetblue', relief=RIDGE)
        detailframe.grid(row=3, column=0)
        # create letfframe
        letfframe = Frame(middleframe, bd=7, width=700, height=200, bg='cadetblue', relief=RIDGE)
        letfframe.pack(side=LEFT, padx=5, pady=0)
        # create innerframe
        innerframe = Frame(letfframe, bd=5, width=700, height=200, bg='azure')
        innerframe.pack(side=TOP, padx=5, pady=0)
        # --------------add wiget------------------
        fonts = ('Times New Roman', 14)
        lbltitle = Label(titleframe, font=('Times New Roman', 22), text='Unit manage', bg='cadetblue')
        lbltitle.grid(row=0, column=0)
        lblUnitID = Label(innerframe, font=fonts, text='Unit ID', width=10, justify=RIGHT)
        lblUnitID.grid(row=0, column=0)
        txtUnitID = Entry(innerframe, font=fonts, textvariable='',width=30)
        txtUnitID.grid(row=0,column=1)

        lblName = Label(innerframe, font=fonts, text='Unit Name', width=10, justify=RIGHT)
        lblName.grid(row=1, column=0)
        txtName = Entry(innerframe, font=fonts, textvariable=unitid, width=30)
        txtName.grid(row=1, column=1)

        btnSave=Button(buttonframe,font=fonts,text='Save',width=8,command=SaveData)
        btnSave.grid(row=0,column=0)
        btnEdit = Button(buttonframe, font=fonts, text='Edit', width=8, command='')
        btnEdit.grid(row=0, column=1)

        btnDelete = Button(buttonframe, font=fonts, text='Delete', width=8, command='')
        btnDelete.grid(row=0, column=2)
        btnExit = Button(buttonframe, font=fonts, text='Exit', width=8, command='')
        btnExit.grid(row=0, column=3)

        #add scrollbar
        scroll_y=Scrollbar(detailframe,orient=VERTICAL)
        self.member_record = ttk.Treeview(detailframe, heigh=12,
                                        columns=('UnitID', 'UnitName', ),
                                        yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        self.member_record.heading('UnitID',text='UnitID')
        self.member_record.heading('UnitName',text='UnitName')
        self.member_record['show'] = "headings"
        self.member_record.column('UnitID',width=200)
        self.member_record.column('UnitID',width=200)
        self.member_record.pack(fill=BOTH,expand=1)
        self.member_record.bind('ButtonRelease-1','')

        ShowData()
if(__name__=='__main__'):
    root=Tk()
    application=unit(root)
    root.mainloop()
