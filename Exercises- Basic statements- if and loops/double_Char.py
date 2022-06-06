command = input()

while command != "End":
    if command == "SoftUni":
        sentence = command
        new_sentence = ""
        for char in sentence:
            new_sentence += char * 2
    else:
        sentence = command
        new_sentence = ""
        for char in sentence:
            new_sentence += char * 2
        print(new_sentence)

    command = input()
