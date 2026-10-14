import psycopg
from Models.config import DatabaseConfig


class Database:
    def __init__(self, config: DatabaseConfig | None = None) -> None:
        self.config = config or DatabaseConfig()

    def connect(self) -> psycopg.Connection:
        return psycopg.connect(
            host=self.config.host,
            port=self.config.port,
            dbname=self.config.name,
            user=self.config.user,
            password=self.config.password,
        )
