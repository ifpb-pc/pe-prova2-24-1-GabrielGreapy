from collections import Counter
from typing import List
import csv
def q1a(nums: List[int]) -> bool:
    pass
    

def q1b(nums: List[int]) -> bool:
    pass


def q2(s: List,t: List) -> bool:
    pass
    
def q3() -> int:
    s = input('')
    t = input('')
    if s.sort() == t.sort() :
        return(True)

def q4():
    lista1 = []
    num = int(input(''))

    while num != 0:
        num = int(input(''))
        lista1.append(num)
    resultado_impares = []
    resultado_pares = []

    for i in lista1:
        if i % 2 == 0:
            resultado_pares.append(i)
        else : 
            resultado_impares.append(i)
    return(resultado_pares, resultado_impares)
    


if __name__=="__main__":
    # teste sua questão manualmente aqui
    q3()