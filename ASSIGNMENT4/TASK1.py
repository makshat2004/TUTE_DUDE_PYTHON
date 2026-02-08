"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

"""
try:
    with open("sample.txt",'rt') as fh:
        # Method: 1
        # data = fh.readline()
        # while data != '':
        #     print(data)
        #     data = fh.readline()

        # Method: 2
        data = fh.readlines()
        i = 1
        for datas in data:
            print(f"Line {i}: ",datas.rstrip('\n'))
            i = i + 1
except FileNotFoundError as e:
    print(f"Error: File sample.txt not found")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Program Ending")
