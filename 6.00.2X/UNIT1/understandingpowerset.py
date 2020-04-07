def powerSet(items):
    N = len(items)
    for i in range(2**N):
        combo = []
        for j in range(N):
            if (i//(2**j)) % 2 == 1:
                combo.append(items[j])
                print("item appended: " + items[j])
                print(i//(2**j))
            else:
                print("no item appended")
        yield combo


fruits = ["apple", "orange", "watermelon", "tangerine", "strawberry"]

a = powerSet(fruits)

num = 0

for x in range(2**len(fruits)):
    print("binary number: " + "{0:b}".format(num)[::-1])
    print("")
    print("set = " + str(next(a)))
    print("")
    print("")
    num += 1
