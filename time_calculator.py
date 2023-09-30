# Get the time in hours
time_in_hours = int(input("Enter the current time (in hours, 0-23): "))

# Get the number of hours to wait for the alarm
wait_time = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the alarm time
alarm = (time_in_hours+ wait_time) % 24

# Alarm clock
print(f"The alarm will go off at {alarm:02}:00 hours.")




