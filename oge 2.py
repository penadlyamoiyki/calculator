from array import array

numbers = [12, 14, 24, 54, 44, 33, 84, 114]
da = []
i = 0
while i < len(numbers):
    if 4 == numbers[i] % 10:
        a = numbers[i] // 3
        if numbers[i] == a * 3:
            da.append(numbers[i])
    i += 1
print(len(da))