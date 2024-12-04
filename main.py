"""
Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:

test_walk:

Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
с сообщением "Неверная скорость для Runner".

test_run:

Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
с сообщением "Неверный тип данных для объекта Runner".
"""

import unittest
import runners
import logging
import traceback

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):
    """Дочерний класс, наследуемый от класса unittest.TestCase"""
    def test_walk(self):
        """Метод тестирует метод объекта 'walk'"""
        try:
            runner_walk = runners.Runner('Runner_1', -5)  # создаем экземпляр класса
            for i in range(10):  # в цикле от 0 до 9 включительно
                runner_walk.walk()  # вызываем метод 'walk' объекта
            self.assertEqual(runner_walk.distance, 50)  # сравниваем значение атрибута объекта с контрольным значением
            logging.info(f'Метод <test_walk> выполнен успешно')
        except ValueError as e:
            logging.warning(f'Метод <test_walk>. Неверная скорость для Runner')
            logging.warning(f"{e}")
            logging.warning(traceback.format_exc())
        except TypeError as e:
            logging.warning(f"{e}")
            logging.warning(traceback.format_exc())



    def test_run(self):
        """Метод тестирует метод объекта 'run'"""
        try:
            runner_run = runners.Runner(True)  # создаем экземпляр класса
            for i in range(10):  # в цикле от 0 до 9
                runner_run.run()  # вызываем метод 'run' объекта
            self.assertEqual(runner_run.distance, 100)  # сравниваем значение атрибута объекта с контрольным значением
            logging.info('Метод <test_run> выполнен успешно')
        except TypeError as e:
            logging.warning(f'Метод <test_run>. Неверный тип данных для объекта Runner')
            logging.warning(f"{e}")
            logging.warning(traceback.format_exc())

    def test_challenge(self):
        """Метод тестирует атрибуты двух объектов класса на неравенство"""
        test_runner_1 = runners.Runner('Runner_1')  # создаем первый объект класса
        test_runner_2 = runners.Runner('Runner_2')  # создаем второй объект класса
        for i in range(10):  # в цикле от 0 до 9
            test_runner_1.run()  # вызываем метод 'run' для первого объекта
            test_runner_2.walk()  # вызываем метод 'walk' для второго объекта
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)  # сравниваем значение атрибута объектов с контрольным значением на неравенство
        logging.info('Метод <test_challenge> выполнен успешно')

if __name__ == '__main__':
    unittest.main()  # вызов метода тестирования