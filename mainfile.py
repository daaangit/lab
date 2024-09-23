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
total = c + q; evenN = []; notEven = []
for x in range(c, total):
    if x % 2 == 0: evenN.append(x)
srednEv = sum(evenN) / len(evenN)
print(srednEv)

    
