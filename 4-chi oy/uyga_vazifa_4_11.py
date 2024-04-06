import psycopg2
from prettytable import PrettyTable
table = PrettyTable()
conn = psycopg2.connect(dbname='uyga_vazifa_4_9',
                            host='localhost', port='5432', user='postgres', password='20021002')
curr = conn.cursor()
#1
def print_table(data, headers):
    table.field_names = headers
    for i in data:
        table.add_row(i)
    print(table)

# data = [
#     ['Jahongir', 'Vohidov', 19],
#     ['Bekjon', 'Zokirov', 21],
#     ['Malika', 'Jamilova', 23]
# ]
#
# headers = ['Name', 'Surname', "Age"]
#
# print_table(data, headers)

#2
def write_table__file(data, headers, new_file):
    table.field_names = headers
    for i in data:
        table.add_row(i)

    with open(new_file, "w") as file:
        file.write(str(table))

# data = [
#     ['Sirojidin', 'Abdusattorov', 'Fizika', 34],
#     ['Addusattor', 'Jamilov', 'Tarix', 35],
#     ['Adror', 'Ziyoyev', 'Kimyo', 40]
# ]
# headers = ['Name', 'Surname', "Subject", 'Age']
# write_table__file(data, headers, 'new_file.txt')

#3
def create_new_table_from_txt(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    headers = [i.strip() for i in lines[0].split(',')]
    del lines[0]
    data = [i.strip().split(',') for i in lines]
    table.field_names = headers
    for i in data:
        table.add_row(i)
    return table
# file_name = 'new_file.txt'
# table = create_new_table_from_txt(file_name)
# print(table)

#4
def insert_function(table_name):

    table_name1 = input('Table nomini kiriting: ')
    curr.execute(f'select *from {table_name}')
    c_name = [i[0] for i in curr.description]
    input_data = [input(f'{i} ni kiriting: ') for i in c_name]
    curr.execute(f"insert into {table_name} values {tuple(input_data)}")

#5
def create_new_table_txt(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    headers = [i.strip() for i in lines[0].split(',')]
    del lines[0]
    data = [i.strip().split(',') for i in lines]
    table.field_names = headers
    for i in data:
        table.add_row(i)
    return table

file_name = 'new_file.txt'
create_new_table_txt(file_name)
print(table)









