ch = input("Enter a character: ")

# Convert to lowercase to handle both upper and lower case
ch = ch.lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print("It is a vowel")
else:
    print("It is a consonant")