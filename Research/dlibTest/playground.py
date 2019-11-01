from utils.SDCalculator import SDCalculator
from utils.RTPlotter import RTPlotter

sd_calculator = SDCalculator()
rt_plotter = RTPlotter()

rt_plotter.show_graph()
yValue = 1

while True:
    rt_plotter.input_value(yValue)
    yValue = yValue + 0.1
    print("Current Value: {}".format(yValue))
    if yValue >= 10:
        yValue = 1      