import pyautogui as ag
from tkinter import *
import time

w=False

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",'t',"u","v","w","x","y","z"]

def start():
    pi = preparation_input.get()
    ib = initial_button_input.get()
    balc = button_after_lane_changed_input.get()
    ci = cycle_input.get()
    tblc = time_between_lane_changes_input.get()
    if pi.isnumeric():
        time.sleep(int(pi))
        if len(ib) > 1 or len(balc) > 1:
            initial_button_input.delete(0,END)
            initial_button_input.insert(0,'Please enter one key/button only')
            button_after_lane_changed_input.delete(0,END)
            button_after_lane_changed_input.insert(0,'Please enter one key/button only')
        else:
            if ib in letters and balc in letters:
                if ci.isnumeric():
                    if tblc.isnumeric():
                        print(w)
                        if w:
                            ag.keyDown("w")
                            ag.mouseDown()
                            for i in range(int(ci)):
                                ag.keyDown(ib)
                                time.sleep(int(tblc))
                                ag.keyUp(ib)
                                ag.keyDown(balc)
                                time.sleep(int(tblc))
                                ag.keyUp(balc)
                            ag.keyUp("w")
                            ag.mouseUp()
                        else:
                            ag.mouseDown()
                            for i in range(int(ci)):
                                ag.keyDown(ib)
                                time.sleep(int(tblc))
                                ag.keyUp(ib)
                                ag.keyDown(balc)
                                time.sleep(int(tblc))
                                ag.keyUp(balc)
                            ag.mouseUp()
                    else:
                        time_between_lane_changes_input.delete(0,END)
                        time_between_lane_changes_input.insert(0,'Please enter numbers only')   
                else:
                    cycle_input.delete(0,END)
                    cycle_input.insert(0,'Please enter numbers only')
            else:
                initial_button_input.delete(0,END)
                initial_button_input.insert(0,'Please enter a proper key/button')
                button_after_lane_changed_input.delete(0,END)
                button_after_lane_changed_input.insert(0,'Please enter a proper key/button')
    else:
        preparation_input.delete(0,END)
        preparation_input.insert(0,'Please enter numbers only')

def with_w():
    global w
    if w == True:
        w = False
    else:
        w = True





gui = Tk()
gui.geometry("700x500")
gui.title("Skyblock Farming Macro")

icon = PhotoImage(file='image.png')
image = PhotoImage(file='farming_talisman.png')

gui.iconphoto(True,icon)
gui.config(background='#cecece')







label = Label(gui,
              text="Farming Macro",
              font=('Arial',20,'bold'),
              fg='black',
              bg='#cecece',
              relief=RIDGE,
              bd=5)
label.pack()

preparation = Label(gui,
              text='Time before the macro starts (seconds)',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
preparation.place(x=10,y=120)

initial_button = Label(gui,
              text='Initial button',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
initial_button.place(x=195,y=220)

button_after_lane_changed = Label(gui,
              text='Button after lane changed',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
button_after_lane_changed.place(x=100,y=250)

time_between_lane_changes = Label(gui,
              text='Time between lane changes(seconds)',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
time_between_lane_changes.place(x=15,y=280)

cycle = Label(gui,
              text='Cycle times',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
cycle.place(x=200,y=310)

farming_talisman = Label(gui,
              image=image,
              bg='#cecece')
farming_talisman.place(x=400,y=200)







preparation_input = Entry()
preparation_input.config(bg='#FFFFFF',
                         fg='#000000')
preparation_input.place(x=300,y=120)

initial_button_input = Entry()
initial_button_input.config(bg='#FFFFFF',
                            fg='#000000')
initial_button_input.place(x=300,y=220)

button_after_lane_changed_input = Entry()
button_after_lane_changed_input.config(bg='#FFFFFF',
                                       fg='#000000')
button_after_lane_changed_input.place(x=300,y=250)

time_between_lane_changes_input = Entry()
time_between_lane_changes_input.config(bg='#FFFFFF',
                                       fg='#000000')
time_between_lane_changes_input.place(x=300,y=280)

cycle_input = Entry()
cycle_input.config(bg='#FFFFFF',
                                       fg='#000000')
cycle_input.place(x=300,y=310)





button_start = Button(gui,text='Start')
button_start.config(command=start,
                    font=('Arial',12,'bold'),
                    bg='#cecece',
                    fg='black',
                    highlightbackground='#cecece',
                    activebackground='#000000',)
button_start.place(x=325,y=400)






press_w = Checkbutton(gui,text="press 'w'")
press_w.config(command=with_w,
                        font=('Arial',15,'bold'),
                        bg='#cecece',
                        fg='black',
                        highlightbackground='#cecece',
                        activebackground='#000000',)
press_w.place(x=300,y=170)


gui.mainloop()



