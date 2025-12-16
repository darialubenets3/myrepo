def min_letters_to_palindrome(word):
    n = len(word)
    for i in range(n + 1):
        if word + word[:i][::-1] == (word + word[:i][::-1])[::-1]:
            return i
    return n

t = int(input("Скільки слів будете вводити? "))

for _ in range(t):
    word = input("Введіть слово: ")
    print(min_letters_to_palindrome(word))
