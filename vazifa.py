# 1-masalal sql

# create database Online_shop;

import psycopg2

try:
    connection = psycopg2.connect(
        database="online_shop",
        user="postgres",
        password="shaxboz7116",
        host="127.0.0.1",
        port="5432")
    print("connected")
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """drop table if exists users;
            CREATE table users(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                last_name VARCHAR(255),
                reg_date date,
                age int
            );"""
        )
        print("Table created")
    
    with connection.cursor() as cursor:
        cursor.execute(
            """alter table users rename column name to first_name
            ;""")
        print("Column renamed")

    with connection.cursor() as cursor:
        cursor.execute(
            """alter table users add column adress varchar(255);""")
        print("Column added")

    with connection.cursor() as cursor:
        cursor.execute(
            """alter table users alter column reg_date type timestamp;""")
        print("Column type changed")

    with connection.cursor() as cursor:
        cursor.execute(
            """insert into users (first_name, last_name, age, adress) 
            values('Anvar', 'Ganiyev', 25, 'Fargona'), ('Madina', 'Muminova', 25, 'Fargona'), ('Akmal', 'Ruziyev', 25, 'Fargona');""")
        print("Data inserted")

    with connection.cursor() as cursor:
        cursor.execute(
            """select * from users where last_name like '%a';""")
        print("Done")

    with connection.cursor() as cursor:
        cursor.execute(
            """update users set age = 1 where age = 0;""")
        print("Done")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """delete from users where adress is not null;""")
    #     print("Done")

except Exception as e:
    print(e)
finally:
    if connection:
        connection.close()
        print("Connection is closed")