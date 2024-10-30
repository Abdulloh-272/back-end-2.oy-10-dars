for i in range(1, 101):
    if i % 5 != 0:
        print(i, end=", " if i < 100 else "")
ismlar = []
while True:
    ism = input("Ism kiriting (stop deb yozing to'xtatish uchun): ")
    if ism.lower() == 'stop':
        break
    ismlar.append(ism)


print(" ".join(ismlar))  
footballers = {}
while True:
    ism = input("Futbolchi ismini kiriting (stop deb yozing to'xtatish uchun): ")
    if ism.lower() == 'stop':
        break
    gol = int(input(f"{ism} uchun gollar sonini kiriting: "))
    footballers[ism] = gol


for ism, gol in footballers.items():
    print(f"{ism} - {gol}")  
footballers = {}
while True:
    ism = input("Futbolchi ismini kiriting (stop deb yozing to'xtatish uchun): ")
    if ism.lower() == 'stop':
        break
    gol = int(input(f"{ism} uchun gollar sonini kiriting: "))
    footballers[ism] = gol

for ism, gol in footballers.items():
    print(f"{ism} - {gol}") \
