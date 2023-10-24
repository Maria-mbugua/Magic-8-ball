import random

# List of Magic 8 Ball responses
responses = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

# Function to get a random Magic 8 Ball response
def get_magic_8_ball_response():
    return random.choice(responses)

# Main function
def main():
    print("Welcome to the Magic 8 Ball Game!")
    while True:
        input("Ask a question and press Enter to shake the Magic 8 Ball...")

        response = get_magic_8_ball_response()
        print("Magic 8 Ball says:", response)

        play_again = input("Do you want to ask another question? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
