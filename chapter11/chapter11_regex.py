import re

file_name = input("Input filename:")

if len(file_name) ==  0:
    # file_name = "regex_sum_42.txt"
    file_name = "regex_sum_1511837.txt"

file_handler = open(file=file_name)

number_list = []

for line in file_handler:
    re_list =  re.findall('[0-9]+',line)        

    if len(re_list) == 0:
        continue
    else:
        for ii in range(len(re_list)):
            re_list[ii] = int(re_list[ii])

        number_list += re_list    

print("Number of value:", len(number_list))
print("Final value:", number_list[-1])
print("Sum of value: ", sum(number_list))