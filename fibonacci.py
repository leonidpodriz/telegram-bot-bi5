import datetime

fibonacci_numbers = [0, 1]
counter = 0

# while counter < 98:
#     fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
#     counter += 1
#
# print(fibonacci_numbers)

start = datetime.datetime.now()

for _ in range(100000):
    new = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(new)
    # print(new)
end = datetime.datetime.now()

print(end - start)
# print(fibonacci_numbers)
