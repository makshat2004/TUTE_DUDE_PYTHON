"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""

writing_text = input("Enter text to write into file: ")

try:
    with open("output.txt", "wt") as file:
        file.write(writing_text.rstrip() + "\n")
    print("Data successfully written to output.txt")
except Exception as e:
    print(f"Write error: {e}")

append_text = input("Enter text to append into file: ")

try:
    with open("output.txt", "at") as file:
        file.write(append_text.rstrip() + "\n")
    print("Data successfully appended to output.txt")
except Exception as e:
    print(f"Append error: {e}")

print("\nFinal content of output.txt:")

try:
    with open("output.txt", "rt") as file:
        line = file.readline()
        while line != "":
            print(line, end="")
            line = file.readline()
except Exception as e:
    print(f"Read error: {e}")
