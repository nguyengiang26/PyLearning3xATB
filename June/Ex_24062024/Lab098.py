letters = ['a', 'b', 'c', 'd', 'e']

def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels

filtered_letters = filter(filter_vowels, letters)
print(list(filtered_letters))  # Output: ['a', 'e']
