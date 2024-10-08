reading_a_file = open("read_file.txt", 'r')
f = reading_a_file.readlines()

list_items = []

for items in f:
    if items[-1] == '\n':
        list_items.append(items[:-1]) # for removing backslash n
    else:
        list_items.append(items)

print(list_items)