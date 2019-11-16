#1
k = "カミュ"
print(k[0])
print(k[1])
print(k[2])

#2
a = input("type what you wrote")
b = input("type who you sent it to ")
c = "私は昨日{}を書いて{}に送った！".format(a,b)
print(c)

#3
three = "aldous Hexley was born in 1894."
print(three.capitalize())

#4
four = "where? who? when?"
print(four.split())

#5
first_list = ["The", "fox", "jumped", "over", "the", "fence", "."]
second_list = " ".join(first_list)
fin = second_list.replace(" .", ".")
print(fin)

#6
six = "A screaming comes across the sky"
six_plus =  six.replace("s", "$")
print(six_plus)

#7
seven = "Hemingway".index("m")
print(seven + 1)

#8
print("He said \"I got it!\".")

#9
nine_one = "three" + " three" + " three"
print(nine_one)
nine_two = "three " * 3
print(nine_two)

#10
ten = "四月の晴れ他寒い日で、時計がどれも十三時を打っていた".split("、")
print(ten[0])
