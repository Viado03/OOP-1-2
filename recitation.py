import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=F:\Desktop\Programs\Python\Database01.accdb;')
    print("Database is Connected")

    user_id=3
    Name = 'Arvin Viado'
    Age = '18'
    Address = 'Cavite'
    Birthdate = '22/08/2003'
    SemGrade = '93'
    database = connect.cursor()
    database.execute('update Table1 set FullName=? where id=?', (Name, user_id))
    database.execute('update Table1 set Age=? where id=?', (Age, user_id))
    database.execute('update Table1 set Address=? where id=?', (Address, user_id))
    database.execute('update Table1 set Birthdate=? where id=?', (Birthdate, user_id))
    database.execute('update Table1 set SemGrade=? where id=?', (SemGrade, user_id))
    database.commit()
    print("Data is updated")

except pyodbc.Error:
    print("Error in Connection")
