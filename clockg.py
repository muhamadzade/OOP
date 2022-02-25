from clock import Clock
import tkinter as tk
class ClockG(Clock):
    def __init__(self,op=2):
        Clock.__init__(self,op=2)
        self.createGUI()
    def createGUI(self):
        self.top=tk.Tk()
        self.top.title('ساعت')
        self.top.resizable(0,0)
        self.top.geometry('+600+300')

        self.fr0=tk.Frame(master=self.top)
        self.fr0.pack()
        self.fr1=tk.Frame(master=self.top)
        self.fr1.pack()
        self.lb=tk.Label(master=self.fr0,
            text='HH:MM:SS',
            bg='darkblue',
            fg='cyan',
            font='Airal 30',
            width=10,
            height=2)

        self.lb.pack(side=tk.TOP)
    
        self.bt=tk.Button(master=self.fr1,
            text='خروج',
            bg='black',
            fg='gray',
            font='Airal 30',
            width=5,
            height=1,
             command=self.top.destroy)
        self.bt.pack(side=tk.LEFT)
        self.bt1=tk.Button(master=self.fr1,
            text='اجرا',
            bg='gray',
            fg='black',
            font='Airal 30',
            width=5,
            height=1,
            command=self.run
                           )
        self.bt1.pack(side=tk.LEFT)
    def run(self):
        def run_():
            self.__next__()
            self.lb.config(text=repr(self))
            self.bt1.after(1000,run_)    

        run_()
    
        
if __name__=="__main__":
    c=ClockG()
