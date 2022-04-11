name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hour_dict = {}

# Build hour dict
for line in handle:
    if (line.startswith("From ")):
        line = line.rstrip()
        word_list = line.split()
        hour = word_list[5][:2]
        hour_dict[hour] = hour_dict.get(hour, 0) + 1
        
#print(hour_dict)

# Create list and tuple
list_to_sort = []
for (hr, freq) in hour_dict.items():
    list_to_sort.append((hr, freq))

#print(list_to_sort)

list_after_sort = sorted(list_to_sort)

#print(list_after_sort)
for (k, v) in list_after_sort:
    print("{} {}".format(k,v))
