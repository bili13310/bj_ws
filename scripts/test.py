s = input()
field = []

for i in range(len(s)):
    field.append(s[i:])
print(field)
field.sort()

for i in range(len(s)):
    print(field[i])