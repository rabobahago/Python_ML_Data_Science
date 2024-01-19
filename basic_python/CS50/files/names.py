name = input('what is name?')
with open("name.txt", 'a') as file:
    file.write(f"{name}\n")
    file.close()
