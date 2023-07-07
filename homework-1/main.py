"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

#connect to bd
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='2362'
)

def customers_add_data():
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/customers_data.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # пропуск хедера
                for row in reader:
                    cursor.execute(
                        "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                        row
                    )

def employees_add_data():
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/employees_data.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) "
                        "VALUES (%s, %s, %s, %s, %s, %s)",
                        row
                    )

def orders_add_data():
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/orders_data.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # пропуск хедера
                for row in reader:
                    cursor.execute(
                        "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) "
                        "VALUES (%s, %s, %s, %s, %s)",
                        row
                    )

if __name__ == '__main__':
    employees_add_data()
    customers_add_data()
    orders_add_data()