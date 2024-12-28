import schedule
import time

# Функция, которую нужно выполнить по расписанию
def my_task():
    print("Выполняю задачу...")

# Запланировать выполнение задачи каждую минуту
<<<<<<< HEAD
schedule.every(1).seconds.do(my_task)
=======
schedule.every(1).minutes.do(my_task)
>>>>>>> fc07bdd2fcbdedbf7aa41a89c30bff15d0b2b5d9

# Цикл планирования
while True:
    schedule.run_pending()
<<<<<<< HEAD
    time.sleep(1)  # Пауза в 1 секунду
=======
    time.sleep(1)  # Пауза в 1 секунду
>>>>>>> fc07bdd2fcbdedbf7aa41a89c30bff15d0b2b5d9
