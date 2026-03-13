with open("sample.txt", "r") as file:
    print(file.read())
with open("sample.txt", "a") as file:
    file.write("new line\n")
with open("sample.txt", "r") as file:
    print(file.read())