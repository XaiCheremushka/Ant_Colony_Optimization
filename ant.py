import random

from data import Data

ALPHA = 1.0  # коэффициент влияния феромонов
BETA = 5.0  # коэффициент видимости
Q = 5.0  # константа

class Ant:
    def __init__(self):
        self.tabu = [1]  # пройденные города (индексирование с 1)
        self.tabuEdges = []  # Пройденные пути
        self.Tij = 0.0  # локальные феромоны на отрезке i-j

    def find_probability(self, city: str):
        """Нахождение вероятности"""
        proizv = {}  # Произведения видимости и кол-ва феромонов доступных вершин
        ver = {}  # Итоговые вероятности выбора вершины
        print(f"Текущий город: {city}, Доступные пути: {Data.ways[city]}")
        for j in Data.ways[city]:
            if j not in self.tabu:  # Проверяем есть ли выбранный город в пройденных
                try:
                    t = Data.amount_of_pheromones[f'{city}-{j}']  # (Тау) количество феромонов на этом пути
                    n = 1 / Data.distances[f'{city}-{j}']
                except KeyError:
                    print(f'{city}-{j} - такого пути нет')
                    t = Data.amount_of_pheromones[f'{j}-{city}']  # (Тау) количество феромонов на этом пути
                    n = 1 / Data.distances[f'{j}-{city}']
                proizv[str(j)] = t**ALPHA * n**BETA
        if not proizv:
            raise ValueError(f"No available cities to move to from city {city}. Tabu: {self.tabu}")
        for j in proizv.keys():
            ver[j] = proizv[j] / sum(proizv.values())
        print(f"Произведения: {proizv}")
        print(f"Вероятности: {ver}")

        # Производим выбор города по вероятностям
        r = random.random()  # Рандомное число от 0 до 1
        otrezok = 0.0  # Отрезок, к которому будут прибавляться числа
        for key in ver.keys():
            otrezok += ver[key]
            if r < otrezok:  # если число r попало в отрезок из вероятностей, то возвращаем город, в который пойдет мур.
                print(f'Выбранный город: {key}')
                return key
        # Если не удалось выбрать город, что не должно происходить
        raise RuntimeError("Не удалось выбрать следующий город")

    def local_update(self):
        """Локальное обновление феромонов"""
        L = 0.0  # Расстояние пройденное муравьем на итерации

        for i in range(1, len(self.tabu)):
            if self.tabu[i] > self.tabu[i-1]:
                L += Data.distances[f'{self.tabu[i-1]}-{self.tabu[i]}']
                self.tabuEdges.append(f'{self.tabu[i-1]}-{self.tabu[i]}')
            else:
                L += Data.distances[f'{self.tabu[i]}-{self.tabu[i-1]}']
                self.tabuEdges.append(f'{self.tabu[i]}-{self.tabu[i-1]}')

        self.Tij = Q / L

    def start(self):
        """Запуск итерации муравья"""
        city1 = '1'
        while city1 != str(Data.citiesCount):
            city2 = self.find_probability(city1)
            self.tabu.append(int(city2))
            city1 = city2
            print('-')
        print('-----------------------------------')
        self.local_update()
