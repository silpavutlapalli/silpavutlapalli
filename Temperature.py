temperature = float(input("temperature value in degree celsius:")
choice == int((input(
     ''' choose values in specific options
1-celsius
2-fahernheit
3-kelvin                   
''')))

def get result() --> str:
   """ executes the code"""
if choice == 1:
    celsius = ((temperature - 32) * 5) / 9
return f'The temperature converted from {temperature} fahrenheit to celsius {celsius}'
if choice == 2:
    fahrenheit = (temperature * 1.8) + 32
    return f'The temperature converted from {temperature} celsius to fahrenheit {fahrenheit}'
if choice == 3:
    kelvin = temperature + 273
    return f'The temperature converted {temperature} to kelvin {kelvin}'

if 0 < choice < 4:
    print(get_result())
else:
    print('KINDLY CHOOSE ONLY OPTIONS LISTED')
