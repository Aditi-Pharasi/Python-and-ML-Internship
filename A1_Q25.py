#25. Write a program that copies the contents of one text file to another.
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File copied successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_file = "file1.txt"
destination_file = "output.txt"
copy_file(source_file, destination_file)