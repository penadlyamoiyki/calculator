auto = [4, 74, 69, 63, 96]

i = 0
a = 0
while i < len(auto):
    a = auto[i] + a
    if auto[i] > 60:
        v = "YES"
    else:
        v = "NO"
    i = i + 1
s = a / len(auto)
print(s)
print(v)

