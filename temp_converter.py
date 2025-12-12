def convert_temperature():
    pass

def show_examples():
    pass

def quick_mode():
    pass

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

        