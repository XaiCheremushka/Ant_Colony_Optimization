import asyncio
import time
import turtle

from data import Data
from ant import Ant
from interface import run_animation

async def main():
    iteration = 5
    pathsIter = []

    for _ in range(iteration):
        print(Data.amount_of_pheromones)
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

        pathsAnts = []

        # Инициализация муравьев для каждой итерации
        ants = [Ant() for i in range(Data.citiesCount)]

        for ant in ants:
            try:
                ant.start()  # запускаем подсчет данных
                pathsAnts.append(ant.tabu)  # добавляем пройденный путь муравья
                # добавляем локальные феромоны в словарь
                for edge in ant.tabuEdges:
                    if edge in sum_local_pheromones.keys():
                        sum_local_pheromones[edge] += ant.Tij
            except ValueError as e:
                print(e)

        pathsIter.append(pathsAnts)

        Data.regenerate_pheromones(sum_local_pheromones)  # Обновляем феромоны на ребрах

    await run_animation(pathsIter)  # Запускаем анимацию без использования await


if __name__ == '__main__':
    # main()
    asyncio.run(main())
