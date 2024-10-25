print("-=" * 20)
num = int(input("Você quer ver tabuada de qual numero? "))
print("-=" * 20)

while True:
    for i in range(1,11):
        print(f"{num} X {i} = {num * i}")

    print("-=" * 20)    
    num = int(input("Você quer ver tabuada de qual numero? "))
    print("-=" * 20)

    if num < 0:
        break

print("Volte Sempre!")