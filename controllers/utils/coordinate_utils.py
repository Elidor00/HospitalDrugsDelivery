from math import sqrt, atan2, pi


# u = vector[0], v = vector[1]
# vector = [u,v]
# ||v||
def norm(vector: list) -> float:
    return sqrt(vector[0] * vector[0] + vector[1] * vector[1])


# v = v/||v||
def normalize(vector: list) -> list:
    n = norm(vector)
    u = vector[0] / n
    v = vector[1] / n
    return [u, v]


def modulus_double(a: float, m: float) -> float:
    div_i = int(a / m)
    div_d = float(div_i)
    r = a - div_d * m
    if r < 0.0:
        r += m
    return r


# compute the angle between two vectors
# return value: [0, 2Pi[
def angle(vector1: list, vector2: list) -> float:
    return modulus_double(atan2(vector2[1], vector2[0]) - atan2(vector1[1], vector1[0]), 2.0 * pi)


# v = v1-v2
def minus(vector1: list, vector2: list) -> list:
    vector_res = [0.0, 0.0]
    vector_res[0] = vector1[0] - vector2[0]
    vector_res[1] = vector1[1] - vector2[1]
    return vector_res


# v = v1+v2
def plus(vector1: list, vector2: list) -> list:
    vector_res = [0.0, 0.0]
    vector_res[0] = vector1[0] + vector2[0]
    vector_res[1] = vector1[1] + vector2[1]
    return vector_res


# atan2(z, x)
def polar_angle(vector1: list):
    angle_degree = atan2(vector1[1], vector1[0]) / pi * 180
    if angle_degree < 0:
        angle_degree = angle_degree 
    return angle_degree
