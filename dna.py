from sys import argv
import csv

if len(argv) != 3:
    print("python dna.py [DATABASE..] [SEQUENCE..]")
    exit()

with open(argv[1], mode="r") as database:
    reader = csv.DictReader(database)
    STR = []
    profiles = []
    STR = reader.fieldnames[1:]
    for row in reader:
        profiles.append(row)

str_count = dict.fromkeys(STR, 0)

def repeats(sequence, STR):
    L = len(STR)

    max_repeats = 0
    for i in range(len(sequence)):
        repeats = 0

        if sequence[i: (i + L)] == STR:
            repeats += 1

            while sequence[i: i + L] == sequence[i + L: i + (2 * L)]:
                repeats += 1
                i += L
        if repeats > max_repeats:
            max_repeats = repeats

    return max_repeats


with open(argv[2], "r") as sequence_:
    sequence = sequence_.readlines()
    sequence = sequence[0].strip("\n")
    # TODO: Check for repeats in DNA profile, and then add them to the str_count dictionary
    for str in STR:
        str_count[str] = repeats(sequence, str)


for profile in profiles:
    matches = 0
    for str in STR:
        if int(profile[str]) != str_count[str]:
            continue
        matches += 1

        if matches == len(STR):
            print(profile["name"])
            exit()


print("No Match")
exit()
