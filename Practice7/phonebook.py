import csv
from connect import get_connection


def create_table():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS phonebook (name TEXT, phone TEXT);")
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("DB error:", e)


def insert_from_csv():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM phonebook")

        with open("contacts.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) != 2:
                    continue
                cur.execute("INSERT INTO phonebook VALUES (%s, %s)", row)

        conn.commit()
        cur.close()
        conn.close()
        print("CSV loaded")

    except FileNotFoundError:
        print("contacts.csv not found")
    except Exception as e:
        print("Error:", e)


def insert_from_console():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()

    if not name or not phone:
        print("Empty input!")
        return

    if not phone.isdigit():
        print("Phone must be numbers")
        return

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO phonebook VALUES (%s, %s)", (name, phone))
        conn.commit()
        cur.close()
        conn.close()
        print("Contact added")
    except Exception as e:
        print("Error:", e)


def update_contact():
    choice = input("1-change name 2-change phone: ").strip()

    try:
        conn = get_connection()
        cur = conn.cursor()

        if choice == "1":
            phone = input("Phone: ").strip()
            new_name = input("New name: ").strip()

            if not phone or not new_name:
                print("Empty input!")
                return

            cur.execute("UPDATE phonebook SET name=%s WHERE phone=%s", (new_name, phone))

        elif choice == "2":
            name = input("Name: ").strip()
            new_phone = input("New phone: ").strip()

            if not name or not new_phone:
                print("Empty input!")
                return

            if not new_phone.isdigit():
                print("Phone must be numbers")
                return

            cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, name))

        else:
            print("Invalid choice")
            return

        if cur.rowcount == 0:
            print("Not found")
        else:
            print("Updated")

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print("Error:", e)


def query_contacts():
    key = input("Search: ").strip()

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM phonebook WHERE name LIKE %s OR phone LIKE %s",
            (f"%{key}%", f"{key}%")
        )

        results = cur.fetchall()

        if not results:
            print("No results")
        else:
            for row in results:
                print(row)

        cur.close()
        conn.close()

    except Exception as e:
        print("Error:", e)


def delete_contact():
    val = input("Name or phone: ").strip()

    if not val:
        print("Empty input!")
        return

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM phonebook WHERE name=%s OR phone=%s", (val, val))

        if cur.rowcount == 0:
            print("Not found")
        else:
            print("Deleted")

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print("Error:", e)


create_table()

while True:
    print("\n1-csv 2-add 3-update 4-search 5-delete 0-exit")
    c = input("> ").strip()

    if c == "1":
        insert_from_csv()
    elif c == "2":
        insert_from_console()
    elif c == "3":
        update_contact()
    elif c == "4":
        query_contacts()
    elif c == "5":
        delete_contact()
    elif c == "0":
        break
    else:
        print("Invalid choice")