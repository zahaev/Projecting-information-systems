#app.py
import tkinter as tk
from controller import MainController,PatientController,PatientsListController
from model import Patients_DB
from view import MainView


def main():
    window = tk.Tk()

    # Здесь необходимо передать параметры подключения  
    model = Patients_DB(host='localhost', user='postgres', password='postpass', database='Patients_DB')
    view = MainView(window)
    controller = MainController(model, view)

    view.set_controller(controller)

    window.mainloop()


if __name__ == "__main__":
    main()  
