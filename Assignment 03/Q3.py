# Function to count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# Function to count consonants
def count_consonants(s):
    count = 0
    for ch in s:
        if ch.isalpha() and ch.lower() not in "aeiou":
            count += 1
    return count


# Function to calculate ratio of vowels to consonants
def vowel_consonant_ratio(vowels, consonants):
    if consonants == 0:
        return "Undefined (no consonants)"
    return vowels / consonants


# Main program
string = input("Enter a string: ")

v = count_vowels(string)
c = count_consonants(string)
ratio = vowel_consonant_ratio(v, c)

print("\nNumber of vowels     :", v)
print("Number of consonants:", c)
print("Vowels : Consonants :", ratio)
