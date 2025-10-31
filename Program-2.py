a = int(input("Enter A Value: "))
for i in range(1, a + 1):
    print(2 * i - 1, end=", " if i < a else "\n")
