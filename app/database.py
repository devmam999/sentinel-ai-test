import os

import psycopg


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/sentinelai_test",
)


def get_connection():
    return psycopg.connect(DATABASE_URL)


def get_user_by_id(user_id: int):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, username, email, active
                FROM users
                WHERE id = %s
                """,
                (user_id,),
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return {
                "id": row[0],
                "username": row[1],
                "email": row[2],
                "active": row[3],
            }

def create_user(username: str, email: str):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO users (username, email, active)
                VALUES (%s, %s, TRUE)
                RETURNING id, username, email, active
                """,
                (username, email),
            )

            row = cursor.fetchone()

            return {
                "id": row[0],
                "username": row[1],
                "email": row[2],
                "active": row[3],
            }