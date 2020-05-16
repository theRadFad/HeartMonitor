from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import datetime as dt
import matplotlib.animation as animation
from threading import Timer


class ContinuousGraphScreen:
    def __init__(self, ser, sampling_rate):
        self.ser = ser
        self.sampling_rate = sampling_rate
        self.data_chunk = sampling_rate // 5

        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        self.ser.write(b'b')
        Timer(60, self.stop).start()

        #Designing the UI
        self.screen = Tk()
        self.screen.geometry('700x600')
        self.screen.resizable(width = False, height = False)
        self.screen.title('Continuous Data')
        self.back_button = Button(self.screen, text='Go back',
            command = self.screen.destroy)
        self.back_button['state'] = DISABLED

        #Adding the continuous plot
        fig = Figure()

        self.x = np.arange(0, 10 * self.sampling_rate)
        self.y = np.zeros(10 * self.sampling_rate)

        label = Label(self.screen,text="ECG Live Monitor").pack()

        canvas = FigureCanvasTkAgg(fig, master=self.screen)
        canvas.get_tk_widget().pack()

        ax = fig.add_subplot(111)
        self.line, = ax.plot(self.x, self.y)
        ax.set_ylim(0, 4100)
        self.ani = animation.FuncAnimation(fig, self.animate,
        interval= 200, blit=False)

        #Adding the buttons
        self.back_button.pack()

        # Displaying the window
        self.screen.mainloop()

    def animate(self, i):
        self.y = np.roll(self.y, - self.data_chunk)
        self.y[-self.data_chunk:] = self.get_datapoint()
        self.line.set_ydata(self.y)  # update the data
        return self.line,

    def get_datapoint(self):
        return self.ser.read(6 * self.data_chunk).decode('utf-8').split('\r\n')[:-1]
        
    def stop(self):
        self.ani.event_source.stop()
        self.back_button['state'] = NORMAL
