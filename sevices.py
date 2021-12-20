def greet_name(name):
    return f'Hello, {name}!'


def greet_names(names):
    result = ''

    for name in names:
        result += greet_name(name) + '\n'

    return result


print(greet_name("Leonid"))
print(greet_names(["Leonid", 'Oleg']))
