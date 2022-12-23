from art import logo,vs
from game_data import data
import random

#printing game logo
def play():
    print(logo)
    def game():
        #getting details of A
        A_index = random.randint(0,49)
        A_name = data[A_index]['name']
        A_follower_count = data[A_index]['follower_count']
        A_description =  data[A_index]['description']
        A_country = data[A_index]['country']
        #displaying details of A
        print(f"Compare A: {A_name} who is a {A_description} from {A_country}")
        #printing versus logo
        print(vs)
        #getting details of B
        B_index = random.randint(0,49)
        B_name = data[B_index]['name']
        B_follower_count = data[B_index]['follower_count']
        B_description =  data[B_index]['description']
        B_country = data[B_index]['country']
        #displaying details of B
        print(f"Compare B: {B_name} who is a {B_description} from {B_country}")
        answer = input("Enter higher or lower : ")
        if(answer == 'higher'):
            if(A_follower_count < B_follower_count):
                game()
            else:
                print("Your answer is wrong...! You Lose")
        else:
            if(A_follower_count > B_follower_count):
                game()
            else:
                print("Your answer is wrong..! You Lose")
        play_again = input("Do you want to play the game again? Type 'y' for yes and 'n' for no")
        if(play_again == 'y'):
            play()
        else:
            print("Thanks For Playing...!")
            exit()
    game()
play()
