import datetime
def solution(age):
    answer = datetime.datetime.now().year - int(age) - 1
    return answer