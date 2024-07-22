def solution(angle):
    if angle == 180:
        return 4
    elif angle < 180 and  angle > 90:
        return 3
    elif angle == 90:
        return 2
    elif angle > 0 and angle < 90 :
        return 1