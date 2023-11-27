import re

# Main function that prompts the user for an HTML string and prints the parsed YouTube short link if found.
def main():
    print(parse(input("HTML: ")))

# Parses the provided HTML string to extract a YouTube short link if present.
def parse(s: str) -> str:
    """
    Args:
    - s (str): HTML string to parse.

    Returns:
    - str: YouTube short link if found, otherwise None.
    """

    # Extract URL from 'src' attribute
    URL = re.search(r'src=[\'"]([^\'"]+)', s)
    if URL:
        URL = URL.group(1)

        # Check if the URL is from YouTube
        youtubeLink = re.search(r'(youtube)', URL)
        if youtubeLink:
            # Extract YouTube video ID
            ytID = re.sub(r"^(https?://)?(www\.)?youtube\.com/([a-z0-9_]+)", "", URL)
            return f"https://youtu.be{ytID}"
    return None  # If no YouTube link was found

if __name__ == "__main__":
    # Execute the main function
    main()
