import big_o
from big_o.complexities import ALL_CLASSES
import random
def big_o_compare(function1, function2, limit, min=4, max=10, measures=3, repeats=1 ):
    generator = lambda n: big_o.datagen.integers(n, 0, limit)
    best1, others1 = big_o.big_o(function1,generator,min_n=min, max_n=max, n_measures= measures,n_repeats=repeats)

    best2, others2 = big_o.big_o(function2,generator,min_n=min, max_n=max, n_measures= measures,  n_repeats=repeats)
    print(best1, best2)

    big_o_complexity = [ALL_CLASSES[0].__name__, ALL_CLASSES[5].__name__,ALL_CLASSES[1].__name__,ALL_CLASSES[6].__name__,
                        ALL_CLASSES[2].__name__,ALL_CLASSES[3].__name__,ALL_CLASSES[4].__name__,ALL_CLASSES[7].__name__]
    
    if big_o_complexity.index(str(type(best1).__name__)) < big_o_complexity.index(str(type(best2).__name__)):
        print(f"El algoritmo con mayor rendimiento es {function1.__name__}\nSu rendimiento es {best2}")
    elif big_o_complexity.index(str(type(best1).__name__)) == big_o_complexity.index(str(type(best2).__name__)):
        print(f"Ambos algoritmos tiene desempeños similares. Sus rendimientos son {type(best1).__name__} y {type(best2).__name__}")
    else:
        print(f"El algoritmo con mayor rendimiento es {function2.__name__} \nSu rendimiento es {type(best2).__name__}")