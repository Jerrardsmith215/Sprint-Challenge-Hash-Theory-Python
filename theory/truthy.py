# `!(A || B) || ( (A || C) && !(B || !C) )`

def truthy(a, b, c):
    answer = ((not (a or b)) or ((a or c) and not(b or not c)))
    return answer

def truthTable():
    print(               # A     B     C
        truthy(0, 0, 0), # 0     0     0
        truthy(0, 0, 1), # 0     0     1
        truthy(0, 1, 0), # 0     1     0
        truthy(0, 1, 1), # 0     1     1
        truthy(1, 0, 0), # 1     0     0
        truthy(1, 0, 1), # 1     0     1
        truthy(1, 1, 0), # 1     1     0
        truthy(1, 1, 1), # 1     1     1
    ) 

truthTable()