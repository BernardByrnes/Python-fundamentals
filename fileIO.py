# my_file = open('sample.txt')

# with open('sample.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
# print(text)


# with open('sample.txt', 'r+', encoding='utf-8') as f:
#     text = f.write("am another bro")
# print(text)


# with open('sample.txt', 'a', encoding='utf-8') as f:
#     text = f.write("🤣😂😂")
# print(text)

# with open('sample.txt', 'w', encoding='utf-8') as f:
#     text = f.write("😎😎😋😊😊")
# print(text)

with open('sad.pdf', 'w', encoding='utf-8') as f:
    text = f.write("damn!!")
print(text)


# with open('sample.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line.rstrip('\n'))