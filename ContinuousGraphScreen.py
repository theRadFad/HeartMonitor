from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import datetime as dt
import matplotlib.animation as animation


class ContinuousGraphScreen:
    def __init__(self, ser, sampling_rate):
        self.ser = ser
        self.sampling_rate = sampling_rate

        #Designing the UI
        self.screen = Tk()
        self.screen.geometry('700x500')
        self.screen.resizable(width = False, height = False)
        self.screen.title('Continuous Data')

        #Adding the continuous plot
        fig = Figure()

        #Todo: should make this a function of sampling rate
        self.x = np.arange(0, 60 * self.sampling_rate)
        self.y = np.zeros(60 * self.sampling_rate)

        label = Label(self.screen,text="ECG Live Monitor").pack()

        canvas = FigureCanvasTkAgg(fig, master=self.screen)
        canvas.get_tk_widget().pack()

        ax = fig.add_subplot(111)
        self.line, = ax.plot(self.x, self.y)
        ax.set_ylim(0, 4100)
        ani = animation.FuncAnimation(fig, self.animate,
        interval= 1000 // self.sampling_rate, blit=False)

        # Displaying the window
        self.screen.mainloop()

    def animate(self, i):
        self.y = np.roll(self.y, -1)
        self.y[-1] = self.get_datapoint()
        self.line.set_ydata(self.y)  # update the data
        return self.line,

    def get_datapoint(self):
        return 10
