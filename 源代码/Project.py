import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
import mysql.connector as mysql
import os

def about():
    """关于界面"""
    def b1_return():
        root6.destroy()
        main_interface()

    root6 = tk.Tk()
    root6.resizable(width=tk.FALSE, height=tk.FALSE)
    root6.geometry("400x300+%d+%d" % ((root6.winfo_screenwidth()/2) - (400/2), (root6.winfo_screenheight()/2) - (300/2)))
    root6.title('关于')
    l1 = ttk.Label(root6, text='产品管理系统', font=('微软雅黑', 40))
    l1.pack(padx=20, pady=20)
    l2 = ttk.Label(root6, text='制作人：刘琛', font=('微软雅黑', 10))
    l2.pack(padx=10, pady=5)
    l3 = ttk.Label(root6, text='单位：湖南大学', font=('微软雅黑', 10))
    l3.pack(padx=10, pady=5)
    l4 = ttk.Label(root6, text='版本号：2018.8.10', font=('微软雅黑', 10))
    l4.pack(padx=10, pady=5)
    b1 = ttk.Button(root6, text='返回', command=b1_return)
    b1.pack(padx=10, pady=20, side=tk.BOTTOM)
    root6.mainloop()

def product_searchdelete():
    """产品查询和修改"""

    global SELECTTABLE
    def b2_delete():

        if len(lb1.curselection()) == 0:
            mbox.showerror('错误', '请选择要删除的产品')
        else:

            global SELECTTABLE
            SELECTTABLE = lb1.get(lb1.curselection())
            file = open("MySQL账户.txt", "r")
            mysql_host = file.readline()
            mysql_username = file.readline()
            mysql_password = file.readline()
            file.close()
            conn = mysql.connect(host=mysql_host, user=mysql_username, password=mysql_password, database='project')
            cursor = conn.cursor()
            exword = 'drop table ' + SELECTTABLE
            if mbox.askyesno('提示', '确定要删除整个产品的数据？') == True:
                cursor.execute(exword)
                lb1.delete(lb1.curselection())
            cursor.close()
            conn.close()

    def b1_return():
        root5.destroy()
        main_interface()

    def b3_search(event=None):

        if len(lb1.curselection()) == 0:
            mbox.showerror('错误', '请选择要查询的产品')
        else:
            def b4_delete():
                if len(tv1.selection()) == 0:
                    mbox.showerror('错误', '请选择要删除的产品')
                else:
                    exword = 'delete from ' + SELECTTABLE + ' where ID=' + tv1.item(tv1.selection(), 'values')[0] + ';'
                    file = open("MySQL账户.txt", "r")
                    mysql_host = file.readline()
                    mysql_username = file.readline()
                    mysql_password = file.readline()
                    file.close()
                    conn = mysql.connect(host=mysql_host, user=mysql_username, password=mysql_password, database='project')
                    cursor = conn.cursor()
                    cursor.execute(exword)
                    conn.commit()
                    cursor.close()
                    conn.close()
                    tv1.delete(tv1.selection())

            def b5_return():
                tl1.destroy()

            global SELECTTABLE
            SELECTTABLE = lb1.get(lb1.curselection())
            names = []
            types = []
            file = open("MySQL账户.txt", "r")
            mysql_host = file.readline()
            mysql_username = file.readline()
            mysql_password = file.readline()
            file.close()
            conn = mysql.connect(host=mysql_host, user=mysql_username, password=mysql_password, database='project')
            cursor = conn.cursor()
            cursor.execute('desc ' + SELECTTABLE)
            for item in cursor.fetchall():
                names.append(item[0])
                types.append(item[1])
            cursor.execute('select * from ' + SELECTTABLE)
            datas = cursor.fetchall()
            cursor.close()
            conn.close()


            tl1 = tk.Toplevel()
            tl1.title(SELECTTABLE + '产品表')
            # tl1.geometry('500x300')
            tl1.geometry("600x700+%d+%d" % ((root5.winfo_screenwidth()/2) - (600/2), (root5.winfo_screenheight()/2) - (700/2)))

            tv1 = ttk.Treeview(tl1, show="headings", columns=names, selectmode=tk.BROWSE)
            for name in names:
                tv1.column(name, anchor='center', width=len(name)*20)
                tv1.heading(name, text=name)
            for data in datas:
                tv1.insert('', tk.END, values=data)
            tv1.pack(fill=tk.BOTH, expand=1)
            f2 = ttk.Frame(tl1)
            f2.pack(fill=tk.Y, expand=0)
            b4 = ttk.Button(f2, text='删除', command=b4_delete)
            b4.pack(side=tk.LEFT, fill=tk.Y, expand=0)
            b5 = ttk.Button(f2, text='返回', command=b5_return)
            b5.pack(side=tk.RIGHT, fill=tk.Y, expand=0)
            tl1.mainloop()

    tables = []
    file = open("MySQL账户.txt", "r")
    mysql_host = file.readline()
    mysql_username = file.readline()
    mysql_password = file.readline()
    file.close()
    conn = mysql.connect(host=mysql_host, user=mysql_username, password=mysql_password, database='project')
    cursor = conn.cursor()
    cursor.execute('show tables')
    for table in cursor.fetchall():
        tables.append(*table)
    cursor.close()
    conn.close()


    root5 = tk.Tk()
    root5.title('产品查询和删除')
    # root5.resizable(width=tk.FALSE, height=tk.FALSE)
    root5.geometry("500x800+%d+%d" % ((root5.winfo_screenwidth()/2) - (500/2), (root5.winfo_screenheight()/2) - (800/2)))

    lf1 = ttk.LabelFrame(root5, text='产品列表：')
    lf1.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)
    lb1 = tk.Listbox(lf1, selectmode=tk.SINGLE)
    lb1.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)
    for table in tables:
        lb1.insert(tk.END, table)
    f1 = ttk.Frame(root5)
    f1.pack(fill=tk.Y, expand=0)
    b2 = ttk.Button(f1, text='删除', command=b2_delete)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = ttk.Button(f1, text='查询', command=b3_search)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    b1 = ttk.Button(f1, text='返回', command=b1_return)
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    root5.mainloop()


def product_entry():
    """产品录入"""
    global SELECTTABLE  # 存储产品表名，多个程序段要用
    def lb1_selection(event=None):
        """"选择产品"""
        if len(lb1.curselection()) != 0:
            global SELECTTABLE
            SELECTTABLE = lb1.get(lb1.curselection())
            names = []  # 存储表的各属性名
            types = []  # 存储表的各属性的值类型
            file = open("MySQL账户.txt", "r")
            mysql_host = file.readline()
            mysql_username = file.readline()
            mysql_password = file.readline()
            file.close()
            conn = mysql.connect(host=mysql_host, user=mysql_username, password=mysql_password, database='project')
            cursor = conn.cursor()
            cursor.execute('desc ' + SELECTTABLE)
            for item in cursor.fetchall():
                names.append(item[0])
                types.append(item[1])
            cursor.close()
            conn.close()
            lf2.configure(text=SELECTTABLE+'产品录入：')
            for id in tv1.get_children():
                tv1.delete(id)
            for name, type in zip(names, types):
                tv1.insert('', tk.END, value=(name, type, ''))

            l1.configure(text='属性名称：')
            l2.configure(text='   值类型：')
            ev1.set('')

            b3.configure(state=tk.DISABLED)
            b2.configure(state=tk.DISABLED)

    def tv1_selection(event=None):
        if len(tv1.selection()) != 0:
            id = tv1.selection()
            l1.configure(text='属性名称：' + tv1.item(id, 'values')[0])
            l2.configure(text='   值类型：' + tv1.item(id, 'values')[1])
            ev1.set(tv1.item(id, 'values')[2])
            b3.configure(state=tk.ACTIVE)
            b2.configure(state=tk.ACTIVE)

    def b1_return():
        """返回主界面"""
        root4.destroy()
        main_interface()

    def b2_entry(event=None):
        """键入值"""
        if len(tv1.selection()) == 0:
            mbox.showerror('错误', '请选择产品和要输入的属性')
        else:
            value = e1.get()
            tv1.set(tv1.selection()[0], column='值', value=value)
            ev1.set('')

    def b3_add():
        """录入数据库"""
        global SELECTTABLE
        file = open("MySQL账户.txt", "r")
        mysql_host = file.readline()
        mysql_username = file.readline()
        mysql_password = file.readline()
        file.close()
        conn = mysql.connect(host=mysql_host, user=mysql_username, password=mysql_password, database='project')
        cursor = conn.cursor()

        insertnames = []
        insertvalues = []
        IDs = []  # 存储数据库中以有的产品ID号
        flag = False  # 判断录入值是否为空的标志位

        cursor.execute('select ID from ' + SELECTTABLE)
        for ID in cursor.fetchall():
            IDs.append(*ID)

        exword = 'insert into ' + SELECTTABLE + ''
        for id in tv1.get_children():
            insertnames.append(tv1.item(id, 'values')[0])
            insertvalues.append(tv1.item(id, 'values')[2])
            if tv1.item(id, 'values')[2] == '':
                flag = True

        temp = ''
        for name in insertnames:
            temp = temp + name + ","
        exword = exword + '(' + temp[:-1] + ') values('
        temp = ''
        for value in insertvalues:
            if not value.isdigit():
                temp = temp + "'" + value + "',"
            else:
                temp = temp + value + ','
        exword = exword + temp[:-1] + ');'

        if flag == True:
            mbox.showerror('错误', '存在值为空')
        elif int(insertvalues[0]) in IDs:  # insertvalues[0]为小数时会出现BUG
            mbox.showerror('错误', '插入ID值已经存在')
        else:
            try:
                cursor.execute(exword)
                conn.commit()
                mbox.showinfo('提示', '产品录入成功')
            except mysql.Error:
                mbox.showerror('错误', '输入值类型不正确')

        cursor.close()
        conn.close()

    file = open("MySQL账户.txt", "r")
    mysql_host = file.readline()
    mysql_username = file.readline()
    mysql_password = file.readline()
    file.close()
    conn = mysql.connect(host=mysql_host, user=mysql_username, password=mysql_password, database='project')
    cursor = conn.cursor()
    cursor.execute('show tables')
    tables = []  # 存放数据库中已有的产品表名
    for table in cursor.fetchall():
        tables.append(*table)
    cursor.close()
    conn.close()

    root4 = tk.Tk()
    root4.geometry("1100x500+%d+%d" % ((root4.winfo_screenwidth()/2) - (1024/2), (root4.winfo_screenheight()/2) - (500/2)))
    root4.title('产品录入')

    f1 = ttk.Frame(root4)
    f1.pack(fill=tk.BOTH, expand=1)

    lf1 = ttk.LabelFrame(f1, text='产品选择：')
    lf1.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=1)
    lb1 = tk.Listbox(lf1, selectmode=tk.SINGLE)
    lb1.pack(padx=5, pady=5, fill=tk.BOTH, expand=1)
    for table in tables:
        lb1.insert(tk.END, table)
    lb1.bind('<ButtonRelease-1>', lb1_selection)

    lf2 = ttk.LabelFrame(f1, text='')
    lf2.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.BOTH, expand=1)
    tv1 = ttk.Treeview(lf2, show="headings", columns=('属性名称', '值类型', '值'))
    tv1.column('属性名称', anchor='center')
    tv1.column('值类型', anchor='center')
    tv1.column('值', anchor='center')
    tv1.heading('属性名称', text='属性名称')
    tv1.heading('值类型', text='值类型')
    tv1.heading('值', text='值')
    tv1.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=1)
    tv1.bind('<ButtonRelease-1>', tv1_selection)

    f2 = ttk.Frame(lf2)
    f2.pack(side=tk.RIGHT, padx=5, pady=5)
    l1 = ttk.Label(f2, text='属性名称：')
    l1.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W, columnspan=2)
    l2 = ttk.Label(f2, text='   值类型：')
    l2.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W, columnspan=2)
    l3 = ttk.Label(f2, text='         值：')
    l3.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
    ev1 = tk.StringVar()
    e1 = ttk.Entry(f2, width=20,  textvariable=ev1)
    e1.grid(column=1, row=2, padx=5, pady=5)

    f3 = ttk.Frame(root4)
    f3.pack(side=tk.BOTTOM, padx=5, pady=5)

    b1 = ttk.Button(f3, text='返回', width=10, command=b1_return)
    b1.pack(side=tk.RIGHT, padx=50, pady=10)
    b2 = ttk.Button(f2, text='键值', width=10, command=b2_entry, state=tk.DISABLED)
    b2.grid(column=0, row=3, padx=5, pady=5, columnspan=2)
    b3 = ttk.Button(f3, text='录入', width=10, command=b3_add, state=tk.DISABLED)
    b3.pack(side=tk.LEFT, padx=50, pady=10)

    root4.mainloop()


def product_creation():
    """创建新产品界面"""

    def b1_return():
        """返回主界面"""
        root3.destroy()
        main_interface()

    def b2_add(event=None):
        """添加"""
        insertname = e2.get()
        inserttype = cb1.get()
        names = []  # 获取列表中已有的属性，用来检测属性是否重复
        itemsID = tv1.get_children()
        for id in itemsID:
            names.append(tv1.item(id, 'values')[0])

        if len(insertname) == 0 or len(inserttype) == 0:
            mbox.showinfo('提示', '输入属性名称和属性类型不能为空')
        elif insertname in names:
            mbox.showinfo('提示', '已有属性名称')
        else:
            tv1.insert('', tk.END, values=(insertname, inserttype))

    def b3_delete():
        """删除"""
        if len(tv1.selection()) > 0:
            for item in tv1.selection():
                tv1.delete(item)
        else:
            mbox.showinfo('提示', '请选择要删除的属性')

    def b4_create():
        """创建新产品表格"""

        file = open("MySQL账户.txt", "r")
        mysql_host = file.readline()
        mysql_username = file.readline()
        mysql_password = file.readline()
        file.close()
        conn = mysql.connect(host=mysql_host, user=mysql_username, password=mysql_password, database='project')
        cursor = conn.cursor()
        cursor.execute('show tables')
        names = []  # 保存数据库中已有的产品表名
        for name in cursor.fetchall():
            names.append(*name)

        insertname = str(e1.get())  # 得到要创建新产品表名

        if len(tv1.get_children()) == 0 or len(insertname) == 0:
            mbox.showinfo('提示', '名称和信息不能为空')
        elif insertname.isdigit():
            mbox.showinfo('提示', '产品名称开头不能为数字')
        elif insertname in names:
            mbox.showerror('错误', '数据库已创建该产品')
        else:
            exword = 'create table ' + insertname + '('
            for id in tv1.get_children():
                exword = exword + tv1.item(id, 'values')[0] + ' ' + tv1.item(id, 'values')[1] + ','
            exword = exword[:-1] + ') charset=utf8'
            cursor.execute(exword)
            conn.commit()
            mbox.showinfo('提示', '新产品创建成功')

        cursor.close()
        conn.close()

    root3 = tk.Tk()
    root3.resizable(width=tk.FALSE, height=tk.FALSE)
    root3.geometry("480x600+%d+%d" % ((root3.winfo_screenwidth()/2) - (480/2), (root3.winfo_screenheight()/2) - (480/2)))
    root3.title('创建新产品')

    f1 = ttk.Frame(root3)
    f1.pack(pady=20, padx=5)

    l1 = ttk.Label(f1, text='产品名称：', width=10)
    l1.grid(column=0, row=0)
    e1 = ttk.Entry(f1, width=20)
    e1.grid(column=1, row=0)

    lf1 = ttk.LabelFrame(root3, text='信息：')
    lf1.pack(padx=5, pady=5, fill=tk.Y, expand=1)

    f2 = ttk.Frame(lf1)
    f2.pack(pady=5, padx=5)

    l2 = ttk.Label(f2, text='属性名称：')
    l2.pack(padx=5, pady=5, side=tk.LEFT)
    e2 = ttk.Entry(f2, width=30)
    e2.pack(padx=5, pady=5, side=tk.RIGHT)

    f3 = ttk.Frame(lf1)
    f3.pack(pady=5, padx=5)

    l3 = tk.Label(f3, text='属性类型：')
    l3.pack(padx=5, pady=5, side=tk.LEFT)

    cb1 = ttk.Combobox(f3, width=28)
    cb1["state"] = "readonly"
    cb1["values"] = ("int auto_increment primary key", "int", "float", "char(30)", "datetime", 'date')
    cb1.pack(padx=5, pady=5, side=tk.RIGHT)

    f4 = ttk.Frame(lf1)
    f4.pack(pady=5, padx=5)

    b2 = ttk.Button(f4, text='添加', width=10, command=b2_add)
    b2.pack(padx=5, pady=5, side=tk.LEFT)

    b3 = ttk.Button(f4, text='删除', width=10, command=b3_delete)
    b3.pack(padx=5, pady=5, side=tk.RIGHT)

    f5 = ttk.Frame(lf1, width=70)
    f5.pack(padx=5, pady=5, fill=tk.Y, expand=1)
    tv1 = ttk.Treeview(f5, show="headings", columns=('属性名称', '属性类型'))
    tv1.column('属性名称', anchor='center')
    tv1.column('属性类型', anchor='center')
    tv1.heading('属性名称', text='属性名称')
    tv1.heading('属性类型', text='属性类型')
    tv1.pack(side=tk.LEFT, fill=tk.Y, expand=1)

    tv1.insert('', tk.END, value=("ID", "int auto_increment primary key"))
    tv1.insert('', tk.END, value=("名称1", "int"))
    tv1.insert('', tk.END, value=("名称2", "float"))
    tv1.insert('', tk.END, value=("名称3", "char(30)"))
    tv1.insert('', tk.END, value=("名称4", "char(30)"))
    tv1.insert('', tk.END, value=("名称5", "float"))
    tv1.insert('', tk.END, value=("名称6", "date"))
    tv1.insert('', tk.END, value=("名称7", "int"))
    tv1.insert('', tk.END, value=("名称8", "datetime"))
    tv1.insert('', tk.END, value=("名称9", "int"))
    tv1.insert('', tk.END, value=("名称10", "datetime"))
    tv1.insert('', tk.END, value=("生产日期", "datetime"))

    sb1 = ttk.Scrollbar(f5, orient=tk.VERTICAL, command=tv1.yview)
    tv1.configure(yscrollcommand=sb1.set)
    sb1.pack(side=tk.RIGHT, fill=tk.Y, expand=1)

    f6 = ttk.Frame(root3)
    f6.pack(padx=5, pady=5)

    b1 = ttk.Button(f6, text='返回', width=10, command=b1_return)
    b1.pack(padx=5, pady=5, side=tk.RIGHT)

    b4 = ttk.Button(f6, text='创建', width=10, command=b4_create)
    b4.pack(padx=5, pady=5, side=tk.LEFT)

    root3.bind('<Return>', b2_add)
    root3.mainloop()


def main_interface():
    """主界面"""
    def b1_product_searchdelete():
        root2.destroy()
        product_searchdelete()

    def b2_product_entry():
        root2.destroy()
        product_entry()

    def b3_product_creation():
        root2.destroy()
        product_creation()

    def b4_about():
        root2.destroy()
        about()

    def b5_Logout():
        os.remove('MySQL账户.txt')
        root2.destroy()
        login()

    def b6_exit():
        root2.destroy()
        os._exit(0)

    root2 = tk.Tk()
    root2.resizable(width=tk.FALSE, height=tk.FALSE)
    root2.geometry("512x384+%d+%d" % ((root2.winfo_screenwidth()/2) - (512/2), (root2.winfo_screenheight()/2) - (384/2)))
    root2.title('产品管理系统')

    e1 = ttk.Label(root2, text='产品管理系统', font=('微软雅黑', 40))
    e1.pack(padx=20, pady=20)

    b1 = ttk.Button(root2, text='产品查询和删除', width=20, command=b1_product_searchdelete)
    b1.pack(padx=10, pady=5)

    b2 = ttk.Button(root2, text='产品录入', width=20, command=b2_product_entry)
    b2.pack(padx=10, pady=5)

    b3 = ttk.Button(root2, text='新产品创建', width=20, command=b3_product_creation)
    b3.pack(padx=10, pady=5)

    b4 = ttk.Button(root2, text='关于', width=20, command=b4_about)
    b4.pack(padx=10, pady=5)

    b5 = ttk.Button(root2, text='注销', width=20, command=b5_Logout)
    b5.pack(padx=10, pady=5)

    b6 = ttk.Button(root2, text='退出', width=20, command=b6_exit)
    b6.pack(padx=10, pady=5)

    root2.mainloop()


def login():
    """"登录本机MySQL界面"""
    def b1_login(event=None):
        mysql_host = e1.get()
        mysql_username = e2.get()
        mysql_password = e3.get()
        try:
            conn = mysql.connect(host=mysql_host, user=mysql_username, password=mysql_password)
            conn.close()
        except mysql.Error:
            mbox.showerror('错误', '登录的服务器、账户或密码错误')
        else:
            file = open("MySQL账户.txt", "w")
            file.write(mysql_host + "\n" + mysql_username + "\n" + mysql_password)
            file.close()
            root1.destroy()
            main_interface()

    def b2_exit():
        root1.destroy()
        os._exit(0)

    root1 = tk.Tk()
    root1.resizable(width=tk.FALSE, height=tk.FALSE)
    root1.geometry("256x175+%d+%d" % (root1.winfo_screenwidth()/2 - 256/2, root1.winfo_screenheight()/2 - 175/2))
    root1.title('登录')

    f1 = ttk.Frame(root1)
    f1.pack()
    l1 = ttk.Label(f1, text='服务器：', width=6)
    l1.pack(side=tk.LEFT, padx=10, pady=10)
    e1 = ttk.Entry(f1)
    e1.pack(side=tk.RIGHT, padx=10, pady=10)

    f2 = ttk.Frame(root1)
    f2.pack()
    l2 = ttk.Label(f2, text='用户名：', width=6)
    l2.pack(side=tk.LEFT, padx=10, pady=10)
    e2v = tk.StringVar()
    e2 = ttk.Entry(f2, textvariable=e2v)
    e2v.set('root')
    e2.pack(side=tk.RIGHT, padx=10, pady=10)

    f3 = ttk.Frame(root1)
    f3.pack()
    l3 = ttk.Label(f3, text='   密码:', width=6)
    l3.pack(side=tk.LEFT, padx=10, pady=10)
    e3 = ttk.Entry(f3, show="*")
    e3.pack(side=tk.RIGHT, padx=10, pady=10)

    f4 = ttk.Frame(root1)
    f4.pack()
    b1 = ttk.Button(f4, text="登录", command=b1_login)
    b1.pack(padx=10, pady=10, side=tk.LEFT)
    b2 = ttk.Button(f4, text="退出", command=b2_exit)
    b2.pack(padx=10, pady=10, side=tk.RIGHT)

    root1.bind('<Return>', b1_login)
    root1.mainloop()


def run():
    """初始化"""
    if not os.path.exists("MySQL账户.txt"):  # 判断MySQL账户.txt文件是否存在
        login()
    file = open("MySQL账户.txt", "r")  # 读取账户，如果文件被修改可能会出现BUG
    mysql_host = file.readline()
    mysql_username = file.readline()
    mysql_password = file.readline()
    file.close()
    try:
        conn = mysql.connect(host=mysql_host, user=mysql_username, password=mysql_password)
        cursor = conn.cursor()
        cursor.execute('show databases')  # 判断是否有project数据库，没有则创建数据库
        databaseslist=[]
        for database in cursor.fetchall():
            databaseslist.append(*database)
        if 'project' not in databaseslist:
            cursor.execute('create database project')
            conn.commit()
        cursor.close()
        conn.close()
    except mysql.Error:
        login()
    else:
        main_interface()  # 如果上面全部通过则进入主界面，不然就进入登录界面重新登录


if __name__ == '__main__':
    run()
