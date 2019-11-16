#1
one = ["wd", "ant", "sop", "vd"]
for name in one:
    print(name)

#2
x = 25
for i in range (0, 100):
    if x == 51:
        break
    print(x)
    x += 1

#3
num = ["1", "2", "3"]
for i in range(0, 3):
    print( num[i] + "." + " " + one[i])

#4
ans = ["7", "13", "91"]
while True:
    print("type q to quit")
    sug = input("guess and type the number from 0 to 100")
    if sug == "q":
        break
    elif sug in ans:
        print("You got it!")
        break

#5
a = [8, 19, 148, 4]
b = [9, 1, 33, 88]
result = []
for i in a:
    for j in b:
        result.append(i*j)
print(result)
