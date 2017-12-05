num = int(input("Number : "))
x = []

for ans in range(2, num):
    count = 0
    for bas in range(2, num):
        if ans % bas == 0:
            count += 1
            if ans == bas and count == 1:
                x.append(ans)
print(x)