import numpy

class DataCalculator:
    
    def __init__(self, dataSize: int = 5, startingValue: float = 0):
        self.raw_data = [startingValue] * dataSize

    def calculate_standard_deviation(self):
        self.sd_value = numpy.std(self.raw_data, ddof=1)

    def calculate_variance(self):
        self.variance_value = numpy.var(self.raw_data, ddof=1)

    def calculate_mean_value(self):
        self.mean_value = numpy.mean(self.raw_data)

    def calculate_median_value(self):
        self.median_value = numpy.median(self.raw_data)

    def input_value(self, value: float):
        self.raw_data.pop()
        self.raw_data.insert(0, value)
        self.calculate_standard_deviation()
        self.calculate_mean_value()
        self.calculate_median_value()
        self.calculate_variance()

    