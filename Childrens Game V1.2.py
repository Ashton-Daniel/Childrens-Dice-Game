# Childrens Game
#Random Numbers:
import random

#Set the scores to 0
P1Score = 0
P2Score = 0

Number1 = 0
Number2 = 0
Number3 = 0
Number4 = 0

# Generate 2 random numbers between 1 and 6 inclusive and place them in variables Number1 and Number2
Number1 = random.randint(0, 6)
print(Number1)
Number2 = random.randint(0, 6)
print(Number2)

#If the player rolls the dice they lose
if Number1 == Number2:
    print("Player 1 rolled a double therefore player 2 wins")
    exit()
    
#Ordering the numbers
elif Number1 > Number2:
    P1Score = str(Number1) + str(Number2)

else:
    P1Score = str(Number2) + str(Number1)



#Generate 2 random numbers between 1 and 6 inclusive and place them in variables Number3 and Number4
Number3 = random.randint(0, 6)
print(Number3)
Number4 = random.randint(0, 6)
print(Number4)

#If the player rolls the dice they lose
if Number3 == Number4:
    print("Player 2 rolled a double therefore player 1 wins")
    exit()

#Ordering the numbers
elif Number3 > Number4:
    P2Score = str(Number3) + str(Number4) 

else:
    P2Score = str(Number4) + str(Number3)


#Comparing the scores to find the winner
if int(P1Score) > int(P2Score):
    print(str(P1Score) + ">" + str(P2Score))
    print("Player 1 Wins")

elif int(P2Score) > int(P1Score):
    print(str(P2Score) + ">" + str(P1Score))
    print("Player 2 Wins")

else:
    print(str(P1Score) + "=" + str(P2Score))
    print("It's a tie! Both players rolled a " + str("P1Score"))