def solution(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    int(ab)
    int(ba)
    if ab >= ba:
        answer = ab
    else:
        answer = ba
    return int(answer)