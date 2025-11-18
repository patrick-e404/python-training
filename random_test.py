import random

value = random.randint(1, 20)
print(f"Random integer between 1 and 20: {value}") 

print('Aleatory number between 1 and 50: \n')
for i in range(5):
    n = random.randint(1, 50)
    print(f'Number: {n}')

value = random.random()
print(f'number generated: {round(value * 10, 2)}')

value = random.uniform(1, 100)
print(f'Number: {round(value, 4)}')

list = [2,4,6,9,10,13,15,18,20,21]
n = random.choice(list)
print(f'Number chosen: {n}')

num = random.sample(list, 3)
print(f'Numbers chosen: {num}')

print(f'Original list: {list}')
print('Shuffling the list...')
n1 = random.shuffle(list)
print(f'Shuffled list: {list}')