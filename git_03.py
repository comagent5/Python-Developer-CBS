'''
Вибираэмо парны числа, пушимо в GitHub
'''

from random import randint

numbers = [randint(1, 100) for _ in range(100)]
print(numbers)

num_even = []

for num in numbers:
    if num % 2 == 0:
        num_even.append(num)

print(num_even)




