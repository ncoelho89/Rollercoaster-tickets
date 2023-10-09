height = int(input("How tall are you in cm? "))
age = int(input("How old are you? "))
bill = 0
if height >= 120:
  print("You can right the rollercoaster")
  if age < 12:
    bill += 5
    print("Chile tickets are %5.")
  elif age <=18:
    bill += 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    bill += 0
    print("Mid life crisis tickets are $0")
  elif age > 18:
    bill += 12
    print("Adult tickets are $12.")
else:
  print("You are not tall enough to ride the rollercoaster")

wants_photo = input("Do you want a photo taken? Y or N. ")
if wants_photo == "Y":
  bill +=3

print(f"Your total bill is {bill}")