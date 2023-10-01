from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
wait_time = int(input("Enter the number of hours to wait for the alarm: "))
alarm = (now.hour + wait_time) % 24
print(f"The alarm will go off at {alarm:02}:00 hours.")




