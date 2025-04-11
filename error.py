# Program to handle errors when asking for a filename
filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        print("File content:")
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
