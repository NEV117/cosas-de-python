from collections import Counter
from math import factorial
from functools import reduce
import re
from itertools import permutations

#Nicolas Escandon Varela#

def principal():
    print("***Programa que calcula cuantas cadenas Distintas***\n***      Se pueden formar con una palabra.       ***\n*** (numeros y simbolos se leen como caracteres) ***")
    try:
        palabra = input("\nDigita una palabra: ")
        p = r'\s+'
        p2 = re.sub(p, '', palabra)

        c1 = Counter(p2)
        c2 = [t[1] for t in list(c1.items())]
        f = len(p2)
        m = factorial(f)

        x = []
        for n in range(len(c2)):
            x.append(factorial(c2[n]))

        r = reduce(lambda x, y: x*y, x)

        c_d = m / r

        z = [''.join(p) for p in permutations(p2)]
        res = []
        for item in z:
            if item not in res:
                res.append(item)

        print("\nCardinalidad de la palabra: " + str(f) + "\n\nCardinalidad de cada clase: " + str(list(c1.items())) + "\n\nCantidad de cadenas que se pueden formar: " + str(c_d) + "\n\nTodas las posibles cadenas son : \n\n" + str(res))
        #print(z)
        
    except:
        print("Debe digitar por lo menos una letra, simbolo o numero")
        
principal()
