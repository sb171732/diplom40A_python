# import pyodbc;

# msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
# print(msa_drivers)
import pyodbc
conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Admin\\Documents\\40A\\diplom40A_python\\bd.accdb;')
cursor = conn.cursor() # создается курсор

# cursor.execute("insert into users(user_name, chat_id) values('Тест', 1223)")
# cursor.commit()

cursor.execute("select *from users")
for string in cursor.fetchall():
  print(string)  # Выводятся строки базы данных.
