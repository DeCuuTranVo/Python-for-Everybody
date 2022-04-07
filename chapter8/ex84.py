file_name = input("Enter file name: ")
file_handle = open(file_name,"r")

word_list = []
string_list = []
for line in file_handle:
    line = line.strip()
    string_list = line.split()

    for item in string_list:
        if item not in word_list:
            word_list.append(item)

word_list.sort()
print(word_list)