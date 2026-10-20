import os

def read_txt_lines():
    directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, "songs.txt")
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def sort_txt_lines(lines):  
    lines.sort()
    return lines


def write_txt_lines(sorted_lines):
    with open("sorted_songs.txt", "w", encoding="utf-8") as file:
        for line in sorted_lines:
            file.write(line)


def main():
    lines = read_txt_lines()  
    sorted_lines=sort_txt_lines(lines)
    write_txt_lines(sorted_lines)


if __name__ == "__main__":
    main()