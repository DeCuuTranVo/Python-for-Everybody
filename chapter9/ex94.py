name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

word_dict = {}

for line in handle:
    if (line.startswith("From ")):
        line = line.rstrip()
        word_list = line.split()
        word = word_list[1]
        word_dict[word] = word_dict.get(word, 0) + 1
        
# print(word_dict)
max_word = None
max_freq = 0
for word, freq in word_dict.items():
    if freq > max_freq:
        max_word = word
        max_freq = freq

print(max_word, max_freq)
