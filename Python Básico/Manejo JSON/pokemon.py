import json


def read_json():
    with open("pokemon.json","r",encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
    return data


def get_pokemon_info():
    name = input("Enter name: ")
    pokemon_type=  input("Enter type: ")
    level= int(input("Enter level: "))
    weight_kg= float(input("Enter weight: "))
    held_item= input("Enter item name name: ")
    while True:
        try:
            is_shiny = input("Is it shiny?: ")
            if is_shiny not in ["yes", "no"]:
                raise ValueError("Invalid selection")
            if is_shiny == "yes":
                is_shiny = True
            else:
                is_shiny = False
        except ValueError:
            print("Enter a valid option, yes or no")
            continue
        break
    skills = get_skills()
    stats = get_stats()
    pokemon = {
        "name": name,
        "pokemon_type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }
    return pokemon


def get_skills():
    skills = []
    for word in range(4):
        skill = input("Enter the skill: ")
        skills.append(skill)     
    return skills


def get_stats():    
    hp = int(input("Enter HP: "))
    attack = int(input("Enter Attack: "))
    defense = int(input("Enter Defense: "))
    sp_attack = int(input("Enter Special Attack:"))
    sp_defense = int(input("Enter Special Defense: "))
    speed = int(input("Enter Speed: "))

    stats = {
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "sp_attack": sp_attack,
        "sp_defense":sp_defense,
        "speed":speed

    }

    return stats


def add_to_json(data):
    pokemon = get_pokemon_info()
    if pokemon is None:
        return data
    data.append(pokemon)
    return data


def write_json(data):
    with open("pokemon.json", "w", encoding="utf8") as jsonfile:
        json.dump(data, jsonfile, indent = 4)


def main():
    data = read_json()
    add_to_json (data)
    write_json(data)

if __name__ == "__main__":
    main()
