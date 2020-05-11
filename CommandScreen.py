from tkinter import *
from ContinuousGraphScreen import ContinuousGraphScreen

class CommandScreen:
    def __init__(self, ser):
        self.ser = ser
        self.sampling_rate = 20

        #Designing the UI
        self.screen = Tk()
        self.screen.geometry('400x250')
        self.screen.resizable(width = False, height = False)
        self.screen.title('Commands Panel')

        self.sampling_rate_entry = Entry(self.screen)
        self.sampling_rate_entry.grid(row = 1, column = 2)
        self.sampling_rate_entry.insert(END, 10)

        rate_button = Button(self.screen, text='Set Sampling Rate',
            command = self.set_sampling_rate)
        rate_button.grid(row = 2, column = 2)

        data_button = Button(self.screen, text='Collect one minute of data',
            command = self.get_minute_data)
        data_button.grid(row = 3, column = 2, padx = 120, pady = 15)

        bpm_button = Button(self.screen, text='Get BPM reading',
            command = self.get_bpm)
        bpm_button.grid(row = 4, column = 2, padx = 120, pady = 15)

        # Displaying the window
        self.screen.mainloop()

    def get_bpm(self):
        self.ser.write(b'a')

    def get_minute_data(self):
        ContinuousGraphScreen(self.ser, self.sampling_rate)

    def set_sampling_rate(self):
        try:
            selected_rate = int(self.sampling_rate_entry.get())
            if selected_rate > 1:
                self.sampling_rate = selected_rate
                self.ser.write(('c' + self.sampling_rate_entry.get() + 'c').encode('utf-8'))
            else:
                print("Cannot set non-positive sampling rate")
        except:
            print("Error in setting sampling rate")
            return
