for cont_ex in range (1,6):
    print(f'\nexternal loop: {cont_ex}')
    for cont_in in range (5, 0, -1):
        print(f'  internal loop: {cont_in}')
print("Finished all loops!")

import random

for A in range(1,6):
    print(f'\nConjunto {A}')
    for B in range(5):
        num = random.randint(1,100)
        print(f'  Número sorteado: {num}')