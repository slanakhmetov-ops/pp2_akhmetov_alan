import csv
from connect import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS phonebook (name TEXT, phone TEXT);")
    conn.commit()
    conn.close()

def insert_from_csv():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook") 

    with open("contacts.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook VALUES (%s, %s)", row)

    conn.commit()
    conn.close()

def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook VALUES (%s, %s)", (name, phone))
    conn.commit()
    conn.close()

def update_contact():
    choice = input("1-change name 2-change phone: ")
    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        phone = input("Phone: ")
        new_name = input("New name: ")
        cur.execute("UPDATE phonebook SET name=%s WHERE phone=%s", (new_name, phone))
    elif choice == "2":
        name = input("Name: ")
        new_phone = input("New phone: ")
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, name))

    conn.commit()
    conn.close()

def query_contacts():
    key = input("Search: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name LIKE %s OR phone LIKE %s",
                (f"%{key}%", f"{key}%"))
    for row in cur.fetchall():
        print(row)
    conn.close()

def delete_contact():
    val = input("Name or phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name=%s OR phone=%s", (val, val))
    conn.commit()
    conn.close()

create_table()

while True:
    print("\n1-csv 2-add 3-update 4-search 5-delete 0-exit")
    c = input("> ")
    if c=="1": insert_from_csv()
    elif c=="2": insert_from_console()
    elif c=="3": update_contact()
    elif c=="4": query_contacts()
    elif c=="5": delete_contact()
    elif c=="0": break