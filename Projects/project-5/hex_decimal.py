def main():
    stop = False
    while stop != True:
        try:
            display_menu()
            choice = input("Enter option: ").lower()
            if choice == "d":
                dec_num = int(input("Decimal number: "))
                print("The hex is", decimal_to_hex_str(dec_num))
            elif choice == "h":
                hex_num = input("Hex number: ")
                print("The decimal is", hex_str_to_decimal(hex_num))
            elif choice == "x":
                stop = True
            else:
                print("Invalid option!")
                # If none of the above choices match, print the error and continue execution

        except Exception as e:
            print(e)

def decimal_to_hex_str(dec_int):
    return ''.join('{:X}'.format(dec_int)) # Return the decimal in a hex format

def hex_str_to_decimal(hex_str):
    try:
        return int(hex_str, 16) # Return the hex string in a decimal format
    except ValueError:
        return None

def display_menu():
    print("\nd. Decimal to hex\nh. Hex to decimal\nx. Exit\n") # Display a choice menu




# Main program starts here
if __name__ == "__main__":
    main()