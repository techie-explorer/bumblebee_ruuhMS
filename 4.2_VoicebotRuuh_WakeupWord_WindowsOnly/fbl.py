from tkinter import *
import tkinter.messagebox as tm
def quit(self):
    self.root.destroy()

username=''
password=''
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        master.geometry("959x587+297+152")
        master.title("Ruuh Voice bot Login Page")
        master.configure(background="#5f87d8")

        #self.Label1 = tk.Label(master)
        """self.Label1.place(relx=0.282, rely=0.375, height=34, width=95)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Facebook Id''')
        self.Label1.configure(width=95)"""
        self.label_username=Label(master=None)
        self.label_password = Label(master=None)
        #self.label_username = Label(self, text="Facebook erwerwId")
        self.label_username.place(relx=0.282, rely=0.375, height=34, width=95)
        self.label_username.configure(background="#d9d9d9")
        self.label_username.configure(foreground="#000000")
        self.label_username.configure(text='''Facebook Id''')
        self.label_username.configure(width=95)
        #label_password
        self.label_password.place(relx=0.282, rely=0.477, height=34, width=95)
        self.label_password.configure(background="#d9d9d9")
        self.label_password.configure(foreground="#000000")
        self.label_password.configure(text='''Password''')
        self.label_password.configure(width=95)

        self.Entry1 = Entry(master=None)
        self.Entry1.place(relx=0.428, rely=0.375,height=30, relwidth=0.357)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=342)

        self.Entry2 = Entry(master=None,show = '*')
        self.Entry2.place(relx=0.428, rely=0.477,height=30, relwidth=0.357)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=342)

        self.Button1 = Button(master=None)
        self.Button1.place(relx=0.469, rely=0.613, height=32, width=131)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(text='''Login''')
        self.Button1.configure(width=131)
        self.Button1.configure(command = self._login_btn_clicked)
        
        #self.Button1.configure(command = self.destroy())
        #self.Button1.configure(command = lambda : [f for f in [self.loginUser(),self.destroy()]])
        
        """
        
        
        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        #self.label_username.grid(row=1, sticky=SE)
        self.label_password.grid(row=2, sticky=SE)
        #self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)

#        self.checkbox = Checkbutton(self, text="Keep me logged in")
#        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)
        """

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        global username
        global password
        username = self.Entry1.get()
        password = self.Entry2.get()
        print('frm login')
        print(username, password)
        #self.pack
        self.quit()

        
#       print('login is succesful')
        #tm.showinfo("Login info", "logging in..")
        #sys.exit()
        #self.quit()
        


def start():
  win=Tk()
  #win.title('fb login page')
  win.geometry('400x300+300+350')
  win.configure(background='blue')
  root= win
  lf = LoginFrame(root)
  root.mainloop()
  root.withdraw()
  #root.destroy()
  root.quit()
  #root.destroy()
  
#  print('from main',username,' ' , password)
#
start()
#root.quit()
#if login is unsucesful we can use :' tm.showerror("Login error", "Incorrect username and passwor")'
