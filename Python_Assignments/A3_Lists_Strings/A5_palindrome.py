# Ask user to enter a number
number = int(input("Enter a number: "))

# store the user entered number
user_entered_number = number

# create a variable for the reversed number otuside the loop
reverse = 0

# repeat until all digits are processed
while number > 0:
    # Get the last digit
    last_digit = number % 10
    # Add the digit to the reverse
    reverse = reverse * 10 + last_digit
    # Remove the last digit to proceed the next digit
    number = int(number / 10)

# print the result
print("Reverse of", user_entered_number, "is", reverse)

# check wheather the number is palindrome or not
if user_entered_number==reverse:
    # Print the result if number is palindrome
    print("Result: Palindrome")
else:
    # Print the result if number is not an palindrome
    print("Result: Not Palindrome")
    