from connect import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("CALL upsert_user(%s, %s)", ("Nursultan", "87001239999"))

cur.execute("""
CALL insert_many_users(
    ARRAY['Timur','Ruslan','Madina','Zarina'],
    ARRAY['87001112222','87003334444','87005556666','wrong_phone'],
    NULL
)
""")

cur.execute("CALL delete_user(%s)", ("Zarina",))

cur.execute("SELECT * FROM search_phonebook(%s)", ("Ru",))
search_result = cur.fetchall()
print("Search result:", search_result)

cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (5, 0))
paginated_result = cur.fetchall()
print("Paginated result:", paginated_result)

conn.commit()
cur.close()
conn.close()