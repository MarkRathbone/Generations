setting = input("\"Normal\" or \"Custom\" settings?\n").lower()

if setting == "normal":
    maxFizzbuzz = 100
    fizzDivide = 3
    buzzDivide = 5
else:
    maxFizzbuzz = input("How high would you like us to count?\n")
    fizzDivide = input("What would you like the division for fizz to be?\n")
    buzzDivide = input("What would you like the division for buzz to be?\n")
fizzbuzzDivide = int(fizzDivide) * int(buzzDivide)

fizzbuzz = 1
while int(fizzbuzz) <= int(maxFizzbuzz):
    if int(fizzbuzz)%int(fizzbuzzDivide)==0:
        print("fizzbuzz")
    elif int(fizzbuzz)%int(buzzDivide)==0:
        print("buzz")
    elif int(fizzbuzz)%int(fizzDivide)==0:
        print("fizz")
    else:
        print(fizzbuzz)
    fizzbuzz = fizzbuzz + 1