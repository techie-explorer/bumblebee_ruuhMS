from tkinter import *
import tkinter.messagebox as tm
def quit(self):
    self.root.destroy()

username=''
password=''
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_username = Label(self, text="Userid",bg='LightBlue')
        self.label_password = Label(self, text="Password",bg='LightBlue')

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=1, sticky=SE)
        self.label_password.grid(row=2, sticky=SE)
        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)

#        self.checkbox = Checkbutton(self, text="Keep me logged in")
#        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)
        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        global username
        global password
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)
#        print('login is succesful')
        tm.showinfo("Login info", "logging in..")
        #sys.exit()
        self.quit()


def start():
  win=Tk()
  win.title('fb login page')
  #win.geometry('400x300+300+350')
  win.configure(background='blue')
  root= win
  lf = LoginFrame(root)
  root.mainloop()
#  print('from main',username,' ' , password)
#
#if login is unsucesful we can use :' tm.showerror("Login error", "Incorrect username and passwor")'
