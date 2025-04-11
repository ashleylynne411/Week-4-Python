# Program to read a file and write a modified version to a new file

# Ask the user for the input file name
input_filename = input("Enter the name of the file you want to read: ")

try:
    # Attempt to open the specified file
    with open(input_filename, "r") as input_file:
        # Read the content of the file
        data = input_file.readlines()
    
    # Modify the content (e.g., convert to uppercase)
    modified_data = [line.upper() for line in data]
    
    # Ask the user for the output file name
    output_filename = input("Enter the name of the new file to save the modified content: ")
    
    # Write the modified content to the new file
    with open(output_filename, "w") as output_file:
        output_file.writelines(modified_data)
    
    print(f"The content has been successfully read from '{input_filename}' and saved to '{output_filename}'!")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

