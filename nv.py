import sqlite3
vowels = {
    "a": ["അ", ""],
    "aa": ["ആ", "ാ"],
    "i": ["ഇ", "ി"],
}

consonants = {
    "k": ["ക", "ഖ"],
    "m": ["മ", "ം"],
    "l": ["ല", "ള"],
    "L": ["ള"],
    "v": ["വ"],
    "t": ["റ്റ"],
    "th": ["ത"],
}

chil = {
    "m": ["ം", "മ"],
    "l": ["ൽ", "ല"]
}

scheme = []


def makeScheme():
    for c, cList in vowels.items():
        scheme.append({
            "combo": c,
            "i": cList,  # info
            "weight": 0,
            "type": "vowel"
        })

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
# print(scheme)


def search(combo, first=False):
    r = []
    for s in scheme:
        if s["combo"] == combo:
            t = s
            if s["type"] == "vowel":
                if first:
                    t["i"] = t["i"][0]
                else:
                    t["i"] = t["i"][1]
            r.append(t)
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
            if ch in chil:
                add(chil[ch][0])
            else:
                match = search(ch, i == 0)
                if len(match) == 0:
                    add(ch)
                else:
                    add(match)
        elif len(search(sequence)) == 0:
            if len(sequence) == 1:
                add(sequence)
            else:
                # found end, backtrack
                add(search(sequence[0:-1], i == 0))
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
                    results.append([possibility["i"], possibility["weight"]])
                first = False
            else:
                for j in range(len(results)):
                    till = results[j][0]
                    tillWeight = results[j][1]

                    results[j][0] += t[0]["i"]
                    results[j][1] += t[0]["weight"]

                    for k in range(1, len(t)):
                        till += t[k]["i"]
                        tillWeight += t[k]["weight"]
                        results.append([till, tillWeight])
        else:
            if first:
                results.append([t, 0])
                first = False
            else:
                for j in range(len(results)):
                    results[j][0] += t
        i += 1

    return results


def transliterate(word):
    return flatten(make(word))


print(transliterate("kaaaaaaaaa"))
