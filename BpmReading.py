from tkinter import *

class BpmReading:
    def __init__(self, ser):
        self.ser = ser

        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        self.ser.write(b'a')

        #Designing the UI
        self.screen = Tk()
        self.screen.geometry('350x300')
        self.screen.resizable(width = False, height = False)
        self.screen.title('BPM Reading')
        v = StringVar(self.screen)
        Label(master= self.screen, textvariable=v, width=200, pady = 100).pack()
        self.back_button = Button(self.screen, text='Go back',
            command = self.screen.destroy)
        self.back_button['state'] = DISABLED
        self.back_button.pack()
        bpm = str(int(self.ser.read(6).decode('utf-8')))
        v.set("Your heart rate is " + bpm + " beats per minute")
        self.back_button['state'] = NORMAL
        self.screen.mainloop()
