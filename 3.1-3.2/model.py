#model.py
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

    def add_observer(self, observer):
        self._observers.append(observer)

    #def remove_observer(self, observer):
      #  self._observers.remove(observer)

    def notify_observers(self):
       for observer in self._observers:
          observer.update(self._data)

    #def set_data(self, data):
       # self._data = data
       # self.notify_observers()

    def get_data_from_db(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT Name, Date_of_birth, Email, Address, Phone FROM Patients")
                self._data = cursor.fetchall()
                self.notify_observers()
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
    def close(self):
        if self.conn:
            self.conn.close()
