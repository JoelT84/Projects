x = input("Which temperature are you looking to convert? eg. Farenheit to celsius: ").capitalize().strip()
temp = float(input("How many degrees?: "))

def name(x):
    if "Farenheit to celsius" in x:
        result = round((temp - 32) * (5 / 9), 3)
        return result, "Celsius"
    
    if "Celsius to farenheit" in x:
        result = round(((temp * (9 / 5)) + 32), 3)
        return result, "Farenheit"
    
result, unit = name(x)

print(f"The temperature is {result} degrees {unit}")


"""
def farenheit():
    if "farenheit":
        return round(int((temp - 32) * (5 / 9), 3))

print(farenheit())
"""

