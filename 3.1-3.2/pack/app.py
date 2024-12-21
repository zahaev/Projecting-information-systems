# main.py
from model import Database, PatientModel, DoctorModel,ServiceModel,AppointmentModel
from controller import (MainController,PatientController,PatientListController, DoctorController,DoctorListController,
                        ServiceController,ServiceListController,AppointmentController,AppointmentListController)
from view import MainView

if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': 'postgres',
        'password': 'postpass',
        'dbname': 'Patients_DB'
    }

    # Создание базы данных
    database = Database(db_config)

    # Создаем модели
    patient_model = PatientModel(database)
    doctor_model = DoctorModel(database)
    service_model = ServiceModel(database)
    app_model = AppointmentModel(database)


    # Создание контроллеров
    patient_controller = PatientController(patient_model)
    patient_list_controller = PatientListController(patient_model)
    doctor_controller = DoctorController(doctor_model)
    doctor_list_controller = DoctorListController(doctor_model)
    service_controller = ServiceController(service_model)
    service_list_controller=ServiceListController(service_model)
    app_controller = AppointmentController(app_model)
    app_list_controller = AppointmentListController(app_model)

    # Создаем экземпляр контроллера главного окна
    main_controller = MainController(patient_controller,patient_list_controller,
                                    doctor_controller,doctor_list_controller,
                                    service_controller,service_list_controller,
                                    app_controller,app_list_controller)

    # Создаем главное окно
    main_view = MainView(main_controller)

    # Передаем ссылку на главное окно контроллеру
    main_controller.set_main_view(main_view)

    # Запускаем главное окно
    main_view.run()

    # Закрываем соединение с базой данных
    database.close()
