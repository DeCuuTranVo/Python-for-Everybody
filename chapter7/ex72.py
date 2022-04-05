# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
acc_val = 0
acc_count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    # Get the number from string
    number_part = line[line.find(":")+1:].strip()
    number = float(number_part)
    
    # Accumulate sum and count
    acc_val += number
    acc_count += 1

# Calculate average and print the output
print("Average spam confidence:",acc_val/acc_count)