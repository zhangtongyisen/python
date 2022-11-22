import tkinter as tk
import random
import threading
import time
def dow():
    window=tk.Tk()
    width=window.winfo_screenwidth()
    height=window.winfo_screenheight()
    a=random.randrange(0,width)
    b=random.randrange(0,height)
    window.title('Surprise！')
    window.geometry("400*100"+"+"+str(a)+"+"+str(b))
    tk.Label(window,
             text='我是你爹！！！',
             bg='pink',
             font=('楷体',23),
             width=40,height=15).pack()
    window.mainloop()
threads=[]
for i in range(10):
    t=threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()
