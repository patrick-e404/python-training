lista = [1,4,6,3,1,5,20,31,5,8,13]

for item in lista:
    print(item)

for num in range(11):
    print(num)

name = input("Digit your name: ")
for x in range(10):
    print(f'{x+1} {name}')

for x in range(0, 21, 2):
    print(x)

rocks = ('diamond', 'ruby', 'emerald', 'sapphire', 'topaz')

for rock in rocks:
    if rock == 'topaz':
        continue
    print(rock)