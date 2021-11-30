def encryptChar(ch, n):
    if ch == "" or ch == " " or ch == '\n':
        return ch
    ch = ch.lower()
    a_num = ord('а')
    ya_num = ord('я')

    if a_num <= ord(ch) <= ya_num:
        new_ord = ord(ch) + n
        if new_ord > ya_num:
            new_ord = new_ord + a_num - ya_num - 1
        return chr(new_ord)
    return ""


if __name__ == '__main__':
    n = 10

    inp = open("source.txt", 'r', encoding="utf8")
    out = open("encrypted.txt", 'w', encoding="utf8")

    char = inp.read(1)
    out.write(encryptChar(char, n))

    while char:
        char = inp.read(1)
        out.write(encryptChar(char, n))

    inp.close()
    out.close()
