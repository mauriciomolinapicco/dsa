with open("test.txt", "w") as file:
    content = "This is my file content"
    file.write(content)

with open("test.txt", "a") as file:
    content = "\n I am appending this at the end"
    file.write(content)