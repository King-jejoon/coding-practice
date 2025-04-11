n = input()
l = len(n)
n = int(n)
count = l * (n - (10**(l - 1)-1))
l -= 1
while l > 0:
    count += l * 9 * 10**(l - 1)
    l -= 1
print(count)