# Выполнил: Мальцев Георгий Павлович
# int(input('a: ')
import logging
import math
# from idlelib.iomenu import encoding

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def squaredd(a:int, b: int, c: int):
    while True:
        try:
            d = b ** 2 - 4 * a * c
            xf = (-b + math.sqrt(d)) / (2 * a)
            xs = (-b - math.sqrt(d)) / (2 * a)
        except ValueError:
            print('Дискриминант отрицателен - решения нет, попробуйте другие значения!')
            logging.info("Неудача, отрицательный дискриминант :(")
            raise ValueError
            break
        except ZeroDivisionError:
            raise ZeroDivisionError
            break
        except Exception:
            print('пум-пум-пум, где-то ошибка')
            logging.error("Что-то пошло не так, спасайтесь кто может :/")
            raise Exception
            break
        else:
            if xf != xs:
                print(f"Ответ: {xf}, {xs}")
                logging.info("Ура, получили ответ!")
                break
            else:
                print(f'Ответ: {xf}')
                logging.info("Ура, получили ответ!")
                break


