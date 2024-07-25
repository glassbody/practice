import math
def solution(numer1, denom1, numer2, denom2):
    numer = (numer1*denom2 + denom1*numer2)
    denom = denom1*denom2
    gcd = math.gcd(denom, numer)
    answer = [numer//gcd , denom//gcd]
    return answer