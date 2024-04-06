import psycopg2

conn = psycopg2.connect(dbname='python_with', host='localhost', port='5432', user='postgres', password='20021002')
curr = conn.cursor()

# def students(table_name):
#     curr.execute('CREATE TABLE students(id serial primary key, name varchar(20))')
#
# conn.commit()
# conn.close()
#
# def students(table_name):
#     curr.execute(f'CREATE TABLE {table_name} (id serial primary key)')

def create_table(table_name):
    try:
        curr.execute(f'CREATE TABLE {table_name}  (id serial primary key)')
    except Exception:
        print("Bunaqa table mavjud!")
    else:
        print('Yaratildi')

def add_column(table_name, column_name, data_type, exc=''):
    try:
        curr.execute(f"AlTER Table {table_name} ADD column {column_name} {data_type} {exc}")
    except Exception as e:
        print('Xato!')
    else:
        print("DONE")

add_column('Olmahon', 'phone_number', 'varchar(12)')


#hello

conn.commit()
conn.close()
