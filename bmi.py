#!/usr/local/bin/python3.8

# BMI formula BMI=(weight in kg/heigt in meters square)

def gather_info():
    height = float(input("what is your hight? (inches or meters) "))
    weight = float(input("what is your weight? (pound or kilograms) "))
    system = input("are you measuremets in metric or imperial units? ").lower().strip()
    return(height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the body mass index for the given weight height ad measurement system
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system. startswith('i'):
        bmi = calculate_bmi(weight, system=system, height=height)
        print(f"your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        print(f"your BMI is {bmi}")
        break
    else:
        print("Error: unknown measurment system. Please use imperial or metric system.")

