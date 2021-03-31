import sqlite3
vowels = {
    "a": ["അ", ""],
    "aa": ["ആ", "ാ"]
}

consonants = {
    "k": ["ക", "ഖ"],
    "m": ["മ", "ം"],
    "l": ["ല", "ള"]
}

chil = {
    "m": ["ം", "മ"]
}

scheme = []


def makeScheme():
    for c, cList in consonants.items():
        weight = 0
        for ci in cList:
            scheme.append({
                "combo": c,
                "i": ci,  # info
                "weight": weight,
                "type": "consonant_vowel"
            })
            weight += 1

    for c, cList in consonants.items():
        weight = 0
        for ci in cList:
            for v, vi in vowels.items():
                scheme.append({
                    "combo": c + v,
                    "i": ci + vi[1],  # info
                    "weight": weight,
                    "type": "consonant_vowel"
                })
            weight += 1


makeScheme()


def search(combo):
    r = []
    for s in scheme:
        if s["combo"] == combo:
            r.append(s)
    return r


def make(word):
    result = []

    def add(sequence):
        result.append(sequence)

    sequence = ""
    i = 0
    while i < len(word):
        ch = word[i]
        sequence += ch

        if i == len(word) - 1 and len(sequence) == 1:
            # last char
            match = search(ch)
            if len(match) == 0:
                add(ch)
            else:
                add(match)
        elif len(search(sequence)) == 0:
            print(sequence)
            if len(sequence) == 1:
                add(sequence)
            else:
                # found end, backtrack
                add(search(sequence[0:-1]))
                i -= 1
            sequence = ""

        i += 1

    return result


def flatten(tokens):
    results = []
    first = True
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if type(t) is list:
            # t is possiblities
            if first:
                for possibility in t:
                    results.append(possibility["i"])
                first = False
            else:
                for j in range(len(results)):
                    till = results[j]
                    results[j] = results[j] + t[0]["i"]
                    for k in range(1, len(t)):
                        till += t[k]["i"]
                        results.append(till)
        else:
            if first:
                results.append([t])
                first = False
            else:
                for j in range(len(results)):
                    results[j] += t
        i += 1

    return results


def transliterate(word):
    return flatten(make(word))


print(transliterate("kamalam"))
