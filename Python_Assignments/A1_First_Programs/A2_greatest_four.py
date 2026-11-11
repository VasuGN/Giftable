a=int(input("Please give a value:"))
b=int(input("Please give b value:"))
c=int(input("Please give c value:"))
d=int(input("Please give d value:"))
def highestNum(a,b,c,d):
    highestValue = a
    
    if b>=highestValue:
        highestValue=b
    if c>=highestValue:
        highestValue=c
    if d>=highestValue:
        highestValue=d
            
    return highestValue

print(highestNum(a,b,c,d))

