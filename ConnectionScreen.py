from serial import Serial
from serial.tools import list_ports
from tkinter import *
from tkinter import messagebox

class ConnectionScreen:

    def __init__(self):


        self.ser = -1
        # Designing the UI
        self.screen = Tk()
        self.screen.geometry('500x100')
        self.screen.resizable(width = False, height = False)
        self.screen.title('Pick your UART settings')

        Label(self.screen, text = 'Select the COM port').grid(row = 1, column = 1)
        Label(self.screen, text = 'Enter the baud rate').grid(row = 3, column = 1)

        self.ports = list_ports.comports()
        self.port_dict = {}
        port_descs = []
        for i in self.ports:
            self.port_dict[i.description] = i.device
            port_descs.append(i.description)

        self.port = StringVar(self.screen)
        if len(port_descs) > 0:
            self.port.set(port_descs[0])

        ports_menu = OptionMenu(self.screen, self.port, *port_descs)
        ports_menu.grid(row = 1, column = 2)

        self.baud_rate_entry = Entry(self.screen, width = 30)
        self.baud_rate_entry.grid(row = 3, column = 2)
        self.baud_rate_entry.insert(END, 115200)

        submit_button = Button(self.screen, text='Connect',
            command = self.connect)
        submit_button.grid(row = 5, column = 2, pady = 15)

        # Displaying the window
        self.screen.mainloop()


    def connect(self):
        try:
            baud_rate = int(self.baud_rate_entry.get())
            if baud_rate <= 0:
                raise
        except:
            messagebox.showerror("Setting baud rate",
            "Please select a positive baud rate")
            return None

        com_port = self.port_dict[self.port.get()]

        try:
            self.ser = Serial(com_port, baud_rate, timeout = 0.5)
            self.screen.destroy()
        except:
            messagebox.showerror("Access Denied",
            "The COM port seems to be busy. It could be in use by another application")
