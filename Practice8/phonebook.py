from connect import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT * FROM search_phonebook(%s)", ("Al",))
search_result = cur.fetchall()
print("Search:", search_result)


cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (5, 0))
paginated_result = cur.fetchall()
print("Paginated:", paginated_result)

conn.commit()
cur.close()
conn.close()