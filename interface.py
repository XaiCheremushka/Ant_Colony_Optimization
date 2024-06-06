import asyncio
import time
import turtle
from data import Data


class Graf:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Замкнутый граф с городами")
        self.screen.bgcolor("white")
        self.screen.setup(width=800, height=800)
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()

    def draw_graf(self):
        cords = Data.cords
        cities = Data.citiesCount

        # Очистка предыдущего рисунка
        self.pen.clear()

        # Функция для рисования жирной точки
        def draw_city(city):
            x, y = cords[city]
            self.pen.penup()
            self.pen.goto(x, y)
            self.pen.pendown()
            self.pen.dot(20, "red" if city == 0 or city == cities - 1 else "black")

        # Функция для рисования линий между городами
        def draw_line(city1, city2):
            self.pen.penup()
            self.pen.goto(city1[0], city1[1])
            self.pen.pendown()
            self.pen.goto(city2[0], city2[1])

        for city in range(cities):
            draw_city(city)

        draw_line(cords[0], cords[1])
        draw_line(cords[0], cords[3])
        draw_line(cords[1], cords[2])
        draw_line(cords[2], cords[4])
        draw_line(cords[1], cords[5])
        draw_line(cords[3], cords[5])
        draw_line(cords[3], cords[4])
        draw_line(cords[4], cords[6])
        draw_line(cords[5], cords[6])
        draw_line(cords[6], cords[7])
        draw_line(cords[6], cords[8])
        draw_line(cords[6], cords[9])
        draw_line(cords[7], cords[9])
        draw_line(cords[8], cords[9])


class Ant:
    def __init__(self, start_position, path):
        self.position = start_position
        self.path = path
        self.path_index = 0
        self.pen = turtle.Turtle()
        self.pen.shape("turtle")
        self.pen.color("blue")
        self.pen.penup()
        self.pen.goto(start_position)
        self.pen.pendown()
        self.speed = 10  # Скорость муравья
        self.finished = False  # Флаг завершения пути

    def move(self):
        if self.path_index < len(self.path) - 1:
            current_city = self.path[self.path_index]
            next_city = self.path[self.path_index + 1]

            current_position = Data.cords[current_city - 1]
            next_position = Data.cords[next_city - 1]

            dx = next_position[0] - current_position[0]
            dy = next_position[1] - current_position[1]
            distance = (dx ** 2 + dy ** 2) ** 0.5

            steps = int(distance / self.speed)
            x_step = dx / steps
            y_step = dy / steps

            self.pen.goto(self.pen.xcor() + x_step, self.pen.ycor() + y_step)

            if abs(self.pen.xcor() - next_position[0]) < self.speed and abs(
                    self.pen.ycor() - next_position[1]) < self.speed:
                self.path_index += 1

        if self.path_index >= len(self.path) - 1:
            self.finished = True  # Помечаем муравья как завершившего путь


async def update_ants(ants):
    all_finished = True
    for ant in ants:
        ant.move()
        if not ant.finished:
            all_finished = False

    if all_finished:
        for ant in ants:
            ant.pen.clear()  # Удаляем черепаху после достижения конечной точки
        return True
    else:
        return False


async def run(paths):
    ants = []
    start_position = Data.cords[0]

    # Инициализация муравьев
    for path in paths:
        ants.append(Ant(start_position, path))

    while not await update_ants(ants):
        await asyncio.sleep(0.05)  # Пауза перед проверкой завершения движения муравьев


async def run_animation(pathsIter):
    graf = Graf()
    graf.draw_graf()

    for paths in pathsIter:
        await run(paths)
        # await asyncio.sleep(2)  # Пауза между итерациями

    # Чтобы окно turtle не закрывалось сразу
    graf.screen.mainloop()


