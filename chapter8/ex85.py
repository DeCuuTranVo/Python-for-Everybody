fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.strip()
    if (line.startswith("From") and not line.startswith("From:")):
        address_list = line.split()
        word = address_list[1]
        print(word)
        count += 1

print("There were", count, "lines in the file with From as the first word")

