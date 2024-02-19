"""
Who: RJ Zack
What: Final project- black jack simulator
Where: CS125
When: 5 December 2022
"""

#GUI menu displayint rules to the user
from tkinter import *

window = Tk()
window.geometry("1000x500")
window.title("Rules")

message = Message(window, text = "Here are the rules of blackjack!", font = "200", width = 1000)
message.pack()

rule_1 = Message(window, text = "1. All number cards (2-10) score the value indicated on them. The face cards (Jack, Queen, King) score 10 points and Ace can either be treated as 1 or 11."
                 , justify = "left", width = 750)
rule_2 = Message(window, text ="2. At the beginning of each round, all players place their bets in their betting positions - also known as ‘boxes’. After the bets have been placed, all players are dealt two cards face-up in front of their respective betting positions. The dealer receives two cards, one face-up and another face-down."
                 , width = 750, justify = "left")
rule_3 = Message(window, text = "3. Starting to the left of the dealer, each player is given a chance to draw more cards. The players can either ‘hit’ or ‘stand’. If the player calls out ‘HIT’, they are given an extra card. They can then either call out ‘HIT’ again, or ‘STAND’ if they do not wish to draw any more cards. The player can ‘HIT’ as many times as they wish, but have to aim not to ‘bust’ (exceed a total of 21)."
                 , width = 750, justify = "left")
rule_4 = Message(window, text = "4. If the player busts, they immediately lose their bet."
                 , width = 750, justify = "left")
rule_5 = Message(window, text = "5. If the dealer’s hand exceeds 21, all players who didn't bust win immediately - their bet is returned along with a matching amount from the dealer's bank."
                 , width = 750, justify = "left")
rule_6 = Message(window, text ="6. If the dealer reaches a valid hand, the cards are totalled and each player’s hand is compared to the dealer’s. If the player scored higher than the dealer, they win. If the player ties with the dealer, the original bet is returned to the player. Otherwise, the player loses their bet."
                 , width = 750, justify = "left")

rule_1.pack(pady = 10)
rule_2.pack(pady = 10)
rule_3.pack(pady = 10)
rule_4.pack(pady = 10)
rule_5.pack(pady = 10)
rule_6.pack(pady = 10)

def end():
    window.destroy()
    
Button(window, text= "Exit the Window", font=("Calibri",14,"bold"), command= end).pack(pady = 20)

window.mainloop()

#self defined functions to output winning or losing screens
def winner():
    import turtle as w
    canvas = w.Screen()
    w.TurtleScreen._RUNNING=True
    w.speed(0)

    w.title('Winning Screen')

    w.hideturtle()

    w.color('green')
    w.begin_fill()
    w.up()
    w.setpos(0, -100)
    w.write('W',move = False,align ='center', font =('arial', 150))
    w.end_fill()

    w.up()
    w.setpos(0, -150)
    w.write("Yay you won! Click to return to screen." , move = False,align ='center', font =('arial', 15))
    w.down()
    w.up()

    w.setpos(0, -175)
    w.write("You will be prompt to play again or exit program!", move = False,align ='center', font =('arial', 15))

    canvas.exitonclick()
    

def loser():
    import turtle as l
    canvas = l.Screen()
    l.TurtleScreen._RUNNING=True
    l.speed(0)
    l.title('Losing Screen')

    l.hideturtle()

    l.color('red')
    l.begin_fill()
    l.up()
    l.setpos(-100,150)
    l.down()
    l.setpos(-100, -100)
    l.setpos(100,-100)
    l.setpos(100, -50)
    l.setpos(-50, -50)
    l.setpos(-50,150)
    l.setpos(-100,150)
    l.end_fill()
    
    l.up()
    l.setpos(0, -200)
    l.write("Sorry you lost! Click to return to screen." , move = False,align ='center', font =('arial', 15))
    l.down()
    l.up()

    l.setpos(0, -225)
    l.write("You will be prompt to play again or exit program!", move = False,align ='center', font =('arial', 15))

    canvas.exitonclick()
    
    

from random import *

from time import *



print("Hi! Thanks for playing blackjack with RJ!")

print(
"Limitations:"
,"\nCannot split deck when pair is orginally dealt"
, "\nOnly one user may play at a time\n")



#loop to allow the player to play until they opt not to
play = input("Do you want to play? Yes ('Y') or No ('N')? ")
play.upper()
while play == 'Y':

    print("\n\nCards are being shuffled... \n \n")
    sleep(2)

    #initializing card values and suits
    suits = [' of Hearts', ' of Spades', ' of Diamonds', ' of Clubs']
    values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']


    #dealing players first card
    pvalue_1 = choice(values)
    psuit_1 = choice(suits)

    pcard_1 = str(pvalue_1) + psuit_1

    #dealing dealers first card
    dvalue_1 = choice(values)
    dsuit_1 = choice(suits)

    dcard_1 = str(dvalue_1) + dsuit_1

    #dealing players second card
    pvalue_2 = choice(values)
    psuit_2 = choice(suits)

    pcard_2 = str(pvalue_2) + psuit_2

    #dealing dealers second card
    dvalue_2 = choice(values)
    dsuit_2 = choice(suits)

    dcard_2 = str(dvalue_2) + dsuit_2

    #output of cards to the user // including dealers
    print("Your two cards are:", pcard_1, "and", pcard_2)
    print("\nThe dealer's one card is:", dcard_2)
    print("\n")    

    #player and dealer set blank score
    phand = 0
    dhand = 0

    #chaning ace or face cards to int type to add together
    if type(pvalue_1) is str and pvalue_1 == 'Ace':
        pvalue_1 = 11
    if type(pvalue_1) is str:
        pvalue_1 = 10
    if type(pvalue_2) is str and pvalue_2 == 'Ace':
        pvalue_2 = 11
    if type(pvalue_2) is str:
        pvalue_2 = 10
    if type(dvalue_1) is str and dvalue_1 == 'Ace':
        dvalue_1 = 11
    if type(dvalue_1) is str:
        dvalue_1 = 10
    if type(dvalue_2) is str and dvalue_2 == 'Ace':
        dvalue_2 = 11
    if type(dvalue_2) is str:
        dvalue_2 = 10

    #player hand value
    phand = pvalue_1 + pvalue_2
    print("Initial hand value: ", phand, '\n\n')

    #dealer hand value
    dhand = dvalue_1 + dvalue_2


    #ask the user to hit or stay
    bet = input("Would you like to hit ('H') or stay ('S')? *input H or S for choice*: ")
    bet.upper()

    #if bet is 'H' add card to users hand
    if bet == 'H':
        #dealing players third card
        pvalue_3 = choice(values)
        psuit_3 = choice(suits)

        pcard_3 = str(pvalue_3) + psuit_3
        print("Your third card is:", pcard_3, '\n')

        #chaning ace or face cards to int type to add together
        if type(pvalue_3) is str and pvalue_3 == 'Ace':
            pvalue_3 = 11
        if type(pvalue_3) is str:
            pvalue_3 = 10
        
        phand = phand + int(pvalue_3)


        #new layer after hit to allow hit or stay still
        if phand > 21:
            if 'Ace' in pcard_1 or 'Ace' in pcard_2 or 'Ace' in pcard_3:
                phand = phand - 10

                #ask the user to hit or stay
                bet = input("Would you like to hit ('H') or stay ('S')? *input H or S for choice*: ")
                bet.upper()

                #if bet is 'H' add card to users hand
                if bet == 'H':
                    #dealing players fourth card if Ace is present 
                    pvalue_4 = choice(values)
                    psuit_4 = choice(suits)

                    pcard_4 = str(pvalue_4) + psuit_4
                    print("Your fourth card is:", pcard_4, '\n')

                    #chaning ace or face cards to int type to add together
                    if type(pvalue_4) is str and pvalue_4 == 'Ace':
                        pvalue_4 = 11
                    if type(pvalue_4) is str:
                        pvalue_4 = 10
                
                    phand = phand + int(pvalue_4)

                    #final layer for betting
                    if phand > 21:
                        if 'Ace' in pcard_1 or 'Ace' in pcard_2 or 'Ace' in pcard_3 or 'Ace' in pcard_4:
                            phand = phand - 10

                            #ask the user to hit or stay
                            bet = input("Would you like to hit ('H') or stay ('S')? *input H or S for choice*: ")
                            bet.upper()

                            #if bet is 'H' add card to users hand
                            if bet == 'H':
                                #dealing players fifth card if Ace is present 
                                pvalue_5 = choice(values)
                                psuit_5 = choice(suits)

                                pcard_5 = str(pvalue_5) + psuit_5
                                print("Your fifth card is:", pcard_5, '\n')

                            #chaning ace or face cards to int type to add together
                                if type(pvalue_5) is str and pvalue_5 == 'Ace':
                                    pvalue_5 = 11
                                if type(pvalue_5) is str:
                                    pvalue_5 = 10
                            
                                phand = phand + int(pvalue_5)


        #check if user is equal or under 21
        if phand < 22:
            
            #ask the user to hit or stay again
            bet = input("Would you like to hit ('H') or stay ('S')? *input H or S for choice*: ")
            bet.upper()

            #if bet is 'H' add card to users hand
            if bet == 'H':
                #dealing players forth card w/ no Ace
                pvalue_4 = choice(values)
                psuit_4 = choice(suits)

                pcard_4 = str(pvalue_4) + psuit_4
                print("Your fourth card is:", pcard_4, '\n')                

            #chaning ace or face cards to int type to add together
                if type(pvalue_4) is str and pvalue_4 == 'Ace':
                    pvalue_4 = 11
                if type(pvalue_4) is str:
                    pvalue_4 = 10
                
                phand = phand + int(pvalue_4)
                                

                #final layer for betting
                if phand > 21:
                        if 'Ace' in pcard_1 or 'Ace' in pcard_2 or 'Ace' in pcard_3 or 'Ace' in pcard_4:
                            phand = phand - 10

                            #ask the user to hit or stay
                            bet = input("Would you like to hit ('H') or stay ('S')? *input H or S for choice*: ")
                            bet.upper()

                            #if bet is 'H' add card to users hand
                            if bet == 'H':
                                #dealing players fifth card if Ace is present 
                                pvalue_5 = choice(values)
                                psuit_5 = choice(suits)

                                pcard_5 = str(pvalue_5) + psuit_5
                                print("Your fifth card is:", pcard_5, '\n')

                               #chaning ace or face cards to int type to add together
                                if type(pvalue_5) is str and pvalue_5 == 'Ace':
                                    pvalue_5 = 11
                                if type(pvalue_5) is str:
                                    pvalue_5 = 10
                            
                                phand = phand + int(pvalue_5)

                #ask the user to hit or stay again
                bet = input("Would you like to hit ('H') or stay ('S')? *input H or S for choice*: ")
                bet.upper()

                #if bet is 'H' add card to users hand
                if bet == 'H':
                    #dealing players fifth card w/ no Ace
                    pvalue_5 = choice(values)
                    psuit_5 = choice(suits)

                    pcard_5 = str(pvalue_5) + psuit_5
                    print("Your fifth card is:", pcard_5, '\n')                

                #chaning ace or face cards to int type to add together
                    if type(pvalue_5) is str and pvalue_5 == 'Ace':
                        pvalue_5 = 11
                    if type(pvalue_5) is str:
                        pvalue_5 = 10
                
                    phand = phand + int(pvalue_5)

                
                elif bet == 'S':
                    pass

                else:
                    print("Wrong input. You may be cheating restart.\n")
                    

    #if bet is 'S' move to score dealers hand 
    elif bet == 'S':
        pass 

    else:
        print("Wrong input. You may be cheating restart.\n")


    print("\nFinal user hand value: ", phand)
    




    #Reveal delear's second card
    print("\nDealer's cards shown are ", dcard_1, "and", dcard_2)
    print("Dealer hand value: ", dhand)
    

    if dhand < 17:
        #dealing dealers third card
        dvalue_3 = choice(values)
        dsuit_3 = choice(suits)

        dcard_3 = str(dvalue_3) + dsuit_3
        print("\nDealer's third card is:", dcard_3)                

        #chaning ace or face cards to int type to add together
        if type(dvalue_3) is str and dvalue_3 == 'Ace':
            dvalue_3 = 11
        if type(dvalue_3) is str:
            dvalue_3 = 10
                
        dhand = dhand + int(dvalue_3)

        #check if over 21 and if hand contains Ace
        if dhand > 21:
            if 'Ace' in dcard_1 or 'Ace' in dcard_2 or 'Ace' in dcard_3:
                phand = dhand - 10
 
                dvalue_4 = choice(values)
                dsuit_4 = choice(suits)

                dcard_4 = str(dvalue_4) + dsuit_4
                print("Dealer's fourth card is:", dcard_4)

                #chaning ace or face cards to int type to add together
                if type(dvalue_4) is str and dvalue_4 == 'Ace':
                    dvalue_4 = 11
                if type(dvalue_4) is str:
                    dvalue_4 = 10
                
                dhand = dhand + int(dvalue_4)

                #final layer for dealer hit
                if dhand > 21:
                    if 'Ace' in dcard_1 or 'Ace' in dcard_2 or 'Ace' in dcard_3 or 'Ace' in dcard_4:
                        dhand = dhand - 10

                        #drawin fifth and final card
                        dvalue_5 = choice(values)
                        dsuit_5 = choice(suits)

                        dcard_5 = str(dvalue_5) + dsuit_5
                        print("Dealer's fifth card is:", dcard_5)

                    #chaning ace or face cards to int type to add together
                        if type(dvalue_5) is str and dvalue_5 == 'Ace':
                            dvalue_5 = 11
                        if type(dvalue_5) is str:
                            dvalue_5 = 10
                            
                        dhand = dhand + int(dvalue_5)


    if dhand < 17:
        #dealing dealers fourth card
        dvalue_4 = choice(values)
        dsuit_4 = choice(suits)

        dcard_4 = str(dvalue_4) + dsuit_4
        print("Dealer's fourth card is:", dcard_4)                

        #chaning ace or face cards to int type to add together
        if type(dvalue_4) is str and dvalue_4 == 'Ace':
            dvalue_4 = 11
        if type(dvalue_4) is str:
            dvalue_4 = 10
                
        dhand = dhand + int(dvalue_4)

        #final layer for dealer hit
        if dhand > 21:
            if 'Ace' in dcard_1 or 'Ace' in dcard_2 or 'Ace' in dcard_3 or 'Ace' in dcard_4:
                dhand = dhand - 10

                #drawin fifth and final card
                dvalue_5 = choice(values)
                dsuit_5 = choice(suits)

                dcard_5 = str(dvalue_5) + dsuit_5
                print("Your fifth card is:", dcard_5)

            #chaning ace or face cards to int type to add together
                if type(dvalue_5) is str and dvalue_5 == 'Ace':
                    dvalue_5 = 11
                if type(dvalue_5) is str:
                    dvalue_5 = 10
                            
                dhand = dhand + int(dvalue_5)


    if dhand < 17:
        #dealing dealers fifth card
        dvalue_5 = choice(values)
        dsuit_5 = choice(suits)

        dcard_5 = str(dvalue_5) + dsuit_5
        print("Dealer's fifth card is:", dcard_5)                

        #chaning ace or face cards to int type to add together
        if type(dvalue_5) is str and dvalue_5 == 'Ace':
            dvalue_5 = 11
        if type(dvalue_5) is str:
            dvalue_5 = 10
                
        dhand = dhand + int(dvalue_5)

    print("\nDealer's final hand is:", dhand)


    #Score comparison
    if phand > dhand and phand < 22:
        print("\n\n*Winning screen is being outputted (Different window)*")
        sleep(2)
        #winning screen
        winner()

    elif dhand > 22 and phand < 22:
        print("\n\n*Winning screen is being outputted* (Different window)")
        sleep(2)
        #winning screen
        winner()

    else:
        print("\n\n*Losing screen is being outputted* (Different window)")
        sleep(2)
        #losing screen
        loser()
        
    #ending or continuing while loop
    play = input("\n\nDo you want to play again? Yes ('Y') or No ('N')? ")
    play.upper()
