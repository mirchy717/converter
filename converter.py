

print("Hello! Welcome to the unit converter!")

while True:

    kms = float(input("Enter kilometers you wish to convert: "))
    # preverimo uporabnikov vnos, saj če vnese decimalno vejico rabimo zamenjat za piko -> kms = kms.replace(",", ".") !!! ne deluje več funkcija !!!
    
    miles = kms * 0.621371

    print("{0} kilometers is {1} miles.".format(kms, miles)) # za tekstom vnesemo vse spremenljivke po vrsti - štetje se začenja z 0 ({o} se nanaša na kms, {1} se nanaša na miles)

    choice = input("Would you like to  do another conversion (y/n): ")

    if  choice.lower != "y" and choice.lower != "yes": # spremeni vse odgovore v malo tiskano
        break

