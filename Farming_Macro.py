import pyautogui as ag
from tkinter import *
import time


w=False


letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",'t',"u","v","w","x","y","z"]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def start():
    pi = preparation_input.get()
    ib = initial_button_input.get()
    cti = change_to_input.get()
    ci = cycle_input.get()
    wi = wait_input.get()
    lcb = button_while_lane_changing_input.get()
    if is_number(pi):
        time.sleep(float(pi))
        if len(ib) > 1 or len(cti) > 1:
            initial_button_input.delete(0,END)
            initial_button_input.insert(0,'Please enter one key/button only')
            change_to_input.delete(0,END)
            change_to_input.insert(0,'Please enter one key/button only')
        elif len(ib) == 0 or len(cti) == 0:
            initial_button_input.delete(0,END)
            initial_button_input.insert(0,'Cannot be blank')
            change_to_input.delete(0,END)
            change_to_input.insert(0,'Cannot be blank')
        else:
            if ib.lower() in letters and cti.lower() in letters:
                if ci.isnumeric():
                    if is_number(wi):
                        if len(lcb) < 1:
                            if w:
                                ag.keyDown("w")
                                ag.mouseDown()
                                for i in range(int(ci)):
                                    ag.keyDown(ib)
                                    time.sleep(int(wi))
                                    ag.keyUp(ib)
                                    ag.keyDown(cti)
                                    time.sleep(int(wi))
                                    ag.keyUp(cti)
                                ag.keyUp("w")
                                ag.mouseUp()
                            else:
                                ag.mouseDown()
                                for i in range(int(ci)):
                                    ag.keyDown(ib)
                                    time.sleep(int(wi))
                                    ag.keyUp(ib)
                                    ag.keyDown(cti)
                                    time.sleep(int(wi))
                                    ag.keyUp(cti)
                                ag.mouseUp()
                        elif len(lcb) == 1:
                            if w:
                                ag.keyDown("w")
                                ag.mouseDown()
                                for i in range(int(ci)):
                                    ag.keyDown(ib)
                                    time.sleep(int(wi))
                                    ag.keyUp(ib)
                                    ag.keyDown(lcb)
                                    time.sleep(2)
                                    ag.keyUp(lcb)
                                    ag.keyDown(cti)
                                    time.sleep(int(wi))
                                    ag.keyUp(cti)
                                    ag.keyDown(lcb)
                                    time.sleep(2)
                                    ag.keyUp(lcb)
                                ag.keyUp("w")
                                ag.mouseUp()
                            else:
                                ag.mouseDown()
                                for i in range(int(ci)):
                                    ag.keyDown(ib)
                                    time.sleep(int(wi))
                                    ag.keyUp(ib)
                                    ag.keyDown(lcb)
                                    time.sleep(2)
                                    ag.keyUp(lcb)
                                    ag.keyDown(cti)
                                    time.sleep(int(wi))
                                    ag.keyUp(cti)
                                    ag.keyDown(lcb)
                                    time.sleep(2)
                                    ag.keyUp(lcb)
                                ag.mouseUp()
                        else:
                            button_while_lane_changing_input.delete(0,END)
                            button_while_lane_changing_input.insert(0,'Please enter one key/button only')
                    elif len(wi) == 0:
                        wait_input.delete(0,END)
                        wait_input.insert(0,'Cannot be blank') 
                    else:
                        wait_input.delete(0,END)
                        wait_input.insert(0,'Please enter numbers only')  
                elif len(ci) == 0:
                    cycle_input.delete(0,END)
                    cycle_input.insert(0,'Cannot be blank') 
                else:
                    cycle_input.delete(0,END)
                    cycle_input.insert(0,'Please enter numbers only')
            else:
                initial_button_input.delete(0,END)
                initial_button_input.insert(0,'Please enter a proper key/button')
                change_to_input.delete(0,END)
                change_to_input.insert(0,'Please enter a proper key/button')
    elif len(pi) == 0:
        preparation_input.delete(0,END)
        preparation_input.insert(0,'Cannot be blank')
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
              text='Time before the macro starts (s)',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
preparation.place(x=60,y=120)

one_cycle = Label(gui,
              text='One cycle:',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
one_cycle.place(x=210,y=220)

initial_button = Label(gui,
              text='Initial button',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
initial_button.place(x=195,y=250)

wait = Label(gui,
              text='Farm time(s)',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
wait.place(x=196,y=280)

button_while_lane_changing = Label(gui,
              text='Lane change button(if needed)',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
button_while_lane_changing.place(x=67,y=310)

change_to = Label(gui,
              text='Change to',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
change_to.place(x=210,y=340)

wait_again = Label(gui,
              text='Wait again',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
wait_again.place(x=208,y=370)

cycle = Label(gui,
              text='Cycle times',
              font=('Arial',15,'bold'),
              fg='black',
              bg='#cecece')
cycle.place(x=200,y=400)

farming_talisman = Label(gui,
              image=image,
              bg='#cecece')
farming_talisman.place(x=400,y=230)







preparation_input = Entry()
preparation_input.config(bg='#FFFFFF',
                         fg='#000000')
preparation_input.place(x=300,y=120)

initial_button_input = Entry()
initial_button_input.config(bg='#FFFFFF',
                            fg='#000000')
initial_button_input.place(x=300,y=250)

wait_input = Entry()
wait_input.config(bg='#FFFFFF',
                  fg='#000000')
wait_input.place(x=300,y=280)

button_while_lane_changing_input = Entry()
button_while_lane_changing_input.config(bg='#FFFFFF',
                                        fg='#000000')
button_while_lane_changing_input.place(x=300,y=310)

change_to_input = Entry()
change_to_input.config(bg='#FFFFFF',
                       fg='#000000')
change_to_input.place(x=300,y=340)

cycle_input = Entry()
cycle_input.config(bg='#FFFFFF',
                   fg='#000000')
cycle_input.place(x=300,y=400)





button_start = Button(gui,text='Start')
button_start.config(command=start,
                    font=('Arial',12,'bold'),
                    bg='#cecece',
                    fg='black',
                    highlightbackground='#cecece',
                    activebackground='#000000',)
button_start.place(x=325,y=450)






press_w = Checkbutton(gui,text="press 'w'")
press_w.config(command=with_w,
                        font=('Arial',15,'bold'),
                        bg='#cecece',
                        fg='black',
                        highlightbackground='#cecece',
                        activebackground='#000000',)
press_w.place(x=300,y=170)


gui.mainloop()



