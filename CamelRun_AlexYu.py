'''
CamelRun.py
Alex Yu
Version 1.0
September 29th 2017

Playtester: Michael Chen
Comments: Game is trash. Should be deleted.
'''

import time
import math
import random

done = False


# game_end = False

thirst = 0

hunger = 0

morale = 7

days_left = 10
#
# decision_counter = 0
#
#
#

print("_____________________________________________________________________________________________________________________________________________________________________________________________")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Welcome to Raft Survival!")
print("Your boat fails somewhere over the Pacific Ocean, and you are forced to live on a raft.")
print("There's no help around and you must survive for " + str(days_left) + " days until help arrives.")

print("_______________________________________________________________________________________________________________________________________________________________")

print("You begin with a thirst level of " + str(thirst) + ", a hunger level of " + str(hunger) + ", and an overall morale level of " + str(morale) + ".")
print("If morale reaches 0, thirst reaches 5, or hunger reaches 5 before you make it to " + str(days_left) + " days, you lose the game.")



while done == False:
    print("____________________________________________________________________________________________________________________________________________________________________________________________")
    print("Today, your options are:")
    print("_____________________________________________________________________________________________________________________________________________________________________________________________")
    print("A: Eat one piece of chicken.")
    print("B: Drink one bottle of water.")
    print("C: Go fishing.")
    # print("Start paddling.")
    print("D: Rest for one day.")
    print("E: Check status.")
    print("F: Quit.")
    print("_____________________________________________________________________________________________________________________________________________________________________________________________")
    user_choice = raw_input("What do you choose?    ")
    print("____________________________________________________________________________________________________________________________________________________________________________________________")


    print("Summary of what happened yesterday:")
    print("____________________________________________________________________________________________________________________________________________________________________________________________")

    # EVENTS:

    # EVENT 1
    # SHARK CONFRONTATION
    shark_event = random.randrange(1, 5)
    if shark_event == 1:
        sharks = random.randrange(1, 3)

        hunger += sharks
        morale -= sharks

        print("You are confronted with " + str(sharks) + " shark(s).")
        print("In order to keep them at bay, you are forced to throw " + str(sharks) + " pieces of chicken overboard.")
        print("Your new morale is " + str(morale) + ", and your new hunger level is " + str(hunger) + ".")
    else:
        print("You do not encounter any sharks.")

    # EVENT 2
    # STARTS TO RAIN
    rain_event = random.randrange(1, 5)
    if rain_event == 1:

        thirst -= 1
        morale -= 1

        print("It began to rain, filling your raft with drinkable freshwater. However, it gots very cold on your raft.")
        print("This causes your thirst level to go down to " + str(thirst) + ", but your morale level to also go down to " + str(morale) + ".")

    else:
        print("It does not rain.")

    print("____________________________________________________________________________________________________________________________________________________________________________________________")

    # QUITTING CASE
    if user_choice.lower() == "f":
        print("Thanks for Playing!")
        print("____________________________________________________________________________________________________________________________________________________________________________________________")
        done = True
        break;
        # TODO:
        # p_again = raw_input("Do you want to play again? y or n:   ")
        #
        # if p_again.lower() == "y":
        #     # TODO:
        #     else p_again.lower() == "n":
            # done = True

    # WINNING CASE
    elif days_left == 0:
        print("You Win!")
        done = True

    # DEATH CASE
    elif thirst >= 5 or hunger >= 5 or morale <= 0:
        print("U died.")
        print("Your morale level is " + str(morale) + ", your hunger level is " + str(hunger) + ", and your thirst level is " + str(thirst) + ".")

        print("_______________________________________________________________________________________________________________________________________________________________")
        print("Cause of Death:")

        if thirst >= 5:
            print("Your thirst level was too high.")
        elif hunger >= 5:
            print("Your hunger level was too high.")
        elif morale <= 0:
            print("Your morale level was too low.")
        else:
            print("IDK what happened")
        print("_____________________________________________________________________________________________________________________________________________________________________________________________")
        done = True




    # EATING
    elif user_choice.lower() == "a":

        hunger -= 1
        thirst += 1
        morale -= 1
        days_left -= 1

        print("You eat chicken and gained lose one hunger! ")
        print("Your hunger level is now " + str(hunger) + ".")


    # DRINKING
    elif user_choice.lower() == "b":

        hunger += 1
        thirst -= 1
        morale -= 1
        days_left -= 1

        print("You drink one bottle of water and you lose one thirst! ")
        print("Your thirst level is now " + str(thirst) + ".")

    # FISHING
    elif user_choice.lower() == "c":

        fish_caught = random.randrange(3)

        thirst += 1
        hunger -= fish_caught
        morale += fish_caught
        days_left -= 1


        print("You go fishing and catch " + str(fish_caught) + " fish.")
        print("Your hunger level is now " + str(hunger) + " and your morale level is now " + str(morale) + ".")

        #delete in final
        print("Thirst levels: " + str(thirst))
        print("Hunger levels: " + str(hunger))
        print("Morale levels: " + str(morale))
        print("Days remaining: " + str(days_left))

    # RESTING
    elif user_choice.lower() == "d":

        thirst += 0.5
        hunger += 0.5
        morale -= 1
        days_left -= 1

        print("You spent the day resting and lost 1 morale!")
        print("Thankfully, you lose less hunger and thirst from resting, meaning that your new hunger is " + str(hunger) + " and your new thirst is now " + str(thirst) + ".")
        print("Your morale level is now " + str(morale) + ".")

    # STATUS CHECK
    elif user_choice.lower() == "e":

        thirst += 1
        hunger += 1
        morale -= 1
        days_left -= 1

        print("Thirst levels: " + str(thirst))
        print("Hunger levels: " + str(hunger))
        print("Morale levels: " + str(morale))
        print("Days remaining: " + str(days_left))


    # # WINNING CASE
    # elif days_left <= 0:
    #     print("You Win!")
    #     done = True
    #
    # # DEATH CASE
    # elif thirst >= 5 or hunger >= 5 or morale < 1:
    #     print("U died.")
    #     print("Your morale level is " + str(morale) + ", your hunger level is " + str(hunger) + ", and your thirst level is " + str(thirst) + ".")
    #
    #     print("_______________________________________________________________________________________________________________________________________________________________")
    #     print("Cause of Death:")
    #
    #     if thirst >= 5:
    #         print("Your thirst level was too high.")
    #     elif hunger >= 5:
    #         print("Your hunger level was too high.")
    #     elif morale <= 0:
    #         print("Your morale level was too low.")
    #     else:
    #         print("IDK what happened")
    #     print("_____________________________________________________________________________________________________________________________________________________________________________________________")
    #     done = True
    #
    # else:
    #     print( "\"" + str(user_choice) + "\"" + " is an invalid choice. :( ")



# print("_______________________________________________________________________________________________________________________________________________________________")
#
#
# print("Welcome to Raft Survival!")
# print("Your boat fails somewhere over the Pacific Ocean, and you are forced to live on a raft.")
# print("There's no help around and you must survive for 100 days until help arrives.")
#
# print("_______________________________________________________________________________________________________________________________________________________________")
#
# print("You begin with " + str(water_levels) + " jugs of water, " + str(food_levels) + " pieces of chicken, and an overall morale level of " + str(morale_level) + ".")
#
# while food_levels != 0 and water_levels != 0:
#
#
#     print("You are confronted with a problem right away. Your raft has sprung a leak, meaning tha"
#

# while food_levels != 0 and water_levels != 0 and morale_levels != 0:



# def outcome(outcome_number):
#
#     if outcome_number == 1:
#         print("There is a shark under your raft. He is about to rip through the raft to eat you.")
#         print("You must throw away some food.")
#         food_throwaway = input("How many pieces of chicken are you going to throw away? You have " + food_supply + " pieces.")
#         food_supply = food_supply - food_throwaway
#         return;
#     elif outcome_number == 2:
#         return;
#     elif outcome_number == 3:
#         return;
#     else:
#         print("Invalid function argument.")
#         return;
#
# outcome_number = random.randrange(5)
# print(outcome_number)
# outcome(outcome_number)
#







# yn = raw_input("Do you want to play again?  Y or N?")
#
# if yn.lower() == "y":
#
#
#
#
#
#     print("Congratulations, you won!")
