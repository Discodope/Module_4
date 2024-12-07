import math
def div(first , second):
    if second != 0:
        sum = first / second
        print('Ответ : ', sum)
    elif second == 0:
        print('Ответ', float(math.inf))

div(5, 0)
div(6,2)