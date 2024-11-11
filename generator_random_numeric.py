# Выполнил: Мальцев Георгий Павлович


import logging
import random


logging.basicConfig(level=logging.INFO, filename="py_log_2.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')



def random_generator(a: int, b: int):
    while True:
        try:
            if a < 0:
                logging.warning('Кто-то использует магию вне Хогвартса!')
                raise ValueError('Используется отрицательное число!')
            rn = random.randint(a, b)
        except ValueError:
            print('Неверные границы')
            logging.info('Используйте другие границы')
            raise ValueError
            break
        except Exception:
            print("Атстой")
            logging.error("Что-то пошло не так :(")
            break
        else:
            return rn
            logging.info("Получилось!")
            break

