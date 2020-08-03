# Small Exercise 4. Day of the Week

# Prompt the user for a day number. The user will enter a number from 0 to 6. Given this number, print a day of the week. 0 for Sunday, 1 for Monday, 2 for Tuesday, and so on.

def day_numbers():
     day = int(input("Pick a day of the week using (0-6)? "))
     if day == 0:
         print("Sunday")
         day_numbers()
     elif day == 1:
         print("Monday")
         day_numbers()
     elif day == 2:
         print("Tuesday")
         day_numbers()
     elif day == 3:
         print("Wednesday")
         day_numbers()
     elif day == 4:
         print("Thursday")
         day_numbers()
     elif day == 5:
         print("Friday")
         day_numbers()
     elif day == 6:
         print("Saturday")
day_numbers()