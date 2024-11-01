# Принцип работы и алгоритм:
Программа использует муравьиный алгоритм для решения задачи кратчайшего пути. Алгоритм реализуется через несколько ключевых параметров, таких как количество муравьев в колонии, количество итераций алгоритма, коэффициент испарения феромонов и интенсивность его отложения, а также важность феромона и видимости в процессе выбора пути.
## Переменные алгоритма: 
Переменные представляют собой неизменяемые значения, которые определяют основные параметры задачи и способ её решения. 

**Количество муравьев (ants_number):** Это количество муравьев, которые будут использоваться для поиска пути.

**Число итераций (iteration):** Это количество итераций, которые будет выполнять алгоритм. Каждая итерация представляет собой один цикл поиска, в результате которого может быть обновлен найденный путь.

**Коэффициент влияния феромонов (ALPHA):** Этот параметр отвечает за важность феромона при выборе пути муравьем. Большее значение этого коэффициента означает большее влияние феромона на выбор муравья.

**Коэффициент видимости (BETA):** Этот параметр определяет важность видимости (расстояния) при выборе пути муравьем. Большее значение этого коэффициента означает большее влияние расстояния на выбор муравья.

**Коэффициент испарения феромона (p):** Этот параметр определяет скорость испарения феромона с течением времени. Большее значение этого коэффициента означает более быстрое исчезновение феромона, что позволяет избежать застревания в локальных оптимумах.

**Интенсивность отложения феромона (Q):** Этот параметр определяет количество феромона, откладываемого муравьем на пути при прохождении. Большее значение этого коэффициента означает более интенсивное отложение феромона, что может ускорить сходимость к оптимальному решению.

Эти переменные играют ключевую роль в формировании стратегии поиска оптимального пути муравьями и определяют эффективность работы муравьиного алгоритма в решении задачи кратчайшего пути. 

## Визуальное представление работы программы:
https://github.com/user-attachments/assets/aefc4bf6-ff9e-436e-9d90-b4348c292d0f
