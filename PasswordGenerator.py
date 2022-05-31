#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwordLenght = nr_letters + nr_symbols + nr_numbers
password = ""

for character in range (0, nr_letters):
  password = password + letters[random.randint(0, len(letters)-1)]


for number in range (0, nr_numbers):
  password = password + numbers[random.randint(0,9)]

for symbol in range (0, nr_symbols):
  password = password + symbols[random.randint(0, len(symbols)-1)]

myPass = list(password)

myPass_shuffle = random.sample(myPass, len(myPass)) #This is using the python sample method. Another less complicated way to shuffle a string is simply using random.shuffle(). My mistake was that I thought I had to "store" the shuffled password in a new variable, but thisd is not needed
#this would be the easier, cleaner way:
#myPass = list(password) #This is to turn the string into a list and be able to have it "broken down" into individual elements that I then can shuffle.
#random.shuffle(myPass)
#print(myPass) #This should return our shuffled password. We can now use it, no need to save it inside a new variable

final_pass = ""
for characters in myPass_shuffle:
  final_pass += characters

print(password)
print(myPass_shuffle)

