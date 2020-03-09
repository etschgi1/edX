from math import tan, pi


def polysum(n, s):
    """takes sides and length of sides from polygon and sums the area with the
        squared perimeter
    """
    area = (0.25*n*s**2)/(tan(pi/n))
    peri = n*s
    ans = area + peri**2
    return round(ans, 4)


print(polysum(3, 15))
