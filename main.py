'''
numberOne = int(input("Ingresa el primer numero: "))
numberTwo = int(input("Ingresa el segundo numero: "))

result = numberOne + numberTwo
print(result)

numberOne = int(input("Ingresa el primer numero: "))
numberTwo = int(input("Ingresa el segundo numero: "))

result = numberOne - numberTwo
print(result)

numberOne = int(input("Ingresa el primer numero: "))
numberTwo = int(input("Ingresa el segundo numero: "))

result = numberOne * numberTwo
print(result)

numberOne = int(input("Ingresa el primer numero: "))
numberTwo = int(input("Ingresa el segundo numero: "))

result = numberOne / numberTwo
print(result)

numberOne = int(input("Ingresa el primer numero: "))
numberTwo = int(input("Ingresa el segundo numero: "))

result = numberOne % numberTwo
print(result)


opc = int(input("1. Suma \n2. Resta \n3. Multiplicacion \n4. Division \n5. Modulo \n6. Salir \nQue operacion quieres hacer? "))

while opc != 6:
    match opc:
        case 1:
            numberOne = int(input("Ingresa el primer numero: "))
            numberTwo = int(input("Ingresa el segundo numero: "))

            result = numberOne + numberTwo
            print(result)

        case 2:
            numberOne = int(input("Ingresa el primer numero: "))
            numberTwo = int(input("Ingresa el segundo numero: "))

            result = numberOne - numberTwo
            print(result)
        
        case 3:
            numberOne = int(input("Ingresa el primer numero: "))
            numberTwo = int(input("Ingresa el segundo numero: "))

            result = numberOne * numberTwo
            print(result)

        case 4:
            numberOne = int(input("Ingresa el primer numero: "))
            numberTwo = int(input("Ingresa el segundo numero: "))

            result = numberOne / numberTwo
            print(result)
        
        case 5:
            numberOne = int(input("Ingresa el primer numero: "))
            numberTwo = int(input("Ingresa el segundo numero: "))

            result = numberOne % numberTwo
            print(result)

    opc = int(input("\n1. Suma \n2. Resta \n3. Multiplicacion \n4. Division \n5. Modulo \n6. Salir \nQue operacion quieres hacer? "))

numberOne = float(input("Ingresa el primer numero: "))
numberTwo = float(input("Ingresa el segundo numero: "))
numberThree = float(input("Ingresa el tercer numero: "))

result = numberOne + numberTwo + numberThree
print(result)
'''

numbers = []
operations = []

number = int(input("Ingresa un numero: "))
numbers.append(number)

while True:
    operation = input("Ingresa una operacion (+, -, *, /): ")
    operations.append(operation)

    number = int(input("Ingresa otro numero: "))
    numbers.append(number)

    if len(numbers) >= 3:
        continuar = input("Quieres agregar otra operacion? (s/n): ")

        if continuar == "n":
            break

i = 0

while i < len(operations):
    match operations[i]:
        case "*":
            result = numbers[i] * numbers[i + 1]

            numbers[i] = result
            numbers.pop(i + 1)
            operations.pop(i)

        case "/":
            result = numbers[i] / numbers[i + 1]

            numbers[i] = result
            numbers.pop(i + 1)
            operations.pop(i)

        case _:
            i += 1

result = numbers[0]

for i in range(len(operations)):
    match operations[i]:
        case "+":
            result = result + numbers[i + 1]

        case "-":
            result = result - numbers[i + 1]

print("Resultado:", result)