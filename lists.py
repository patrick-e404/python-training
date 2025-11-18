n1 = [1,3,5,7,9]
n2 = [2,4,6,8,10]
value = n1 + n2

print(f'Concatenated list: {value}')
print(value[-1])
print(value[2:7])
print(len(value))
print(sorted(value))
print(sorted(value, reverse=True))
print(sum(value))
print(min(value))
print(max(value))

value.append(11)
print(value)
value.pop()

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet)

movies = []
for i in range(5):
    print(f'Enter your favorite movie: {i+1}' )
    movie = input()
    movies.append(movie)
   
movies.sort()
print("Your favorite movies are:", movies)