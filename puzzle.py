# puzzle.py

def puzzle():
    print("Welcome!")
    print("Fortune favors the brave")
    
    print("""
    You have been given a task to monitor a space mission.
    The launch time was recorded, but the next critical event happens at a specific time.
    You are asked when this event will take place.
    
    Clue:
    'When the clock strikes one day after the rocket soars, 
    What time will the countdown reach before the mission roars?'
    
    Take your time to figure it out...
    """)
    
    # Get user input to "solve" the puzzle
    answer = input("What is your answer? ")
    
    if answer.lower() == "24 hours after launch":
        print("Congratulations! You solved the puzzle correctly.")
    else:
        print("Oops! That's not quite right. Try again!")

# Call the puzzle function to present the challenge
puzzle()
