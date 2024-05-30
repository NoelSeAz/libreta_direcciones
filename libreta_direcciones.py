import pandas as pd
import sqlite3
from tabulate import tabulate

class LibretaDirecciones:
    def __init__(self):
        """Inicializa la libreta de direcciones y la conexión a la base de datos."""
        self.contactos = []
        self.conexion = sqlite3.connect('libreta_direcciones.db')
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        """Crea la tabla de contactos si no existe."""
        query = """
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            telefono TEXT NOT NULL,
            direccion TEXT NOT NULL,
            empleo TEXT NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conexion.commit()

    def buscar_contacto(self, criterio, valor):
        """Busca contactos según un criterio y valor dados.
        
        Args:
            criterio (str): El criterio de búsqueda (nombre, apellido, telefono, direccion, empleo).
            valor (str): El valor a buscar.

        Returns:
            pd.DataFrame: DataFrame con los resultados de la búsqueda.
        """
        query = f"SELECT * FROM contactos WHERE {criterio} = ?"
        self.cursor.execute(query, (valor,))
        resultados = self.cursor.fetchall()
        df = pd.DataFrame(resultados, columns=["id", "nombre", "apellido", "telefono", "direccion", "empleo"])
        return df
    
    def obtener_todos_contactos(self):
        """Obtiene todos los contactos de la libreta.
        
        Returns:
            pd.DataFrame: DataFrame con todos los contactos.
        """
        query = "SELECT * FROM contactos"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        df = pd.DataFrame(resultados, columns=["id", "nombre", "apellido", "telefono", "direccion", "empleo"])
        return df

    def agregar_contacto(self, contacto):
        """Agrega un nuevo contacto a la libreta y a la base de datos.
        
        Args:
            contacto (Contacto): El objeto contacto a agregar.
        """
        self.contactos.append(contacto)
        query = "INSERT INTO contactos (nombre, apellido, telefono, direccion, empleo) VALUES (?, ?, ?, ?, ?)"
        valores = (contacto.nombre, contacto.apellido, contacto.telefono, contacto.direccion, contacto.empleo)
        self.cursor.execute(query, valores)
        self.conexion.commit()

        # Mostrar los datos del nuevo contacto
        query = "SELECT * FROM contactos WHERE id = ?"
        self.cursor.execute("SELECT last_insert_rowid()")
        contacto_id = self.cursor.fetchone()[0]
        self.cursor.execute(query, (contacto_id,))
        resultado = self.cursor.fetchone()
        df = pd.DataFrame([resultado], columns=["id", "nombre", "apellido", "telefono", "direccion", "empleo"])
        print("\n" + tabulate(df, headers='keys', tablefmt='grid', showindex=False) + "\n")

    def modificar_contacto(self, contacto_id, nuevos_datos):
        """Modifica un contacto existente en la libreta.
        
        Args:
            contacto_id (int): El ID del contacto a modificar.
            nuevos_datos (dict): Diccionario con los nuevos datos del contacto.
        """
        set_clause = ", ".join([f"{col} = ?" for col in nuevos_datos.keys()])
        query = f"UPDATE contactos SET {set_clause} WHERE id = ?"
        valores = list(nuevos_datos.values()) + [contacto_id]
        self.cursor.execute(query, valores)
        self.conexion.commit()

        # Mostrar los datos modificados
        query = "SELECT * FROM contactos WHERE id = ?"
        self.cursor.execute(query, (contacto_id,))
        resultado = self.cursor.fetchone()
        df = pd.DataFrame([resultado], columns=["id", "nombre", "apellido", "telefono", "direccion", "empleo"])
        print("\n" + tabulate(df, headers='keys', tablefmt='grid', showindex=False) + "\n")

    def eliminar_contacto(self, contacto_id):
        """Elimina un contacto de la libreta y la base de datos.
        
        Args:
            contacto_id (int): El ID del contacto a eliminar.
        """
        query = "DELETE FROM contactos WHERE id = ?"
        self.cursor.execute(query, (contacto_id,))
        self.conexion.commit()

    def contar_contactos(self):
        """Cuenta el número total de contactos en la libreta.
        
        Returns:
            int: Número total de contactos.
        """
        query = "SELECT COUNT(*) FROM contactos"
        self.cursor.execute(query)
        total_contactos = self.cursor.fetchone()[0]
        return total_contactos

    def __del__(self):
        """Cierra la conexión a la base de datos al destruir la instancia."""
        self.cursor.close()
        self.conexion.close()
