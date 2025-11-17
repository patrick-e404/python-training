num = 0

while num <= 10:
    print(num)
    num += 1

print("Finished counting!")

name = None

while True:
    name = input("Enter your name (or 'exit' to quit):")
    if name.lower() == 'exit':
        break
    print(f"Hello, {name}!")
print("Goodbye!")