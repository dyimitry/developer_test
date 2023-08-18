import math
def zastroischik(N, M, X):
    uchastkov= math.ceil(N / M)
    uchastkov_int= int(N/M)
    summa = 0
    count_N = N
    for i in range(1,uchastkov+1):
        if uchastkov_int != uchastkov and i==uchastkov:
            count_N =int(M* (count_N / M))
            summa +=count_N*X
            break
        count_N -= M
        summa += M*X
        X += 1000
    print(summa)

zastroischik(8,3,10000)