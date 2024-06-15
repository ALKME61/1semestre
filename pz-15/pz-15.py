# Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии,
# которая обеспечивает обработку анкетных данных абитуриентов. Таблица Анкета
# содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя,
# Отчество, Дата Рождения, Награды (наличие кр. Диплома или медали (да/нет)), Адрес,
# выбранная Специальность.

import sqlite3 as sq

infoStudents=[
    (1, 'Эль Кадри', 'Каримчик', 'Рафикович', '02-11-2005', True, 'г.Бейрёт', 'Программист'),
    (2, 'Савелиев', 'Даниил', 'Пуджович', '31-10-2006', False, 'г.Аксай', 'Программист'),
    (3, 'Мышняков', 'Максим', 'Аликсеевич', '27-03-2006', True, 'г.Санкт-Петербург', 'Кассир'),
    (4, 'Канкарко', 'Магиянток', 'Иванович', '02-02-2006', False, 'г.Новошахтинкс', 'Системный администратор'),
    (5, 'Сиртакич', 'Монте', 'Варье', '14-03-2007', True, 'г.Ростов-на-Дону', 'Бухгалтер'),
    (6, 'Мамываев', 'Маприт', 'Киркововчич', '07-10-2006', True, 'х.Победа', 'Программист'),
    (7, 'Марзимян', 'Азул', 'Эбекович', '28-12-2005', False, 'г.Азов', 'Связист'),
    (8, 'Капрон', 'Раприм', 'Кертаков', '21-08-2006', False, 'г.Пекин', 'Программист'),
    (9, 'марко', 'Кенротв', 'Таприч', '17-09-2007', True, 'г.Ростов-на-Дону', 'Бухгалтер'),
]

with sq.connect('pz-15/saper.db') as con:
    cur=con.cursor()
    cur.execute(
        "DROP TABLE IF EXISTS students"
        )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS students("
        "reg_n INTEGER PRIMARY KEY AUTOINCREMENT,"
        "second_name TEXT NOT NULL,"
        "first_name TEXT NOT NULL,"
        "patron TEXT NOT NULL,"
        "bth_date DATE NOT NULL,"
        "achiv BOOLEAN NOT NULL,"
        "address TEXT NOT NULL,"
        "spec TEXT NOT NULL)"
        )
    
with sq.connect('pz-15/saper.db') as con:
    cur=con.cursor()
    cur.executemany("INSERT INTO students VALUES(?,?,?,?,?,?,?,?)", infoStudents)

with sq.connect('pz-15/saper.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE students SET achiv=TRUE WHERE achiv==False")
    cur.execute("SELECT * FROM students")
    result_4=cur.fetchall()
    print(result_4)

with sq.connect('pz-15/saper.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE students SET address='г.Ростов-на-Дону' WHERE address!='г.Ростов-на-Дону'")
    cur.execute("SELECT * FROM students")
    result_5=cur.fetchall()
    print(result_5)

with sq.connect('pz-15/saper.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE students SET spec='Программист' WHERE achiv==TRUE AND address=='г.Аксай' ")
    cur.execute("SELECT * FROM students WHERE spec='Программист'")
    result_6=cur.fetchall()
    print(result_6)
