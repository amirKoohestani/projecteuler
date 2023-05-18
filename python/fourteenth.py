def numberOfChain(number):
    length = 1
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        length = length + 1
    return length

def findMax(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max



listOfLength = []

for i in range(1, 1000000):
    listOfLength.append(numberOfChain(i))

print(findMax(listOfLength))