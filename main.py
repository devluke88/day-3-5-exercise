# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total1 = 0
total2 = 0

names = (name1+name2).lower()
total1 = names.count("T".lower()) + names.count("R".lower()) + names.count("U".lower()) + names.count("E".lower())

total2 = names.count("L".lower()) + names.count("O".lower()) + names.count("V".lower()) + names.count("E".lower())

love_score = str(total1)+str(total2)
total_love = int(love_score)

if total_love < 10 or total_love > 90:
  print(f"Your score is {total_love}, you go together like coke and mentos.")
elif total_love >=40 and total_love <=50:
  print(f"Your score is {total_love}, you are alright together.")
else:
  print(f"Your score is {total_love}.")