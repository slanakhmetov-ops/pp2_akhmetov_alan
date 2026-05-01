import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="snake",
        user="postgres",
        password="12345678",
        host="127.0.0.1",
        port="5432"
    )


def get_or_create_player(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    res = cur.fetchone()

    if res:
        cur.close()
        conn.close()
        return res[0]

    cur.execute(
        "INSERT INTO players (username) VALUES (%s) RETURNING id",
        (username,)
    )
    conn.commit()
    player_id = cur.fetchone()[0]

    cur.close()
    conn.close()
    return player_id


def save_game(player_id, score, level):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)",
        (player_id, score, level)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_best_score(player_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT MAX(score) FROM game_sessions WHERE player_id=%s",
        (player_id,)
    )
    res = cur.fetchone()[0]

    cur.close()
    conn.close()
    return res or 0


# top10
def get_top10():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.username, g.score, g.level_reached, g.played_at
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        ORDER BY g.score DESC
        LIMIT 10
    """)

    data = cur.fetchall()

    cur.close()
    conn.close()
    return data