def decipher_this(s):
    words = s.split()
    result = []

    for word in words:
        num = ''
        i = 0
        while i < len(word) and word[i].isdigit():
            num += word[i]
            i += 1
        
        first_char = chr(int(num))
        rest = list(word[i:])

        if len(rest) >= 2:
            rest[0], rest[-1] = rest[-1], rest[0]

        decoded_word = first_char + ''.join(rest)
        result.append(decoded_word)

    return ' '.join(result)