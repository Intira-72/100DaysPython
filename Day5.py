fruits = ['Apple', 'Peach', 'Pear']

# For Loop
for fruit in fruits:
    print(fruit)


stu_height = [180, 124, 165, 173, 189, 169, 146]
total_height = 0
stu_count = 0

for h in stu_height:
    total_height += h
    stu_count += 1

print(f'Stu Height Avg = {round(total_height / stu_count)}')


stu_scores = [78, 65, 89, 86, 55, 91, 64, 89]
height_score = 0

for score in stu_scores:
    if score > height_score:
        height_score = score
print(f'Height Score = {height_score}')


sum_numbers = 0

for i in range(1, 101):
    sum_numbers += i
print(f'Number Total = {sum_numbers}')


sum_even_number = 0

for i in range(2, 101, 2):
    sum_even_number += i
print(f'Even Number = {sum_even_number}')


# while True:
#     num = int(input('your number : '))

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
        # break
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)