#buat kalkulator mini angap dia cuman nerima inputan +,-,*,/
# format adalah input 1 input operator dan input kedua
# print hasilnya
#
# CONTOH
# 1
# +
# 2
# result = 3

#buat calc operasi ( + ; - ; * ; /)
result = 0
operand1 = float(input("Enter your first operand : "))
operator = input("Enter you operator [+,-,*,/] : ")
# 'in' ada apakah operator ini ada diantara [+,-,*,/]
if operator not in ['*','-','+','/']:
    print("Invalid operator")
else:

    operand2 = float(input("Enter your second operand : "))
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        #inget kalau dibagi dengan 0 ini bakal error galat matematika
        if operand2 == 0:
            print("Error Division By Zero")
            exit()
        else:
            result = operand1 / operand2
    print(f"the result of {operand1} {operator} {operand2} : is {result}")

