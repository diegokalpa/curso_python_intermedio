def read():
    numbers = []
    with open("archivos/numbers.txt", "r",encoding = "utf-8") as f: 
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Diego", "Miguel", "Cristian", "Marcela", "Rocío", "Mario", "Martha"]
    with open("archivos/names.txt", "a" , encoding = "utf-8") as f:
        for names in names:
            f.write(names)  #escribe el nombre
            f.write("\n")   #salto del linea 



def run():
    write()


if __name__ == '__main__':
    run()