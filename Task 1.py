try:
    with open("sample.txt", "rt") as file:
        lines = file.readlines()   
        for i in range(len(lines)):
         print(f"Line {i+1}: {lines[i].strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
