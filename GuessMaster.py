import random
import math
starting_value = int(input("enter the starting_value "))
ending_value = int(input("enter the ending_value "))
random_no = random.randint(starting_value,ending_value)
print("The No. of chance's you have to play the game are", str(round(math.log( ending_value- starting_value + 1 ,2))))
count=0
while count< math.log(ending_value - starting_value + 1,2):
    count+=1
    target = int(input())
    if random_no == target:
        print("HU REEE!! you Got the number",str(target),"in",str(count),"\U0001f607")
        break
    elif target < random_no:
        print("You are to low","\U0001f616")
    else:
        print("you are too high","\U0001f630")
if count >= math.log(ending_value -starting_value +1,2):
    print("The number is",str(random_no),"\U0001f611")
    print("BETTER LUCK NEXT TIME","\U0001f614")
