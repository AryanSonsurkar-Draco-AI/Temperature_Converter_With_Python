def convert_temperature():
    convertor = float(input("Enter temperature value: "))

    while True:    
        From_Unit = input("From unit (C/F/K): ")

        if From_Unit in ["C","F","K"]:
            break

        else :
            print("Enter Valid Unit!!!")
    while True:
        To_Unit = input("To Unit (C\F\K) : ")

        if To_Unit in ["C","F","K"]:
            break

        else:
            print("Enter valid unit!!!")

    if From_Unit == "C" and To_Unit == "F":
        result = ((convertor*9)/5) + 32
        print(f"{convertor}°C = {result}°F")

    elif From_Unit == "F" and To_Unit == "C":
        result = ((convertor - 32)*5)/9
        print(f"{convertor}°F = {result}°C")

    elif From_Unit == "C" and To_Unit == "K":
        result = convertor + 273.15
        print(f"{convertor}°C = {result}°K")

    elif From_Unit == "K" and To_Unit == "C":
        result = convertor - 273.15
        print(f"{convertor}°K = {result}°C")

    elif From_Unit == "F" and To_Unit == "K":
        step_1 = ((convertor - 32)*5)/9
        result = step_1 + 273.15
        print(f"{convertor}°F = {result}°K")

    elif From_Unit == "K" and To_Unit == "F":
        step_1 = convertor - 273.15
        result = ((step_1*9)/5) + 32
        print(f"{convertor}°K = {result}°F")

    else:
        print("Sorry! try again with correct values...")
def show_examples():
    print("Here are few conversion examples : ")
    print("0°C = 32°F")
    print("32°F = 0°C")
    print("100°C = 373.15K")
    print("300°K = 80.33°F ")

def quick_mode():
    while True:    
        print("Quick Conversions : ")
        print("a) C → F")
        print("b) F → C")
        print("c) C → K")
        print("d) K → C")
        print("e) Back")

        choice = input("Select (a-e): ")
    
        if choice == "e":
            break
        
        elif choice == "a":
            c = float(input("Enter Value in C : "))
            result = ((c*9)/5) + 32
            print(f"{c}°C = {result}°F")
            continue

        elif choice == "b":
            f = float(input("Enter Value in F : "))
            result = ((f - 32)*5)/9
            print(f"{f}°F = {result}°C") 
            continue

        elif choice == "c":
            c = float(input("Enter Value in C : "))
            result = c + 273.15
            print(f"{c}°C = {result}°K")
            continue

        elif choice == "d":
            k = float(input("Enter Value in K : "))
            result = k - 273.15
            print(f"{k}°K = {result}°C")
            continue

        else:
            print("Invalid Choice!!!")
            continue
def tempreature():
    print("-------------------------------------")
    print("Temperature Converter - C <-> F <-> K")
    print("-------------------------------------")

    while True:
        print("1) Convert temperature")
        print("2) Show example conversions")
        print("3) Quick conversions (fixed: C→F, F→C, C→K, K→C)")
        print("4) Exit")

        select = input("Select (1-4) :")
        
        if select == "1":
            convert_temperature()

        elif select == "2":
            show_examples()

        elif select == "3":
            quick_mode()
            
        elif select == "4":
            print("Good bye!!!")
            break

        else:
            print("Invalid input please select between 1-4")

        