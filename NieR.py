#NieR.sh to python port.
#See https://www.youtube.com/watch?v=AczZoNeso04 for reference.

from os import system, name 
from time import sleep

def clear(): 
  if name == 'nt': 
    _ = system('cls') 
  else: 
    _ = system('clear')

#Resetting Invalid to 0
invalidCheck = 0

#will question
def will():
  global invalidCheck
  clear()
  invalid()
  print("LOADING - CHECKING SYSTEM...")
  print("")
  print("Will. From where does our will come?")
  print("1. It is born from nothingness.")
  print("2. It is given to us by God.")
  print("3. I don't care. I don't need any of this!")
  answer = input("Please select 1, 2 or 3.\n")[0]
  if str(answer) == "1":
    nothingness()
  elif str(answer) == "2":
    god()
  elif str(answer) == "3":
    care()
  else:
    invalidCheck = 1
    will()

#nothingness question
def nothingness():
  global invalidCheck
  clear()
  invalid()
  print("LOADING - CHECKING SYSTEM...")
  print("")
  print("Nothingness. Is there any meaning to living in this world?")
  print("1. Pray to God.")
  print("2. Hold true to your own will.")
  print("3. I dont care. I dont need any of this!")
  answer = input("Please select 1, 2 or 3.\n")[0]
  if str(answer) == "1":
    god()
  elif str(answer) == "2":
    will()
  elif str(answer) == "3":
    care()
  else:
    invalidCheck = 1
    nothingness()

#nothingness question
def god():
  global invalidCheck
  clear()
  invalid()
  print("LOADING - CHECKING SYSTEM...")
  print("")
  print("God. How did God create us?")
  print("1. By random chance.")
  print("2. From nothingness.")
  print("3. I dont care. I dont need any of this!")
  answer = input("Please select 1, 2 or 3.\n")[0]
  if str(answer) == "1":
    chance()
  elif str(answer) == "2":
    nothingness()
  elif str(answer) == "3":
    care()
  else:
    invalidCheck = 1
    god()

#nothingness question
def chance():
  global invalidCheck
  clear()
  invalid()
  print("LOADING - CHECKING SYSTEM...")
  print("")
  print("Chance. Was this world created by random chance?")
  print("1. All is according to Gods will.")
  print("2. It was not random. This world is filled with nothingness.")
  print("3. I dont care. I dont need any of this!")
  answer = input("Please select 1, 2 or 3.\n")[0]
  if str(answer) == "1":
    god()
  elif str(answer) == "2":
    nothingness()
  elif str(answer) == "3":
    care()
  else:
    invalidCheck = 1
    chance()

#nothingness question
def care():
  global invalidCheck
  clear()
  invalid()
  print("LOADING - CHECKING SYSTEM...")
  print("")
  print("The game is currently being installed.")
  print("You cannot continue playing the game until the install is completed.")
  print("Do you wish to discard everything and return to the title screen?")
  print("If you do, you will lose any unsaved data")
  answer = input("Yes or No?\n")[0].lower()
  if str(answer) == "y":
    clear()
    print("Thank you for playing!")
    sleep(1)
    clear()
    exit()
  elif str(answer) == "n":
    will()
  else:
    invalidCheck = 1
    care()

def invalid():
  global invalidCheck
  if int(invalidCheck) == 1:
    print("Invalid. Please try again.")
    invalidCheck = 0

will()