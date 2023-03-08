DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    #Crear lista de quiene trabajan con python con list comprehensions:

    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]

    # for worker in all_python_devs:
        # print(worker)

    all_platzi_workers = [worker["name"] for worker in DATA if worker ["organization"]=="Platzi"]
    
    # for worker in all_platzi_workers:
    #     print(worker)

    all_up_18 = [worker["name"] for worker in DATA if worker ["age"]> 18]

    # for worker in all_up_18:
    #     print(worker)

    all_up_18 = list(filter(lambda worker: worker["age"] > 18, DATA))
    # print (all_up_18)

    #Con la anterior se imprime toda la data de los mayores de 18 pero necesitamos solo imprimir el nombre
    #Entonces usamos funcion lambda map
    all_up_18 = list(map(lambda worker: worker["name"], all_up_18))
    # print (all_up_18)

    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    print(old_people)


if __name__ == '__main__':
    run()