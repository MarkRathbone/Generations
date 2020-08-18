f = open("results.txt", "a")
f.truncate(0)

lowNum = input("Where should we start our search?\n")
highNum = input("Where should we end our search?\n")

for number in range(int(lowNum), int(highNum)):
   if number > 1:
       for i in range(2, number):
           if (number % i) == 0:
               break
       else:
           f.write (str(number)+"\n")

print("Results have been printed to results.txt.")