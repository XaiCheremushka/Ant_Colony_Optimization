from data import Data

ALPHA = 1.0  # коэффициент влияния феромонов
BETA = 5.0  # коэффициент видимости
p = 0.2  # коэффициент испарения




class Ant:
    tabu = []  # пройденные города (индексирование с 1)

    def find_probability(self, city: str):
        """Нахождение вероятности"""
        proizv = {}  # Произведения видимости и кол-ва феромонов доступных вершин
        ver = {}  # Итоговые вероятности выбора вершины
        for j in Data.ways[city]:
            if j not in self.tabu:  # Проверяем есть ли выбранный город в пройденных
                # for l in Data.ways[city]:  # Проходимся по всем возможным городам помимо выбранного и пройденных
                #     if l not in self.tabu and l != j:
                try:
                    t = Data.amount_of_pheromones[f'{city}-{j}']  # (Тау) количество феромонов на этом пути
                    n = 1 / Data.distances[f'{city}-{j}']
                except Exception as e:
                    print(f'{city}-{j} - такого пути нет')
                    t = Data.amount_of_pheromones[f'{j}-{city}']  # (Тау) количество феромонов на этом пути
                    n = 1 / Data.distances[f'{j}-{city}']
                proizv[str(j)] = t**ALPHA * n**BETA
        for j in proizv.keys():
            ver[j] = proizv[j]/sum(proizv.values())

        # ! реализовать выбор города по вероятности или вынести этот выбор в другую функцию