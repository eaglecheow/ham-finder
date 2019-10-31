from utils.SDCalculator import SDCalculator

sd_calculator = SDCalculator()

while True:
    value = float(input("Please input value: "))

    sd_calculator.input_value(value)

    print("Current Standard Deviation: {}".format(sd_calculator.sd_value))
