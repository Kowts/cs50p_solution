# Prompt the user to input a file name.
user_input = input("Filename: ").lower().strip()

# Split the user input by the last dot to get the file extension.
file_parts = user_input.rsplit(".", 1)

if len(file_parts) > 1:
    # Extract the file extension from the last part of the split input.
    file_extension = file_parts[1]

    # Define a dictionary that maps file extensions to their corresponding MIME types.
    extensions = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }

    # Check if the file extension is a known extension.
    if file_extension in extensions:
        # If it's a known extension, print the corresponding MIME type.
        print(extensions[file_extension])
    else:
        # If it's not a known extension, print "application/octet-stream."
        print("application/octet-stream")
else:
    # If there was no dot in the input, print "application/octet-stream."
    print("application/octet-stream")
