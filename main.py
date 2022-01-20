import random

first_name = ('Adams', 'Allen', 'Atkinson', 'Bailey', 'Ball', 'Brown', 'Clarke', 'Cole', 'Collins', 'Elliot', 'Fisher', 'Ford', 'Fox', 'Graham', 'Gray')
last_name = ('Emma', 'Michael', 'Matthew', 'Christopher', 'Elizabeth', 'Madison', 'Sophia', 'Chloe', 'Emily', 'Agnes', 'Ariel', 'Ethan', 'Arya', 'Angelina', 'Isabella')
middle_name = ('Smith', 'Johnson', 'Williams', 'Jones', 'Miller', 'Brown', 'Moore', 'Taylor', 'Lewis', 'Harris', 'Martin', 'Wilson', 'Harris', 'Thompson', 'White')


n = ''.join([random.choice(first_name) for x in range(1)])
l = ''.join([random.choice(last_name) for i in range(1)])
m = ''.join([random.choice(middle_name) for o in range(1)])

with open('random_fio.txt', 'a') as file:
    file.write('\nФамилия: ' + l + '.' + '\nИмя: ' + n + '.' + '\nОтчество: ' + m + '.')
    file.close()

files = open('random_fio.txt')
print(files.readlines())





