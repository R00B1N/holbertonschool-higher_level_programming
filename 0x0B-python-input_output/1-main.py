#!/usr/bin/python3
write_file = __import__('3-write_file').write_file

nb_characters = write_file("my_first_file.txt", "Holberton School is so cool!\n")
print(nb_characters)
write_file("my_first_file.txt", "Holberton School is so cooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooool!\n")
with open("my_first_file.txt") as f:
    print(f.read(), end="")
