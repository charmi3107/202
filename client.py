import socket
from threading import Thread
from  tkinter import *

# nickname=input('choose your nickname: ')

client=socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address='127.0.0.1'
port=8000
client.connect((ip_address,port))
class GUI:
    def __init__(self):
        self.Window=Tk()
        self.Window.withdraw()

        self.login=Toplevel()
        self.login.title("login")

        self.login.resizable(width=False,height=False)
        self.login.configure(height=300,width=400)
        self.pls=Label(self.login,text="please login to continue",justify=CENTER)
        self.pls.place(relheight=0.15,relx=0.2,rely=0.07)

        self.labelname=Label(self.login,text="Name ")
        self.labelname.place(relheight=0.2,relx=0.1,rely=0.2)

        self.entryname= Entry(self.login,font='Helvetica 14')
        self.entryname.place(relheight=0.12,relwidth=0.4,relx=0.35,rely=0.2)
        self.entryname.focus()

        self.go= Button(self.login,text='continue',font='Helvetica 14 bold',command=lambda:self.goAhead(self.entryname.get()))
        self.go.place(relx=0.4,rely=0.55)

        self.Window.mainloop()
    def goAhead(self,name):
        self.login.destroy()
        self.name=name
        recv=Thread(target=self.recieve)
        recv.start()
    def recieve(self):
      while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message=='NICKNAME':
                client.send(self.name.encode('utf-8'))
            else:
                pass

        except:
            print('an error occured...')
            client.close()
            break

g=GUI()





print('connected to server...')
"""def recieve():
    while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message=='NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)

        except:
            print('an error occured...')
            client.close()
            break
def write():
    while True:
        message='{}: {}'.format(nickname,input(''))
        client.send(message.encode('utf-8'))
recieve_Thread=Thread(target=recieve)
recieve_Thread.start()
write_thread=Thread(target=write)
write_thread.start()"""
