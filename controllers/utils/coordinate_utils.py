from math import sqrt, atan2, cos, sin, radians, degrees


# ||v||
from controllers.utils.const import MAX_SPEED


def norm(vector: list) -> float:
    return sqrt(vector[0] * vector[0] + vector[1] * vector[1])


# v = v1-v2
def minus(vector1: list, vector2: list) -> list:
    vector_res = [0.0, 0.0]
    vector_res[0] = vector1[0] - vector2[0]
    vector_res[1] = vector1[1] - vector2[1]
    return vector_res


# distance between two points
def calculate_distance(vector1: list, vector2: list) -> float:
    return norm(minus(vector1, vector2))


# arctangent(z, x)
def polar_angle(vector1: list) -> float:
    return degrees(atan2(vector1[1], vector1[0]))


# rotate the vector "vector" (coord system) of angle "angle"
def rotate(angle: float, vector: list) -> list:
    return [vector[0] * cos(radians(angle)) - vector[1] * sin(radians(angle)),
            vector[0] * sin(radians(angle)) + vector[1] * cos(radians(angle))]




