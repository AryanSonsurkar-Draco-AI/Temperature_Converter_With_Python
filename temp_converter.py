def convert_temperature():
    convertor = float(input("Enter temperature value: "))

    while True:
        From_Unit = input("From unit (C/F/K): ").upper()
        if From_Unit in ["C", "F", "K"]:
            break
        else:
            print("Enter valid unit!!!")

    while True:
        To_Unit = input("To unit (C/F/K): ").upper()
        if To_Unit in ["C", "F", "K"]:
            break
        else:
            print("Enter valid unit!!!")

    if From_Unit == "C" and To_Unit == "F":
        result = (convertor * 9 / 5) + 32
        print(f"{convertor}°C = {result}°F")

    elif From_Unit == "F" and To_Unit == "C":
        result = (convertor - 32) * 5 / 9
        print(f"{convertor}°F = {result}°C")

    elif From_Unit == "C" and To_Unit == "K":
        result = convertor + 273.15
        print(f"{convertor}°C = {result}°K")

    elif From_Unit == "K" and To_Unit == "C":
        result = convertor - 273.15
        print(f"{convertor}°K = {result}°C")

    elif From_Unit == "F" and To_Unit == "K":
        result = ((convertor - 32) * 5 / 9) + 273.15
        print(f"{convertor}°F = {result}°K")

    elif From_Unit == "K" and To_Unit == "F":
        result = ((convertor - 273.15) * 9 / 5) + 32
        print(f"{convertor}°K = {result}°F")

    else:
        print("Same unit selected, no conversion needed.")


def show_examples():
    print("Here are a few conversion examples:")
    print("0°C = 32°F")
    print("32°F = 0°C")
    print("100°C = 373.15K")
    print("300K = 80.33°F")


def quick_mode():
    while True:
        print("\nQuick Conversions:")
        print("a) C → F")
        print("b) F → C")
        print("c) C → K")
        print("d) K → C")
        print("e) Back")

        choice = input("Select (a-e): ").lower()

        if choice == "e":
            break

        elif choice == "a":
            c = float(input("Enter value in C: "))
            print(f"{c}°C = {(c * 9 / 5) + 32}°F")

        elif choice == "b":
            f = float(input("Enter value in F: "))
            print(f"{f}°F = {(f - 32) * 5 / 9}°C")

        elif choice == "c":
            c = float(input("Enter value in C: "))
            print(f"{c}°C = {c + 273.15}°K")

        elif choice == "d":
            k = float(input("Enter value in K: "))
            print(f"{k}°K = {k - 273.15}°C")

        else:
            print("Invalid choice!!!")


def temperature():
    print("-------------------------------------")
    print("Temperature Converter - C <-> F <-> K")
    print("-------------------------------------")

    while True:
        print("\n1) Convert temperature")
        print("2) Show example conversions")
        print("3) Quick conversions")
        print("4) Exit")

        select = input("Select (1-4): ")

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
            print("Invalid input, please select between 1-4")


# START PROGRAM
temperature()
