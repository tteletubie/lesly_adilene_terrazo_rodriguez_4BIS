import hashlib
import hmac
import secrets

from Models.database import Database


class AuthModel:
    def __init__(self, database: Database) -> None:
        self.database = database

    def check_database_connection(self) -> bool:
        with self.database.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
        return result == (1,)

    def authenticate(self, username: str, password: str) -> bool:
        with self.database.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT password_hash FROM users WHERE username = %s",
                    (username,),
                )
                user = cursor.fetchone()
        return user is not None and verify_password(password, user[0])

    def register_user(self, username: str, password: str) -> bool:
        username = username.strip()
        if not username or not password:
            return False

        with self.database.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT 1 FROM users WHERE username = %s",
                    (username,),
                )
                if cursor.fetchone() is not None:
                    return False

                cursor.execute(
                    "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                    (username, hash_password(password)),
                )
                connection.commit()
        return True


def hash_password(password: str, salt: bytes | None = None) -> str:
    password_salt = salt or secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), password_salt, 600_000
    )
    return f"{password_salt.hex()}:{password_hash.hex()}"


def verify_password(password: str, stored_password: str) -> bool:
    try:
        salt_hex, hash_hex = stored_password.split(":", maxsplit=1)
        expected_hash = bytes.fromhex(hash_hex)
        actual_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            bytes.fromhex(salt_hex),
            600_000,
        )
    except (ValueError, TypeError):
        return False
    return hmac.compare_digest(actual_hash, expected_hash)
