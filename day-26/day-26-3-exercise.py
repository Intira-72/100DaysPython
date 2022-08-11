
with open('text1.txt') as file:
    text1 = [int(num.strip('\n')) for num in file.readlines()]

with open('text2.txt') as file:
    text_2 = [int(num.strip('\n')) for num in file.readlines()]

result = [num for num in text1 if num in text_2]

print(result)