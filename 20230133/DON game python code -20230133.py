import sys
import random
import datetime

# Initialize game variables and user inputs
User_Name = input("Player name: ")
Life_score = random.randint(1, 50)
attempts = 1
Enemies = []
text_data = []
Status = ""
Choose_No = 0

Max_Chances = 20  # Maximum chances to play the game

# Function to append game data to a list
def list_append():
    # Append various game-related information to the text_data list
    # for later use in file generation
    text_data.append(f"Attempt Number: {attempts}")
    text_data.append(f"Presented Enemies: {Enemies}")
    text_data.append(f"Inputed Number: {Choose_No}")
    text_data.append(f"Status of the game: {Status}")
    text_data.append(f"Life Score: {Life_score}\n")

# Function to display the current game status
def game_status():
    print("\n\n\n*** Game Status ***")
    print(f"Player name: {User_Name}")
    print(f"Total attempts: {attempts}")
    print(f"Final life score: {Life_score}")

# Function to generate a file with game session details
def generate_file(text_data):
    # Generate a unique file name using date, time, and a random number
    current_dt = datetime.datetime.now()
    date_format = current_dt.strftime("%Y_%m_%d")
    time_format = current_dt.strftime("%H_%M_%S_%f")[:-6]
    Rand_No = random.randint(0, 9999)
    file_name = f"{date_format}_{time_format}{Rand_No}.txt"

    # Write game session details to a file
    with open(file_name, 'w') as file:
        file.write("-------------------------------\n")
        file.write("  *** Game Session Details ***\n")
        file.write("-------------------------------\n\n")
        file.write(f"Player name : {User_Name}\n\n")
        file.write(f"Life Score : {Life_score}\n\n\n")
        for data in text_data:
            file.write(data + "\n\n")
        file.write("\n\nEnd Game Statistics\n")
        if attempts == 21:
            file.write(f"Congratulations!! {User_Name} defeated the enemies and You Won the battle")
        else:
            file.write(f"Game Over!! {User_Name} could not defeat the enemies and You lost the battle")

# Main game loop
while attempts <= Max_Chances:
    # Logic to determine the strength of enemies based on the number of attempts
    if attempts <= 5:
        for _ in range(1, 6):
            Rand_No = random.randint(15, 100)
            Enemies.append(Rand_No)
    elif attempts <= 10:
        for _ in range(1, 6):
            Rand_No = random.randint(250, 2000)
            Enemies.append(Rand_No)
    elif attempts <= 15:
        for _ in range(1, 6):
            Rand_No = random.randint(3000, 10000)
            Enemies.append(Rand_No)
    else:
        for _ in range(1, 6):
            Rand_No = random.randint(20000, 100000)
            Enemies.append(Rand_No)
    
    # Display current game information
    print(f"Attempts : {attempts}")
    print(f"{User_Name}'s life score is : {Life_score}")
    print("Presented Enemies:", Enemies)
    
    try:
        # Get user input to select an enemy to fight
        Choose_No = int(input("Select a number to fight: "))
        if Choose_No in Enemies:
            if Life_score >= Choose_No:
                # If the chosen enemy is defeated, update life score and status
                print(f"{User_Name} killed {Choose_No}\n")
                Life_score += Choose_No
                Status = "You Won the game"
            else:
                # If the user loses, display the final status and end the game
                print(f"{Choose_No} killed {User_Name}\n")
                game_status()
                print(f"{User_Name} was defeated!!!")
                Status = "You Lost the game DON has fallen"
                list_append()
                generate_file(text_data)
                break
        else:
            # If the chosen enemy does not exist, end the game
            print("No such enemy")
            Status = "You Lost the game No such enemy and DON has fallen"
            game_status()
            print(f"{User_Name} was defeated!!!")
            list_append()
            generate_file(text_data)
            sys.exit()
    except ValueError:
        # If an invalid input is entered, end the game
        print("Invalid input, Game Over!!")
        Status = "Invalid Input and You Lost the game DON has fallen"
        list_append()
        generate_file(text_data)
        sys.exit()

    # Append game data for this attempt and increment attempts counter
    list_append()
    attempts += 1
    Enemies.clear()  # Clear the list of enemies for the next round

else:
    # Display final game status if maximum attempts are reached
    game_status()
    print(f"{User_Name} saved the day!")
    generate_file(text_data)
