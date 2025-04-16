def process_file():
    # Step 1: Ask user for the file name
    filename = input("📄 Enter the filename to read from: ")

    try:
        # Step 2: Try opening and reading the file
        with open(filename, 'r') as file:
            content = file.read()

        # Step 3: Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Step 4: Save the modified content to a new file
        output_filename = 'book.txt'
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"✅ File processed successfully. Check '{output_filename}' for the result.")

    except FileNotFoundError:
        print("❌ File not found. Please check the name and try again.")
    except PermissionError:
        print("❌ Permission denied. You do not have access to read/write this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the file processor
process_file()
