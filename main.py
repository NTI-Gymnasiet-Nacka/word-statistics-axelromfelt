# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje:
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)
LETTERS = "qwertyuiopasdfghjklzxcvbnmåöäQWERTYUIOPASDFGHJKLZXCVBNMÖÄÅ "


def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def count_words(text: list):
    x = 0
    text = "".join(text)
    text = text.replace("\n", " ")
    for character in text[::-1]:
        if character not in LETTERS:
            text = text.replace(character, "")
    x += len(text.split())
    return x


def most_frequent(text: list):
    text = "".join(text)
    text = text.replace("\n", " ")
    for character in text[::-1]:
        if character not in LETTERS:
            text = text.replace(character, "")
    text = text.lower().split()
    text.sort()
    # dict = {}
    # for word in text:
    #     if word in dict:
    #         dict[word] += 1
    #     else:
    #         dict[word] = 1
    # print(dict)
    # return max(dict, key=lambda word: dict[word])
    old_count = 0
    top_word = []
    for word in text:
        count = 0
        for i in range(0, len(text)):
            if text[i] == word:
                count += 1


def main():

    # Här har du nu en lista av strängar från den inlästa filen.
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt")
    print(count_words(sentences))
    print(most_frequent(sentences))


if __name__ == "__main__":
    main()
