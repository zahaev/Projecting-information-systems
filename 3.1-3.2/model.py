# model.py
import psycopg2
from psycopg2 import extras


class Patients_DB:
    def __init__(self, host, user, password, database):
        self._observers = []
        self._data = []
        try:
            self.conn = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                dbname=database
            )
            print("Подключение к базе данных было успешным")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    # def set_data(self, data):
    # self._data = data
    # self.notify_observers()

    def get_data_from_db(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT Name, Date_of_birth, Email, Address, Phone FROM Patients")
                self._data = cursor.fetchall()
                return self._data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []  # Возвращаем пустой список в случае ошибки

    def add_patient(self, patient_data):
        try:
            with self.conn.cursor() as cursor:
                query = "INSERT INTO Patients (Name, Date_of_birth, Email, Address, Phone) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, patient_data)  # Передаем кортеж данных
                self.conn.commit()  # Не забудьте зафиксировать изменения
                print("Пациент добавлен успешно")
                return True  # Успешное добавление
        except Exception as e:
            print(f"Error adding patient: {e}")

    def delete_patient(self, patient_data):
        try:
            with self.conn.cursor() as cursor:
                query = "DELETE FROM Patients WHERE Name = %s AND Date_of_birth = %s AND Email = %s AND Address = %s AND Phone = %s"
                cursor.execute(query, (
                    patient_data['name'], patient_data['dob'], patient_data['email'], patient_data['address'],
                    patient_data['phone']))
                self.conn.commit()
                print("Пациент удален успешно")
                self.get_data_from_db()  # Обновляем данные после удаления
                return True
        except Exception as e:
            print(f"Error deleting patient: {e}")
            return False

    def close(self):
        if self.conn:
            self.conn.close()
