#!/usr/bin/python3
def bmi_app():
    height = input("How tall are you? ")
    weight = input("How weight are you? ")
    bmi_value = int(weight)/(int(height)/100)**2
    print(round(bmi_value,2))

bmi_app()
