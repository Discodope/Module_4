import math
def div(first , second):
    if second != 0:
        sum = first / second
        print('Ответ : ', sum)
        return sum
    elif second == 0:
        print('Ответ', float(math.inf))
