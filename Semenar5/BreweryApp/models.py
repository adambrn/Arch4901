import datetime

class Employee:
    #Сотрудник
    id: int
    name: str
    surname: str
    department: str
    position: str
    salary: float

class User:
    #Пользователь директор или бухгалтер
    id: int
    login: str
    password_hash_code: int
    employee: Employee
   
class Shift:
    #Смена
    id: int
    employee: Employee
    start_time: datetime
    end_time: datetime

class ShiftSchedule:
    #График работы сотрудника
    id: int
    employee: Employee
    shifts: [Shift]

class Sensor:
    #Датчик
    id: int
    name: str
    location: str
    type: str
    model: str
    serial_number: str
    firmware_version: str
    software_version: str
 
class SensorData:
    #Данные с датчика
    id: int
    sensor: Sensor
    timestamp: datetime
    value: float

class Trigger:
    #тригерры
    id: int
    sensor: Sensor
    trigger_type: str
    trigger_value: float
    date_activation: datetime
    date_deactivation: datetime

class SensorDataCollector:
    #Коллектор данных с датчиков
    def __init__(self):
        self.sensor_data = []

    def collect_data(self, data : SensorData):
        # Сбор данных с датчиков
        self.sensor_data.append(data)

    def process_data(self):
        # Обработка данных
        pass

    def get_data(self):
        # Отобразить данные
        pass

    def add_trigger(self, trigger: Trigger):
        # Добавление триггера
        pass

    def check_triggers(self, data: SensorData):
        # Проверка триггеров и вызов соответствующих реакций
        pass

class ReportGenerator:
    @staticmethod
    def generate_director_report(shifts: [ShiftSchedule]):
        # Генерация отчета для директора на основе данных о сменах
        pass

    @staticmethod
    def generate_accounting_analysis(sensor_data: [SensorDataCollector]):
        # Генерация анализа для бухгалтерии на основе данных с датчиков
        pass


class Notification:
    message: str
    timestamp: datetime

class NotificationObserver:
    def notify(self, notification: Notification):
        # Метод, который будет вызываться при уведомлении
        pass

class NotificationSystem:
    observers: [User]
    notifications: [Notification]

    def add_observer(self, observer: User):
        # Добавление наблюдателя (получателя уведомлений)
        pass

    def remove_observer(self, observer: User):
        # Удаление наблюдателя
        pass

    def notify_observers(self, notification: Notification):
        # Уведомление всех наблюдателей
        pass

    def send_notification(self, message: Notification):
        # Создание уведомления и его отправка всем наблюдателям
        pass