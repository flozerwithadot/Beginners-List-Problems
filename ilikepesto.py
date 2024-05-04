iLikePesto = []
otherFoods = []
for x in range(8):
    fav = input("What's your favourite food? ")
    if fav == "pesto":
        iLikePesto.append(fav)
    else:
        otherFoods.append(fav)
for x in range(len(iLikePesto)):
    print("I like pesto")
for x in range(len(otherFoods)):
    print(otherFoods[x])
