while True:
    try:
        choice = input("(h)armonic, (m)ultiplication or (q)uit: ")
        if choice.lower() == "h":
            try:
                lenght = int(input("Series length: "))
                harmonic_sum = 0
                for i in range(1, lenght+1):
                    harmonic = 1 / i
                    harmonic_sum += harmonic
                    print(round(harmonic, 4))
                print("Sum of series: ", round(harmonic_sum, 4))
            except:
                print("[!] Please enter an integer value")
        elif choice.lower() == "m":
            try:
                first_int = int(input("First integer: "))
                second_int = int(input("Second integer: "))
                product = 0
                print(first_int, second_int)
                while second_int != 0:
                    if second_int % 2 != 0: # if not even
                        product += first_int
                
                    first_int = first_int + first_int
                    second_int = second_int // 2
                    if second_int == 0:
                        break
                    else:
                        print(first_int, second_int)
                print("Product:",product)
            except Exception as e:
                print(e)
        elif choice.lower() == "q":
            quit()
        else:
            print("Illegal choice!")
    except Exception as e:
        print(e)