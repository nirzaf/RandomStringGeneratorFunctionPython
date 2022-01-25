import random


#create a function that generate random names and print it for 10 times 
def random_name():
    name_list = []
    for i in range(10):
        name_list.append(random.choice(['John', 'Jane', 'Mary', 'Tom', 'Jack', 'Lily', 'Lucy', 'Lily', 'Lucy', 'Jack']))
    return name_list

print(random_name())




