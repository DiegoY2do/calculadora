numberOne = float(input("Ingresa el primer numero: "))
numberTwo = float(input("Ingresa el segundo numero: "))

result = numberOne + numberTwo
print("Resultado:", result)


numberOne = float(input("\nIngresa el primer numero: "))
numberTwo = float(input("Ingresa el segundo numero: "))

result = numberOne - numberTwo
print("Resultado:", result)


numberOne = float(input("\nIngresa el primer numero: "))
numberTwo = float(input("Ingresa el segundo numero: "))

result = numberOne * numberTwo
print("Resultado:", result)


numberOne = float(input("\nIngresa el primer numero: "))
numberTwo = float(input("Ingresa el segundo numero: "))

if numberTwo == 0:
    print("No se puede dividir entre 0")
else:
    result = numberOne / numberTwo
    print("Resultado:", result)


numberOne = float(input("\nIngresa el primer numero: "))
numberTwo = float(input("Ingresa el segundo numero: "))

if numberTwo == 0:
    print("No se puede realizar modulo entre 0")
else:
    result = numberOne % numberTwo
    print("Resultado:", result)


opc = int(input("\n1. Suma \n2. Resta \n3. Multiplicacion \n4. Division \n5. Modulo \n6. Salir \nQue operacion quieres hacer? "))

while opc != 6:
    match opc:
        case 1:
            numberOne = float(input("Ingresa el primer numero: "))
            numberTwo = float(input("Ingresa el segundo numero: "))

            result = numberOne + numberTwo
            print("Resultado:", result)

        case 2:
            numberOne = float(input("Ingresa el primer numero: "))
            numberTwo = float(input("Ingresa el segundo numero: "))

            result = numberOne - numberTwo
            print("Resultado:", result)

        case 3:
            numberOne = float(input("Ingresa el primer numero: "))
            numberTwo = float(input("Ingresa el segundo numero: "))

            result = numberOne * numberTwo
            print("Resultado:", result)

        case 4:
            numberOne = float(input("Ingresa el primer numero: "))
            numberTwo = float(input("Ingresa el segundo numero: "))

            if numberTwo == 0:
                print("No se puede dividir entre 0")
            else:
                result = numberOne / numberTwo
                print("Resultado:", result)

        case 5:
            numberOne = float(input("Ingresa el primer numero: "))
            numberTwo = float(input("Ingresa el segundo numero: "))

            if numberTwo == 0:
                print("No se puede realizar modulo entre 0")
            else:
                result = numberOne % numberTwo
                print("Resultado:", result)

        case _:
            print("Opcion no valida")

    opc = int(input("\n1. Suma \n2. Resta \n3. Multiplicacion \n4. Division \n5. Modulo \n6. Salir \nQue operacion quieres hacer? "))


numberOne = float(input("\nIngresa el primer numero: "))
numberTwo = float(input("Ingresa el segundo numero: "))
numberThree = float(input("Ingresa el tercer numero: "))

result = numberOne + numberTwo + numberThree
print("Resultado:", result)


numbers = []
operations = []

number = float(input("\nIngresa un numero: "))
numbers.append(number)

while True:
    operation = input("Ingresa una operacion (+, -, *, /): ")
    operations.append(operation)

    number = float(input("Ingresa otro numero: "))
    numbers.append(number)

    if len(numbers) >= 3:
        continuar = input("Quieres agregar otra operacion? (s/n): ")

        if continuar == "n":
            break

i = 0
error = False

while i < len(operations):
    match operations[i]:
        case "*":
            result = numbers[i] * numbers[i + 1]

            numbers[i] = result
            numbers.pop(i + 1)
            operations.pop(i)

        case "/":
            if numbers[i + 1] == 0:
                print("No se puede dividir entre 0")
                error = True
                break

            result = numbers[i] / numbers[i + 1]

            numbers[i] = result
            numbers.pop(i + 1)
            operations.pop(i)

        case _:
            i += 1

if error == False:
    result = numbers[0]

    for i in range(len(operations)):
        match operations[i]:
            case "+":
                result = result + numbers[i + 1]

            case "-":
                result = result - numbers[i + 1]

    print("Resultado:", result)