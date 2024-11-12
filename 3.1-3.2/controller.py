#comtroller.py
from view import PatientView,PatientsListView
from model import Patients_DB

class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.model.add_observer(self)

    def fetch_data(self):
        data = self.model.get_data_from_db()  # Получаем данные из базы данных
        self.view.update_data(data)  # Обновляем представление с новыми данными

    def open_add_patient_window(self):
        patient_controller = PatientController(self.model)#,self.controller)  # Создаём контроллер для нового окна
        PatientView(self.view.window, patient_controller)  # Создаём окно с контроллером

    def open_patients_list_window(self):
        patients_list_controller = PatientsListController(self.model)#,self.controller)  # Создаём контроллер для списка пациентов
        PatientsListView(self.view.window, patients_list_controller)   # Создаём окно для просмотра пациентов

        # -------------------------------сделать ссылку на другие конторллеры---------------------------------------------
    #def add_patient(self, patient_data):
       #return self.model.add_patient(patient_data)
    #def get_patients(self):
        #return self.model.get_data_from_db()  # Получаем список пациентов из модели

    #def update(self, data):
        # Обновляем данные в представлении, когда модель уведомляет об изменениях
        #self.view.update_data(data)
class PatientController:
    def __init__(self, model,controller):
        self.model = model
        self.controller = controller
    def add_patient(self, patient_data):
        return self.model.add_patient(patient_data)

class PatientsListController:
    def __init__(self, model,controller):
        self.model = model
        self.controller = controller

        def get_patients(self):
            return self.model.get_data_from_db()  # Получаем список пациентов из модели

        def update(self, data):
            self.view.update_data(data) # Обновляем данные в представлении, когда модель уведомляет об изменениях


