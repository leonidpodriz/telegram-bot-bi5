def greet_name(name):
    return f'Hello, {name}!'


def greet_names(names):
    result = ''

    for name in names:
        result += greet_name(name) + '\n'

    return result


print(greet_name("Leonid"))
print(greet_names(["Leonid", 'Oleg']))


def is_even(number):
    return number % 2 == 0


ages = [19, 45, 32, 34, 12, 10, 22, 88, 87]
even_ages = list(filter(is_even, ages))
odd_ages = list(filter(lambda number: number % 2 == 1, ages))

print(even_ages)
print(odd_ages)
