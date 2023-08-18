import math


def zastroischik(N, M, X):
    uchastkov = math.ceil(N / M)
    summa = 0
    count_stay = N
    for i in range(1, uchastkov + 1):
        if count_stay < M:
            summa += count_stay * X
            break
        count_stay -= M
        summa += M * X
        X += 1000
    return summa


result = zastroischik(10, 3, 10000)
print(result)