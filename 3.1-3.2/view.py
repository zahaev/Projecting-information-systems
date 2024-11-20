#view.py
import tkinter as tk
from tkinter import messagebox


class MainView:
    def __init__(self, window):
        self.window = window
        window.title("Главное окно")
        window.geometry('400x250')

        self.label = tk.Label(window, text="Данные:")


        self.add_patient_button = tk.Button(window, text="Добавить пациента", command=self.open_add_patient_window)
        self.add_patient_button.pack(pady=10)

        self.view_patients_button = tk.Button(window, text="Просмотр списка пациентов", command=self.open_patients_list_window)
        self.view_patients_button.pack(pady=10)

    def set_controller(self, controller):
        self.controller = controller

    def update_data(self, data):
        self.label.config(text=f"Данные: {data}")  # Используем config для обновления текста

    def open_add_patient_window(self):
        from controller import PatientController  # Импорт внутри метода
        patient_controller = PatientController(self.controller.model, self.controller)  # Создаём контроллер для добавления пациента
        PatientView(self.window, patient_controller)  # Передаём контроллер в вид

    def open_patients_list_window(self):
        from controller import PatientsListController  # Импорт внутри метода
        patients_list_controller = PatientsListController(self.controller.model, self.controller,self)  # Создаём контроллер для списка пациентов
        PatientsListView(self.window, patients_list_controller)  # Передаём контроллер в вид

class PatientView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить пациента")

        tk.Label(self.window, text="Имя:").pack(pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack(pady=5)

        tk.Label(self.window, text="Дата рождения (DD-MM-YYYY):").pack(pady=5)
        self.dob_entry = tk.Entry(self.window)
        self.dob_entry.pack(pady=5)

        tk.Label(self.window, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.window)
        self.email_entry.pack(pady=5)

        tk.Label(self.window, text="Адрес:").pack(pady=5)
        self.address_entry = tk.Entry(self.window)
        self.address_entry.pack(pady=5)

        tk.Label(self.window, text="Телефон:").pack(pady=5)
        self.phone_entry = tk.Entry(self.window)
        self.phone_entry.pack(pady=5)

        add_button = tk.Button(self.window, text="Добавить", command=self.add_patient)
        add_button.pack(pady=10)

    def add_patient(self):
        patient_data = (
            self.name_entry.get(),
            self.dob_entry.get(),
            self.email_entry.get(),
            self.address_entry.get(),
            self.phone_entry.get()
        )
        if self.controller.add_patient(patient_data):  # Вызываем метод add_patient контроллера
            messagebox.showinfo("Успех", "Пациент добавлен успешно!")
            self.window.destroy()  # Закрываем окно после добавления
            self.controller.controller.fetch_data()  # Обновляем данные в главном контроллере
        else:
            messagebox.showerror("Ошибка", "Не удалось добавить пациента.")

class PatientsListView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.window = tk.Toplevel(parent)
        self.window.title("Список пациентов")

        self.listbox = tk.Listbox(self.window, width=60, height=20)
        self.listbox.pack(pady=10)

        self.update_button = tk.Button(self.window, text="Обновить", command=self.update_list)
        self.update_button.pack(pady=5)

        self.close_button = tk.Button(self.window, text="Закрыть", command=self.window.destroy)
        self.close_button.pack(pady=5)

        self.update_list()  # Изначально обновляем список при открытии окна

    def update_list(self):
        self.listbox.delete(0, tk.END)  # Очищаем список
        patients = self.controller.get_patients()  # Вызываем метод get_patients контроллера
        if not patients:
            messagebox.showinfo("Информация", "Нет доступных пациентов.")
        else:
            for patient in patients:
                self.listbox.insert(tk.END, f"{patient[0]}, {patient[1]}, {patient[2]}, {patient[3]}, {patient[4]}")  # Добавляем пациентов в список
