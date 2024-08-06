def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            t = a + i * d
            answer += t
    return answer