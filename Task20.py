word = input("Введите слово: ").upper()
dictionary_ENG = {1: "AEIOULNSTR",
                  2: "DG",
                  3: "BCMP",
                  4: "FHVWY",
                  5: "K",
                  8: "JZ",
                 10: "QZ"}
dictionary_RU = {1: 'АВЕИНОРСТ',
                 2: 'ДКЛМПУ',
                 3: 'БГЬЯ',
                 4: 'ЙЫ',
                 5: 'ЖЗХЦЧ',
                 8: 'ШЭЮ',
                10: 'ФЩЪ'}
points = 0
for key, value in dictionary_ENG.items():
    for el in value:
        for i in range(len(word)):
            if word[i] == el:
                points += key
for key, value in dictionary_RU.items():
    for el in value:
        for i in range(len(word)):
            if word[i] == el:
                points += key
print(points)

