import psycopg2


conn = psycopg2.connect(dbname='uyga_vazifa_4_9',
host='localhost', port='5432', user='postgres', password='20021002')
curr = conn.cursor()

#1
# def create_table(table_name):
#     try:
#         curr.execute(f"CREATE TABLE {table_name} (id bigserial primary key, name varchar(50), surname varchar(50), age int)")
#     except Exception:
#         print("Bunaqa table mavjud!")
#     else:
#         print('Yaratildi')
#
# create_table('student')

#2
# def drop_table(table_name):
#     try:
#         curr.execute(f"DROP TABLE {table_name}")
#     except Exception:
#         print("Bunaqa table mavjud emas!")
#     else:
#         print("O'chirildi")
#
# drop_table('student')

#3
# def add_column(table_name, column_name, data_type, exc=''):
#     try:
#         curr.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type} {exc}")
#     except Exception as e:
#         print(f"Xato malumot kiritildi!\n{e}")
#     else:
#         print('Done')
#
# add_column('users', "phone_namber", "VARCHAR(30)")

#4
# def drop_column(table_name, column_name):
#     try:
#         curr.execute(f"ALTER TABLE {table_name} DROP COLUMN {column_name}")
#     except Exception:
#         print(f"Qator mavjud emas!")
#     else:
#         print("Bajarildi")
#
# drop_column("users", "phone_namber")

#5
# def rename_column(table_name, old_column_name, new_column_name):
#     try:
#         curr.execute(f"ALTER TABLE {table_name} RENAME COLUMN {old_column_name} TO {new_column_name}")
#     except Exception as e:
#         print(f'Xatolik!\n{e}')
#     else:
#         print("Bajarildi!")
#
# rename_column("users", 'name', "name2")

#6
# def change_column_type(table_name, column_name, new_data_type):
#     try:
#         curr.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name}_temp {new_data_type}")
#         curr.execute(f"UPDATE {table_name} SET {column_name}_temp = CAST({column_name} AS {new_data_type})")
#         curr.execute(f"ALTER TABLE {table_name} DROP COLUMN {column_name}")
#         curr.execute(f"ALTER TABLE {table_name} RENAME COLUMN {column_name}_temp TO {column_name}")
#     except Exception as e:
#         print(f"O'zgartirib bo'lmadi!\n{e}")
#     else:
#         print("O'zgartirildi!")
#
# change_column_type("users", 'age', "bigint")

#7
# def insert_data(table_name, name, surname, age):
#     try:
#         curr.execute(f"INSERT INTO {table_name} (name, surname, age) VALUES (?, ?, ?)", (name, surname, age))
#     except Exception as e:
#         print(f'Xatolik!\n{e}')
#     else:
#         print("Bajarildi!")
#
# insert_data("users", "Johon", "Karimov", 19)

#8
# def insert_data(table_name, id, new_name, new_surname, new_age):
#     try:
#         curr.execute(f"UPDATE {table_name} SET name=?, surname=?, age=? WHERE id=?", (new_name, new_surname, new_age, id))
#
#     except Exception as e:
#         print(f'Xatolik!\n{e}')
#     else:
#         print("Bajarildi!")
#
# insert_data("users", 1, "Johon", "Karimov", 19)

#9
# def rename_table(old_table_name, new_table_name):
#     try:
#         curr.execute(f"ALTER TABLE {old_table_name} RENAME TO {new_table_name}")
#
#     except Exception as e:
#         print(f'Xatolik!\n{e}')
#     else:
#         print("Bajarildi!")
#
# rename_table('users', 'users1')
conn.commit()
conn.close()