str=input("Please give the string:")
count = 0
vowels=['a','e','i','o','u']
for s in str:
    if s in vowels:
        count+=1
        
print(f'there are {count} vowels')


palidromeSrt=str[::-1]
print(palidromeSrt)
if str==palidromeSrt:
    print("Given string is palindrome")
else:
    print("Given string is not an palindrome")