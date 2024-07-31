def solution(a, b):
    ab = str(a) + str(b)
    x = 2 * a * b
    ab = int(ab)
    if ab >= x :
        answer = ab
    else :
        answer = x
        
    return int(answer)