# multiplication game for kids

import random
for i in range(1,11):
    a = random.randint(0,9)
    b = random.randint(0,9)
    prod = a*b
    s = a," x " ,b, " = "
    pgiven = int(input (s))
    if(prod == pgiven):
        print("Correct answer BRAVO")
    else:
        print("Wrong answer \n the answer = ",prod)

        
