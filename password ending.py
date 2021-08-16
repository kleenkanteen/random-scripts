def letters(two):
    if not two.isalpha() or len(two) != 2:
        print("Invalid input")
    else:
        new = ""
        for letter in two:
            letter = letter.lower()
            new += str((ord(letter) - 96))
        print(new)


interest = input("First 2 letters of the site, result is in lowercase: ")
letters(interest)
