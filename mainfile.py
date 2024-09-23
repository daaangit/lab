print("Hello!")
print("enter a")
a = int(input())
print("enter b")
b = int(input())
c = a - b
print("a - b =", c)
c = a + b
print("a + b =", c)
q = a * b
print("a * b =", q)
total = c + q; evenN = []
for x in range(1, total):
    if x % 2 == 0: evenN.append(x)
print(len(evenN))
    
