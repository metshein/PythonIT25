mapping = {
    "000": "tere",
    "001": "maailm",
    "010": "ago",
    "011": "robot",
    "100": "taltech",
    "101": "lahe",
    "110": "on",
    "111": "ja"
}

line = input().strip()
codes = line.split()

translated = []

for code in codes:
    word = mapping[code]
    translated.append(word)

print(" ".join(translated))
