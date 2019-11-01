import matplotlib.pyplot as plt
import numpy

plt.style.use("ggplot")


class RTPlotter:

    def __init__(self, pauseTime: float = 0.01, title="Title"):
        # TODO: Initialization work

        self.pause_time = pauseTime
        self.x_vec = numpy.linspace(0, 1, 101)[0: -1]
        self.y_vec = [0] * len(self.x_vec)

        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        self.line1, = ax.plot(self.x_vec, self.y_vec, '-o', alpha=0.8)
        plt.ylabel("value")
        plt.title(title)

        self.fig = fig

    def show_graph(self):
        plt.show()

    def input_value(self, value: float):
        self.y_vec[-1] = value
        self.line1.set_ydata(self.y_vec)
        if numpy.min(self.y_vec) <= self.line1.axes.get_ylim()[0] or numpy.max(self.y_vec) >= self.line1.axes.get_ylim()[1]:
            self.fig.ylim(
                [numpy.min(self.y_vec) - numpy.std(self.y_vec), numpy.max(self.y_vec) + numpy.std(self.y_vec)])
        self.y_vec = numpy.append(self.y_vec[1:], 0.0)
        plt.pause(self.pause_time)
        # print("Y_Vec: {}".format(self.y_vec))
