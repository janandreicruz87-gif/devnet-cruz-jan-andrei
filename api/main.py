import requests
import random

pokemon_list = ["bulbasaur", "charmander", "squirtle", "rattata", "weedle"]

pokemon_name = random.choice(pokemon_list)

try:
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        pokemon = response.json()

        name = pokemon["name"]
        height = pokemon["height"] / 10
        weight = pokemon["weight"] / 10
        abilities = []

        for ability in pokemon["abilities"]:
            abilities.append(ability["ability"]["name"])

        print("=== Pokemon Guessing Game ===")
        print("Guess which Pokemon I selected!")
        print("You have 3 attempts.")
        print()
        print("Height:", height, "meters")
        print("Weight:", weight, "kilograms")
        print("Abilities:", ", ".join(abilities))
        print()

        attempts = 3

        while attempts > 0:
            guess = input("Enter Pokemon name: ").lower().strip()

            if guess not in pokemon_list:
                print("Invalid Pokemon! Choose from the list:")
                print(pokemon_list)

            elif guess == name:
                print("Correct! You win!")
                print("The Pokemon is", name.title())
                break

            else:
                attempts = attempts - 1
                print("Wrong guess!")

                if attempts > 0:
                    print("Attempts left:", attempts)
                else:
                    print("Game over!")
                    print("The correct Pokemon is", name.title())

    else:
        print("Error getting Pokemon data.")

except requests.exceptions.RequestException:
    print("Connection error! Please check your internet.")

except (KeyError, TypeError):
    print("There was a problem reading the Pokemon data.")
