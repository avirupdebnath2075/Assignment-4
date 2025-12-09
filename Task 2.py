text = input("Enter text to write to the file:")
with open("output.txt", "a") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.\n")

more_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(more_text + "\n")
print("Data successfully appended.\n")

print("Final content of output.txt:\n")
with open("output.txt", "r") as file:
    print(file.read())
