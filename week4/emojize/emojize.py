import emoji

text= input("Enter text: ")
result = emoji.emojize(text, language="alias")
print(f"Output: {result}")
