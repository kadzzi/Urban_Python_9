def all_variants(text: str):
    maxlen = len(text)
    for size in range(1, maxlen + 1):
        for position in range(maxlen - size + 1):
            yield text[position: position + size]


a = all_variants("abc")
for i in a:
    print(i)
