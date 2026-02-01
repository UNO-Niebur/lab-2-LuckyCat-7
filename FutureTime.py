#FutureTime.py
#Name:Tori Gregory
#Date:2/1/26
#Assignment:Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour-6) % 12
  currentMinute = now.minute
  moreHr = int(input("Please enter hours:"))
  moreMin = int(input("Please enter minutes:" ))

  FutureMin = (currentMinute + moreMin) % 60
  extrahour = (currentMinute + moreMin) // 60
  FutureHR = (currentHour + moreHr + extrahour)
  print("The future time will be...")
  print(FutureHR, FutureMin)

  
  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
