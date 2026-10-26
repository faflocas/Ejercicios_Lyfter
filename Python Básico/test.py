import csv


def get_game_info():
    print("Create your game list")
    name = input("Enter the game name: ")
    genre = input("Enter the genre: ")
    developer = input("Enter the developer: ")
    esrb = input("Enter the ESRB rate: ")

    return name, genre, developer, esrb


def save_to_csv(game_list):
    with open("Formated_game_lsit.csv", "w", encoding="utf-8", newline="") as file:      
        writer = csv.writer(file)
        writer.writerow(["Name", "Genre", "Developer", "ESRB"])    
        writer.writerows(game_list)


def ask_to_continue():
    while True:
        try:
            answer= input("Want to add another game?")
            if answer not in ["yes", "no"]:
                raise ValueError("Invalid selection")
            return answer
        except ValueError:
            print("Enter a valid option, yes or no")


def main():
    game_list = []
    game = get_game_info()
    game_list.append(game)
    continue_adding = ask_to_continue()
    while continue_adding == "yes":
        game = get_game_info()
        game_list.append(game)
        continue_adding = ask_to_continue()
    save_to_csv(game_list)
if __name__ == "__main__":
    main()