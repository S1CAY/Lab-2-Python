
width1, height1 = map(int, input("Введіть ширину та висоту першого прямокутника: ").split())
width2, height2 = map(int, input("Введіть ширину та висоту другого прямокутника: ").split())
width3, height3 = map(int, input("Введіть ширину та висоту третього прямокутника: ").split())


area1 = width1 * height1
area2 = width2 * height2
area3 = width3 * height3

print(f"Площа першого прямокутника: {area1}")
print(f"Площа другого прямокутника: {area2}")
print(f"Площа третього прямокутника: {area3}")

import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


a1, b1 = map(int, input("Введіть катети першого трикутника: ").split())
a2, b2 = map(int, input("Введіть катети другого трикутника: ").split())

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print(f"Довжина гіпотенузи першого трикутника: {h1}")
print(f"Довжина гіпотенузи другого трикутника: {h2}")
print("Більша гіпотенуза" if h1 > h2 else "Більша гіпотенуза", "менша", "такі самі"[h1 == h2])



def inside_circle(px, py, a, b, R):
    return (px - a)**2 + (py - b)**2 < R**2

a, b, R = map(int, input("Введіть центр (a, b) та радіус R кола: ").split())
points = [
    tuple(map(int, input("Введіть координати точки Р (р1, р2): ").split())),
    tuple(map(int, input("Введіть координати точки F (f1, f2): ").split())),
    tuple(map(int, input("Введіть координати точки L (l1, l2): ").split()))
]

inside_count = sum(inside_circle(px, py, a, b, R) for px, py in points)
print(f"Кількість точок всередині кола: {inside_count}")



def rectangle_area(x, y):
    return x * y

X, Y, Z, T = map(int, input("Введіть довжини сторін чотирикутника (X, Y, Z, T): ").split())
area = rectangle_area(X, Y)
print(f"Площа чотирикутника: {area}")



n = int(input("Введіть максимальне число n: "))
divisors = list(map(int, input("Введіть дільники через пробіл: ").split()))

numbers = [i for i in range(1, n+1) if all(i % d == 0 for d in divisors)]
print("Числа, що задовольняють умову:", numbers)
