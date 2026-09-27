from fastapi import APIRouter
import sqlite3
import requests

router = APIRouter()


@router.get("/users/{user_id}")
def get_user_profile(user_id: int):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
    user = cur.fetchone()
    conn.close()
    if not user:
        return {"error": "User not found"}, 404
    resp = requests.post("https://notify.example.com/send", json={"id": user_id})
    return {"id": user[0], "status": resp.status_code}
