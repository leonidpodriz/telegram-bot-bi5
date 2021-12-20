fibonacci_numbers = [0, 1]
counter = 0

while counter < 98:
    fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    counter += 1

print(fibonacci_numbers)

for _ in range(98):
    fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

print(fibonacci_numbers)
