def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
        num = input("ingresa un numero: ")
        assert num.isnumeric(), "Debes ingresar un numero entero positivo"
        assert int(num) > 0, "El numero debe ser positivo"
        print(divisors(int(num)))
        print("Termino mi programa...")

if __name__ == '__main__':
    run()