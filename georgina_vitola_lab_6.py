if __name__ == "__main__":
    encoder = True
    while encoder == True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = (input("Please enter your password to encode: "))
            encoded_password = ""
            for i in password[0:]:
                if i == "0":
                    i = "3"
                elif i == "1":
                    i = "4"
                elif i == "2":
                    i = "5"
                elif i =="3":
                    i = "6"
                elif i == "4":
                    i = "7"
                elif i == "5":
                    i = "8"
                elif i == "6":
                    i = "9"
                elif i == "7":
                    i = "0"
                elif i == "8":
                    i = "1"
                elif i == "9":
                    i = "2"
                encoded_password += i
            print("Your password has been encoded and stored!")
            print()
        elif option == 2:
            print(f"The encoded password is {encoded_password} and the original password is {password}.")
        elif option == 3:
            encoder = False