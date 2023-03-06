# 9. Check for Leap year:

print("Check for a Leap year")
your_year = int(input("Please type up a year you would like to check for a Leap year here: " ))
leap_year = your_year % 4 == 0 and (your_year % 100 != 0 or your_year % 400 == 0)
if leap_year:
  print(f"Year {your_year} is a Leap year.")
else:
  print(f"Year {your_year} is not a Leap year.")

# 9.1. Check for Leap year (another way):

print("Check for a Leap year")
your_year = int(input("Please type up a year you would like to check for a Leap year here: " ))
if your_year % 4 == 0:
  if your_year % 100 == 0:
    if your_year % 400 == 0:
      print(f"Year {your_year} is a Leap year.")
    else:
      print(f"Year {your_year} is not a Leap year.")
  else:
    print(f"Year {your_year} is a Leap year.")
else:
  print(f"Year {your_year} is not a Leap year.")
