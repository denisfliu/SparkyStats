import os

from src.sqbs import Matches

if __name__ == "__main__":
    print("Enter Tournament Folder (folder with roster.xlsx and stats sheets): ")
    path = input()
    matches = Matches(path)
    with open(os.path.join(path, f"{matches.general_config.name}.sqbs"), "w") as writer:
        sqbs = matches.compile_sqbs_string()
        writer.write(sqbs)
