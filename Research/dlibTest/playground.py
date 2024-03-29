# from utils.SDCalculator import SDCalculator
# from utils.RTPlotter import RTPlotter

# sd_calculator = SDCalculator()
# rt_plotter = RTPlotter()

from utils.GraphPlotter import GraphPlotter

graph_plotter = GraphPlotter(yRange=[0, 25])

graph_plotter.show_graph()
graph_plotter.add_plot("exampleOne", title="Example One")
graph_plotter.add_plot("exampleTwo", title="Example Two")
yValue = 1

while True:
    graph_plotter.input_value("exampleOne", yValue)
    graph_plotter.input_value("exampleTwo", yValue * 2)
    yValue = yValue + 0.1
    # print("Current Value: {}".format(yValue))
    if yValue >= 10:
        yValue = 1      