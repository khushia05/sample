val=(input("enter multiple values")).split()
print(val)
index_value=int(input("index value"))
part_to_reverse = val[index_value:][::-1]
new_list = val[:index_value] + part_to_reverse
print(new_list)