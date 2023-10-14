number_of_books = int(input("Enter the number of books: "))
message = ""

if number_of_books < 0:
    message = "Error: Enter a positive number. \n" + \
              "Re-run program and try again"

else:

    message =  "You  are  awarded "

    if number_of_books >= 0 and number_of_books <= 1:
        message += "0"
    elif number_of_books >= 2 and number_of_books <=3:
        message += "5"
    elif number_of_books >= 4 and number_of_books <=5:
        message += "15"
    elif number_of_books >= 6 and number_of_books <=7:
        message += "30"
    elif number_of_books >= 8:
        message += "60"
    message += " points."

    
print(message)





