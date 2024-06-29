def repeat(text, repetitions = 2):
    return f"{text}\n" * repetitions

text = input("Enter some text: ")
print(repeat(text))