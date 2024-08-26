a = input("Enter a sentence: ")

n = int(input("Enter the minimum length n: "))
words = a.split()
longer_words = []

for x in words:
    if len(x) > n:
        longer_words.append(x)
print(longer_words)
