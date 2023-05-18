sum = 0
for i in range(10000000000000000000):
    sum += i
    if sum > 70000000:
        counter = 1
        for i in range(1, int(sum/2)):
            if sum % i == 0:
                counter += 1
        if counter >= 500:
            print(sum)
            break