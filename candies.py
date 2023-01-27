# to find the number of candies in jar

for candies in range(0,201):
    if(candies%5 == 2):
        if(candies%6 == 3):
            if(candies%7 == 2):
                break
                

print("The number of candies in the jar : ",candies)
