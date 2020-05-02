from serial import Serial
from serial.tools import list_ports

def connect():
    try:
        baud_rate = int(baud_rate_entry.get())
    except:
        print("Error! Invalid baud rate")
        return

    com_port = port_dict[port.get()]

    ser = Serial(com_port, baud_rate)
    ser.write(b'a')
    ser.close()

# Designing the UI
from tkinter import *

screen = Tk()
screen.geometry('500x100')
screen.resizable(width = False, height = False)
screen.title('Heart Monitor')

Label(screen, text = 'Select the COM port').grid(row = 1, column = 1)
Label(screen, text = 'Enter the baud rate').grid(row = 3, column = 1)

ports = list_ports.comports()
port_dict = {}
port_descs = []
for i in ports:
    port_dict[i.description] = i.device
    port_descs.append(i.description)

port = StringVar(screen)
if len(port_descs) > 0:
    port.set(port_descs[0])

ports_menu = OptionMenu(screen, port, *port_descs)
ports_menu.grid(row = 1, column = 2)

baud_rate_entry = Entry(screen, width = 30)
baud_rate_entry.grid(row = 3, column = 2)

submit_button = Button(screen, text='Connect',
    command=connect)
submit_button.grid(row = 5, column = 2, pady = 15)

# Displaying the window
screen.mainloop()
