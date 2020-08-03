# Small Exercise 5. Work or Sleep?

def work_or_sleep():
    day = int(input("Pick a day of the week using (0-6)? "))
    if (day == 0) or (day == 6):
        print("Sleep in!")
        work_or_sleep()
    elif day > 6:
        print("You are out of range.")
        work_or_sleep()
    else:
        print("Go to work!")
work_or_sleep()