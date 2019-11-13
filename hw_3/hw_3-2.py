def user(**information):
    return information
print('Enter your data, please.')
print(user(name=input('Name: '), surname=input("Surname: "),
date=input('Date of Birth: '), city=input('City: '), email=input('Email: '), num=input('Contact number: ')))