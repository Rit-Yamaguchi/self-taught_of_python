#1
food = ["takoyaki", "ramen", "curry"]
print(food)

#2
place = ("Iwata", "Takasaki", "Fujisawa", "Nagaokakyo")
print(place)

#3
map = {
"Iwata":"til_18",
"Talasaki":"till_19",
"Fujisawa":"till_21"
}

#4
key = input("type a name of city")
if key in map:
    city = map[key]
    print(city)
else:
    print("that is not a city I used to live in")

#5
map["Nagaokakyo"] = "till_now"
print(map["Nagaokakyo"])
