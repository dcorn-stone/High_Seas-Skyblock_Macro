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
    w = True
    with_w_pressed.config(relief=SUNKEN)
    without_w_pressed.config(relief=RAISED)
    w_button = Label(gui,
              text=f"press 'w':{w}",
              font=('Arial',12,'bold'),
              fg='black',
              width=12,
              bg='#cecece',
              bd=5)
    w_button.place(x=290,y=175)
def without_w():
    without_w_pressed.config(relief=SUNKEN)
    with_w_pressed.config(relief=RAISED)
    global w
    w = False
    w_button = Label(gui,
              text=f"press 'w':{w}",
              font=('Arial',12,'bold'),
              fg='black',
              width=12,
              bg='#cecece',
              bd=5)
    w_button.place(x=290,y=175)






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
              text='Time before the macro to start (seconds)',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
preparation.place(x=0,y=120)

w_button = Label(gui,
              text=f"press 'w':{w}",
              font=('Arial',12,'bold'),
              fg='black',
              width=12,
              bg='#cecece',
              bd=5)
w_button.place(x=290,y=175)

initial_button = Label(gui,
              text='Initial button(moving key)',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
initial_button.place(x=105,y=220)

button_after_lane_changed = Label(gui,
              text='Button after lane changed(moving key)',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
button_after_lane_changed.place(x=10,y=250)

time_between_lane_changes = Label(gui,
              text='Time between lane changes(seconds)',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
time_between_lane_changes.place(x=18,y=280)

cycle = Label(gui,
              text='Cycle for how many times',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
cycle.place(x=101,y=310)

cycle = Label(gui,
              image=image,
              bg='#cecece')
cycle.place(x=400,y=200)







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

with_w_pressed = Button(gui,text="With key'w' pressed")
with_w_pressed.config(command=with_w,
                    font=('Arial',12,'bold'),
                    bg='#cecece',
                    fg='black',
                    relief=RAISED,
                    highlightbackground='#cecece',
                    activebackground='#000000',)
with_w_pressed.place(x=150,y=150)

without_w_pressed = Button(gui,text="Without key'w' pressed")
without_w_pressed.config(command=without_w,
                    font=('Arial',12,'bold'),
                    bg='#cecece',
                    fg='black',
                    relief=RAISED,
                    highlightbackground='#cecece',
                    activebackground='#000000',)
without_w_pressed.place(x=400,y=150)




gui.mainloop()



