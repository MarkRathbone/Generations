addFruit = ""
count = 0 
fcount = 0
fruitList = []

while addFruit != "done":
  addFruit = input("Please add a fruit or type \"Done\" to move on.\n").lower()
  if addFruit == "done":
    print("You have finished adding fruit. Moving on.")
  elif addFruit not in fruitList:
    fruitList.append(addFruit)
  elif addFruit in fruitList:
    print("This fruit is already in the list.")

for i in fruitList:
  fruit = fruitList[fcount]
  count = 0
  fruitTotal = input("How many " + fruit + "s do you have?\n")
  if int(fruitTotal) >= 5:
    print("You have a large bunch of " + fruit + "s.")
  elif int(fruitTotal) <= 4 and int(fruitTotal) >= 2:
    print("You have a small bunch of " + fruit + "s.")
  elif int(fruitTotal) == 1:
    print("You only have one " + fruit + "!")
  else:
    print("You have no " + fruit + "s.")
  while (count < int(fruitTotal)):
    fruitCount = count + 1
    print("This is " + fruit + " number " + str(fruitCount))
    count = count + 1
  fcount = fcount + 1