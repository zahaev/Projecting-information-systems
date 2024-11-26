#controller.py
from view import PatientView,PatientsListView
from model import Patients_DB
from datetime import datetime
import re
class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

   
    def update(self, data)
        data = self.model.get_data_from_db()
        self.view.update_data(data) # Обновляем данные в представлении, когда модель уведомляет об изменениях

class PatientController:
    def __init__(self, model,controller,view):
        self.model = model
        self.controller = controller
        self.view=view
    def add_patient(self,name,dob,email,address,phone):
        try:
            self.__validate_patient_name(name)
            self.__validate_date_of_birth(dob)
            self.__validate_email(email)
            self.__validate_phone_number(phone)
            patient_data = {
                'name': name,
                'dob': dob,
                'email': email,
                'address': address,
                'phone': phone
            }
            # Если данные валидны, добавляем пациента в модель
            self.model.add_patient(patient_data)
            self.view.update_data(patient_data)  # Обновляем список в представлении

        except ValueError as e:# Отображаем сообщение об ошибке
            self.controller.view.show_error(str(e))


    # Методы валидации
    def __validate_patient_name(self, name):
        if isinstance(name, str) and name.isalpha():
            return True
        raise ValueError("Некорректное ФИО.")


    def __validate_date_of_birth(self, date_of_birth):
        try:
            datetime.strptime(date_of_birth, '%Y-%m-%d')
            return True
        except ValueError:
            raise ValueError("Дата рождения должна быть в формате ГГГГ-ММ-ДД.")

    def __validate_email(self, email):
        pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(pattern_email, email):
            return True

        raise ValueError("Некорректный email.")
    def __validate_phone_number(self, phone_number):
        pattern = r'^\+?\d{10,15}$'
        if re.match(pattern, phone_number):
            return True

        raise ValueError("Некорректный номер телефона.")

class PatientsListController:
    def __init__(self, model,controller,view):
        self.model = model
        self.controller = controller
        self.view = view

    def get_patients(self):
        return self.model.get_data_from_db()  # Получаем список пациентов из модели
    def delete_patient(self,patient_data):
        self.model.delete_patient(patient_data)

