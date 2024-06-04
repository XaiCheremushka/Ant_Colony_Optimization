import turtle

from data import Data


class Graf:
    # Настройка экрана
    screen = turtle.Screen()
    screen.title("Замкнутый граф с городами")
    screen.bgcolor("white")
    screen.setup(width=800, height=800)

    @staticmethod
    def draw_graf():
        cords = Data.cords
        cities = Data.cities

        # Настройка черепашки для рисования
        pen = turtle.Turtle()
        pen.speed(0)
        pen.hideturtle()

        # Функция для рисования жирной точки
        def draw_city(city):
            x, y = cords[city]
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.dot(20, "red" if city == 0 or city == cities - 1 else "black")

        # Функция для рисования линий между городами
        def draw_line(city1, city2):
            pen.penup()
            pen.goto(city1[0], city1[1])
            pen.pendown()
            pen.goto(city2[0], city2[1])

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
        self.pen.goto(self.position)
        self.pen.pendown()
        self.speed = 5  # Скорость муравья

    def move(self):
        if self.path_index < len(self.path) - 1:
            current_city = self.path[self.path_index]
            next_city = self.path[self.path_index + 1]

            current_position = Data.cords[current_city]
            next_position = Data.cords[next_city]

            dx = next_position[0] - current_position[0]
            dy = next_position[1] - current_position[1]
            distance = (dx**2 + dy**2)**0.5

            steps = int(distance / self.speed)
            x_step = dx / steps
            y_step = dy / steps

            self.pen.goto(self.pen.xcor() + x_step, self.pen.ycor() + y_step)

            if abs(self.pen.xcor() - next_position[0]) < self.speed and abs(self.pen.ycor() - next_position[1]) < self.speed:
                self.path_index += 1


def update_ants():
    for ant in ants:
        ant.move()
    turtle.ontimer(update_ants, 50)  # обновление каждые 50 миллисекунд


def main():
    Graf.draw_graf()

    global ants
    ants = []
    start_position = Data.cords[0]

    # Инициализация муравьев
    for _ in range(len(Data.paths)):
        ants.append(Ant(start_position, Data.paths[_]))

    # Начало обновления муравьев
    update_ants()


if __name__ == "__main__":
    main()
    turtle.done()
