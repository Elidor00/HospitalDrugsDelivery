from math import sqrt, atan2, pi, cos, sin, radians


# u = vector[0], v = vector[1]
# vector = [u,v]
# ||v||
def norm(vector: list) -> float:
    return sqrt(vector[0] * vector[0] + vector[1] * vector[1])


# v = v1-v2
def minus(vector1: list, vector2: list) -> list:
    vector_res = [0.0, 0.0]
    vector_res[0] = vector1[0] - vector2[0]
    vector_res[1] = vector1[1] - vector2[1]
    return vector_res


# arctangent(z, x)
def polar_angle(vector1: list):
    angle_degree = atan2(vector1[1], vector1[0]) / pi * 180
    if angle_degree < 0:
        angle_degree = angle_degree
    return angle_degree


def calculate_angle(checkpoint_angle, north_angle):
    angle_result = 0.0
    if checkpoint_angle >= 0.0 and north_angle >= 0.0:
        if checkpoint_angle < north_angle:
            angle_result = checkpoint_angle - north_angle
        else:
            angle_result = -(north_angle - checkpoint_angle)
    if checkpoint_angle < 0.0 and north_angle >= 0.0:
        # angle_result = checkpoint_angle + north_angle
        if north_angle + abs(checkpoint_angle) < 180.0:
            angle_result = -(north_angle - checkpoint_angle)
        else:
            angle_result = 180.0 - north_angle - checkpoint_angle

    if checkpoint_angle >= 0.0 and north_angle < 0.0:
        # angle_result = checkpoint_angle + north_angle
        if checkpoint_angle + abs(north_angle) >= 180.0:
            angle_result = -(180 + north_angle + checkpoint_angle)
        else:
            angle_result = - north_angle + checkpoint_angle
    if checkpoint_angle < 0.0 and north_angle < 0.0:
        if abs(north_angle) < abs(checkpoint_angle):
            angle_result = - (-checkpoint_angle + north_angle)
        else:
            angle_result = - north_angle + checkpoint_angle
    return angle_result


# angle must be in radiants
def rotate(angle, vector):
    return [vector[0] * cos(radians(angle)) - vector[1] * sin(radians(angle)),
            vector[0] * sin(radians(angle)) + vector[1] * cos(radians(angle))]
