#Celcius conversion
#celcius
print("\nCelcius conversion\n")
celcius = float(input('input temperature on celcius :  '))
print("The temperature in celcius is : ", celcius, "Celcius")
# reamur
reaumur = (4/5) * celcius
print("The temperature in reamur is : ",reaumur, "Reaumur")
# fahrenheit
fahrenheit  = ( celcius * 9 / 5 ) +  32
print("The temperature in fahrenheit is : ", fahrenheit, "fahrenheit")
#kelvin
kelvin = celcius + 237
print("The temperature in kelvin is: ", kelvin, "kelvin")
