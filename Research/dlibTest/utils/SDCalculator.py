import numpy

class SDCalculator:
    
    def __init__(self, dataSize: int = 5, startingValue: float = 0):
        self.raw_data = [startingValue] * dataSize

    def calculate_standard_deviation(self):
        self.sd_value = numpy.std(self.raw_data, ddof=1)

    def input_value(self, value: float):
        self.raw_data.pop()
        self.raw_data.insert(0, value)
        self.calculate_standard_deviation()

    