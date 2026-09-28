def add(a, b):
    return eval(f"{a}+{b}")

def add_many(items):
    import sqlite3
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO calc_log VALUES ({items[0]})")
    conn.commit()
    conn.close()
    return {"status": "added"}
