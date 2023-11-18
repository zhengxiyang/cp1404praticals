for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number = int(input("enter number:"))
for i in range(0, number, 1):
    print('*', end=' ')
print()

number = int(input("enter number:"))
j = 0
while j < number:
    i = 0
    while i <= j:
        print('*', end='')
        i += 1
    print()
    j += 1