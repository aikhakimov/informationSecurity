if __name__ == '__main__':
    inp = open("encrypted.txt", 'r', encoding="utf8")
    frequencies = dict()

    ch = inp.read(1)
    if ch != "" and ch != " " and ch != '\n' and ch not in frequencies:
        frequencies[ch] = 1
    elif ch in frequencies:
        frequencies[ch] += 1

    while ch:
        ch = inp.read(1)
        if ch != "" and ch != " " and ch != '\n' and ch not in frequencies:
            frequencies[ch] = 1
        elif ch in frequencies:
            frequencies[ch] += 1

    for key in frequencies:
        print(key, frequencies[key])

    fr_list = ["о", "е", "а", "и", "н", "т", "с", "р", "в", "л", "к", "м", "д", "п", "у", "я", "ы", "ь", "г", "з", "б",
               "ч", "й", "х", "ж", "ш", "ю", "ц", "щ", "э", "ф", "ъ"]

    replacements = dict()

    i = 0
    for letter in sorted(frequencies.items(), key=lambda x: -1 * x[1]):
        replacements[letter[0]] = fr_list[i]
        i += 1

    replacements[' '] = ' '
    replacements['\n'] = '\n'
    replacements[''] = ""

    inp = open("encrypted.txt", 'r', encoding="utf8")
    out = open("decrypted.txt", 'w', encoding="utf8")

    char = inp.read(1)
    out.write(replacements[char])

    while char:
        char = inp.read(1)
        out.write(replacements[char])

