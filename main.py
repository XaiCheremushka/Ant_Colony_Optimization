import asyncio
import turtle

from data import Data
from ant import Ant
from interface import create_graf, run_animation

async def main():
    create_graf()  # Рисуем граф

    iteration = 3

    for _ in range(iteration):
        sum_local_pheromones = {
            '1-2': 0,
            '1-4': 0,
            '2-3': 0,
            '2-6': 0,
            '3-5': 0,
            '4-5': 0,
            '4-6': 0,
            '5-7': 0,
            '6-7': 0,
            '7-8': 0,
            '7-9': 0,
            '7-10': 0,
            '8-10': 0,
            '9-10': 0
        }
        paths = []

        # Инициализация муравьев для каждой итерации
        ants = [Ant() for i in range(Data.citiesCount)]

        for ant in ants:
            try:
                ant.start()  # запускаем подсчет данных
                paths.append(ant.tabu)  # добавляем пройденный путь муравья
                # добавляем локальные феромоны в словарь
                for edge in ant.tabuEdges:
                    if edge in sum_local_pheromones.keys():
                        sum_local_pheromones[edge] += ant.Tij
            except ValueError as e:
                print(e)

        Data.regenerate_pheromones(sum_local_pheromones)  # Обновляем феромоны на ребрах
        print(paths)
        await run_animation(paths)

    # Чтобы окно turtle не закрывалось сразу
    turtle.mainloop()

if __name__ == '__main__':
    asyncio.run(main())
