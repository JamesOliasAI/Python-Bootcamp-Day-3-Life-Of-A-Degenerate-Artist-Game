print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Life of a Degenerate Artist.")
print("Your mission is to be successful it in the music industry.")
decision1 = str(input("You walk into the studio full of the best artists in the industry and one of them asks you to play a song on the speakers.\nType 'yes' to play your song or 'no' to aurafarm in mystery."))
if decision1 == "yes":
    print("You played your best song but everyone in the studio said your mix was trash and you should quit making music.\nYOU LOSE!")
elif decision1 == "no":
    decision2 = str(input("They was intrigued by your mysterious aura and invited you to the after party they got after studio.\nType 'yes' to go to it or 'no' to go home after."))
    if decision2 == "yes":
        decision3 = str(input("You arrived at the party and a sexy emo girl walks up to you.\nShe asks you if you wanna stay at her place tonight instead of staying at the party.\nType 'yes' to go back to her house or 'no' to stay at the party."))
        if decision3 == "yes":
            print("You have fallen into the eternal loop of goth girl withdrawals and cannot think of making music ever again due to your condition.\nYOU LOSE!")
        elif decision3 == "no":
            decision4 = str(input("You decided to stay at the party and had a great time... you feel inspired!\nWith your new found inspiration you ask yourself whether you should go record a new song or not.\nType 'yes' to go record a new song or 'no' to just go home."))
            if decision4 == "yes":
                decision5 = str(input("You just recorded the best song you've ever made before, you can't believe it.\nYou've come to your final and most important decision you'll ever make...\nShould you release it?\nType 'yes' to release the song or 'no' to forget about it."))
                if decision5 == "yes":
                    print("You released your song and it just went viral on social media!\nYou've gain overnight fame and made it to the mainstream.\nYou finally left your shitty job, bought your mum a house and continued being the greatest artist in the world for the rest of your career.\nCONGRATULATIONS! YOU WIN!!!")
                elif decision5 == "no":
                    print("You never released your music like you always do and you ended up working at your local corner shop as a shelf stacker for the rest of your life\nYOU LOSE!")
            elif decision4 == "no":
                print("You went home and fell asleep...\nYou wake up in the morning to realise that the drink you had was spiked!\nYour vocal chords have been sliced from the drugs and your never able to record another song ever again.\nYOU LOSE!")
    elif decision2 == "no":
        print("You went home thinking about what life could have been like if you just went to the party and gooned yourself to sleep.\nYOU LOSE!")
else:
    print("You didn't select a valid option and froze under the pressure.\nYOU LOSE!")
