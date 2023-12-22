number_per_row = 9
space_per_number = 10
start_number = 1
number_pattern = "xxx"


for i in range(240):
    if i % number_per_row == 0:
        print()
    print(f"{i+1:0>3}", end=" " * space_per_number)