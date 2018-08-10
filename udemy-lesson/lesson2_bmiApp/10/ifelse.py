#!/usr/bin/python3
def bmi_app():
    height = input('How tall are you? ')
    weight = input('How weight are you? ')
    bmi_value = int(weight)/(int(height)/100)**2
    print('test' + round(bmi_value,2))

    if bmi_value < 18 :
        print("You're too slim !")
    elif bmi_value >= 18 and bmi_value <= 24 :
        print("Godd job !")
    else :
        print("You're too fat !")

bmi_app()