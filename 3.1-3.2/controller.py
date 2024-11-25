#comtroller.py
from view import PatientView,PatientsListView
from model import Patients_DB

class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.model.add_observer(self)

    
    def update(self, data)
        self.view.update_data(data) # Обновляем данные в представлении, когда модель уведомляет об изменениях

class PatientController:
    def __init__(self, model,controller):
        self.model = model
        self.controller = controller
    def add_patient(self, patient_data):
        return self.model.add_patient(patient_data)

class PatientsListController:
    def __init__(self, model,controller,view):
        self.model = model
        self.controller = controller
        self.view = view

    def get_patients(self):
        return self.model.get_data_from_db()  # Получаем список пациентов из модели



