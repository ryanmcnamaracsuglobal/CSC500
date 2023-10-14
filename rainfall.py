NumberOfMonths = 12

NumberOfYears = int(input("\nEnter number of years: "))

while NumberOfYears < 0:
    NumberOfYears = int(input("Error: Enter a positive number: "))

inchesOfRainfall = 0.0
totalMonths = 0
totalInchesInRainfall = 0

for year in range(NumberOfYears):
    for month in range(NumberOfMonths): 

        inchesOfRainfall = float(input("How many inches of rainfall for month #" \
                                       + str(month + 1) + " in year " + str(year + 1) + ":"))  # Added missing str()

        while inchesOfRainfall < 0:
            inchesOfRainfall = float(input("Error: Enter a positive number: "))

        totalMonths += 1
        totalInchesInRainfall += inchesOfRainfall

averageRainFall = totalInchesInRainfall / totalMonths

output = "\nNumber of Months           = " + str(totalMonths) + "\n"  
output += "Total Inches In Rainfall     = " + str(totalInchesInRainfall) + "\n"  
output += "Average Rainfall per month   = " + str(averageRainFall) + "\n"  

print(output)






