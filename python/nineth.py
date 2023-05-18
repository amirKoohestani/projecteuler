for i in range(1, 1000):
    for j in range(i+1, 1000):
        for k in range(j+1, 1000):
            if i + j + k ==1000:
                if pow(i, 2) + pow(j, 2) == pow(k, 2):
                    print(i*j*k)