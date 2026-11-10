import mysql.connector


class Product:
    def _conectar(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="login_system_db"
        )

    def obtener_todos(self):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id_product, nombre, precio, stock FROM products")
        filas = cursor.fetchall()
        conn.close()
        return filas

    def agregar(self, nombre, precio, stock):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (nombre, precio, stock) VALUES (%s, %s, %s)",
            (nombre, precio, stock)
        )
        conn.commit()
        conn.close()