import connect_postgres

def print_dinos(dinos):
    HEADER = "name                 |     height | length"
    print(HEADER)
    for dino in dinos:
        dino_line = ""
        for key, value in dino.items():
            dino_line += str(value).center(15, ' ')
        print(dino_line)    


def get_dinos():
    dinos_list = []
    dinos_dict = {}
    dinos_property = []
    properties = connect_postgres.get_data("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'dinos'")
    for property in properties:
        dinos_property.append(property[0])
    dinos = connect_postgres.get_data("SELECT * FROM dinos;")
    for dino in dinos:
        dinos_dict = {}
        for index, property in enumerate(list(dino)):
            dinos_dict[dinos_property[index]] = property
        dinos_list.append(dinos_dict)
    return dinos_list


def add_dino(name, height, length):
    connect_postgres.insert_data(name, height, length)


def delete_dino(name):
    connect_postgres.delete_data(name)


def main():

    delete_dino('R')
    # add_dino('R', 101, 102)
    dinos = get_dinos()
    print_dinos(dinos)



if __name__ == "__main__":
    main()



# numbers_a = [1, 2, 3]
# print(f'a: {numbers_a}')

# numbers_b = copy.deepcopy(numbers_a)
# numbers_b = numbers_a[:]
# print(f'b: {numbers_b}')

# numbers_b.append(4)

# print(f'a: {numbers_a}')
# print(f'b: {numbers_b}')