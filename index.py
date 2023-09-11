# create a function that prompts user to enter name, age and city 
def name_and_age():
    name = input('Enter your Name: ')
    age = int(input('Enter your age: '))
    city = input('Where do you live: ')

    return f'My name is {name}, I am {age} years old. I come from {city}'

results = name_and_age()
print(results)