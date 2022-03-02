username = input()
list_of_characters = []
for i in range(0, len(username)):
    if username[i] not in list_of_characters:
        list_of_characters.append(username[i])
if len(list_of_characters) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
