"""
combinations()
combinations_with_replacement()
permutations()

"""
import itertools

a = [1,2,3]
b = list(itertools.permutations(a,2))
print(b)

a = [1,2,3]
b = list(itertools.combinations(a,2))
print(b)
