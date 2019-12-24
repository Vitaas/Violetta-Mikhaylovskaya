y = int(input())
x = y % 10
y = y // 10

while y > 0:
    if y % 10 > x:
        x = y % 10
    y = y // 10
print(x)
