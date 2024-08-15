#sekarnag kondisi kita
# aku mau bikin menu
#
# menu 1 tambah
# menu 2 kurang
# menu 3 pembagian
# menu 4 perkalian
# menu 5 exit

# terus aku mau ada validasi kalau misalkan user ini inputnya bukan 1 - 5 dia bakal muncul pesan error
# aku mau juga selama usernya ga mencet menu 5 bakal programnya ga akan stop


#kita ga tau kapan programnya akan stop
while True:
    print(100*"\n")

    print("This Calculator Menu")
    print("1. Addition")
    print("2. Substraction")
    print("3. Divide")
    print("4. Multiplication")
    print("5. Quit")
    choice = input("Enter Your Choices : ")
    if choice not in ['1','2','3','4','5']:
        print("Invalid Choice Please input valid option")
        input("Press enter to continue")
        continue
    if choice == '5':
        print("Thank You For using Calculator")
        input("Press Enter to Exit")
        break
    operand1 = float(input("Enter your first operand : "))
    operand2 = float(input("Enter your Second operand : "))
    result = 0
    if choice == '1':
        result = operand1 + operand2
    elif choice == '2':
        result = operand1 - operand2
    elif choice == '3':
        result = operand1 / operand2
    elif choice == '4':
        result = operand1 * operand2


    print(f"The result is {int(result)}")
    input("Press Enter to Continue")
