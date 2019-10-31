import matplotlib.pyplot as plt
import numpy

plt.style.use("ggplot")

class RTPlotter:

    def __init__(self, xVec, y1Data, pauseTime: float = 0.1, title="Title"):
        # TODO: Initialization work

        self.pause_time = pauseTime

        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        self.line1 = ax.plot(xVec, y1Data, '-o', alpha=0.8)
        plt.ylabel("value")
        plt.title(title)

        self.plotter = plt

    def show_graph(self):
        self.plotter.show()


    def input_value(self, value: float):
        self.line1.set_ydata(value)
        if numpy.min(value) <= self.line1.axes.get_ylim()[0] or numpy.max(value) >= self.line1.axes.get_ylim()[1]:
            self.plotter.ylim([numpy.min(value) - numpy.std(value), numpy.max(value) + numpy.std(value)])

        self.plotter.pause(self.pause_time)
