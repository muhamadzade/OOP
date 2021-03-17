import tkinter as tk
def startTime(t):
    lbHour.config(text=f"{t.hour:02}" )
    lbMinute.config(text=f"{t.minute:02}")
    lbSecond.config(text=f"{t.second:02}")
    next(t)
    btStart.after(1000,lambda: startTime(t))
    
if __name__=="__main__":
##    import sys
##    sys.path.append(r"include")
    from zaman import Time
    import datetime
    now=datetime.datetime.now()
    t=Time(now.hour,now.minute,now.second)

    top=tk.Tk()
    top.title("THis is my first tkinter GUI")    
    top.geometry('250x100+100+100')
    top.config(bg='#33ffff')
    lbHour=tk.Label(master=top,
                    text="HH",
                    font='arial 30',
                    )
    lbHour.grid(row=0,column=0)
    tk.Label(master=top,
                    text=":",
                    font='arial 30',
                    ).grid(row=0,column=1)
    
    lbMinute=tk.Label(master=top,
                    text="MM",
                    font='arial 30',
                    )
    lbMinute.grid(row=0,column=2)
    tk.Label(master=top,
                    text=":",
                    font='arial 30',
                    ).grid(row=0,column=3)
    lbSecond=tk.Label(master=top,
                    text="SS",
                    font='arial 30',
                    )
    lbSecond.grid(row=0,column=4)
    btStart=tk.Button(master=top,
                      text='شروع',
                      font='size=20',
                      command= lambda: startTime(t),
                      )
    btStart.grid(row=1,column=4)

    top.mainloop()
