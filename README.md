# Assignment-4
Logic used:-

Task1:
try: block
1.(try)Used to run the code safely. If the file is missing, the program won’t crash.
2.Open the file
3."sample.txt" is opened in text read mode "rt"
4.with open(...) automatically closes the file after reading.
5.Read all lines
readlines() stores every line in a list called lines.
6.Loop through the lines
range(len(lines)) gives index numbers (0, 1, 2, …).

i+1 is used to show line numbers starting from 1.

7.strip() removes unwanted newline characters.

8.If the file does not exist
The FileNotFoundError is caught
A friendly message is printed instead of crashing.


Task2:
1.Writing to the file
Ask the user to enter some text.
Open output.txt in write mode ("w").
Write the text to the file.
Confirm that writing is successful.

2.Appending additional text
Ask the user for more input.
Open the same file in append mode ("a").
Add (append) the new text without deleting previous content.
Confirm that appending is successful.

3.Reading the final content
Open output.txt in read mode ("r").
Read the entire file using read().
Display the full content to the user.
