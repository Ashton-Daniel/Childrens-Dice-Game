# Childrens Game
P1Score = 0
P2Score = 0

Number1 = 6
Number2 = 3

if Number1 == Number2:
    print("test failed 1")

elif Number1 > Number2:
    print("Test success 1")
    P1Score = Number1 + Number2

else:
    print("test failed 2")
    P1Score = Number2 + Number1



Number3 = 5
Number4 = 2


if Number3 == Number4:
    print("test failed 3")

elif Number3 > Number4:
    print("test sucess 2")
    P2Score = Number3 + Number4 

else:
    print("test failed 4")
    P2Score = Number4 + Number3



if P1Score > P2Score:
    print("Player 1 Wins")

else: 
    print("Player 2 Wins")
