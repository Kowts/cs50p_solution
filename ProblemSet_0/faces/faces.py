# Prompt the user to input a text and store it in the 'text' variable.
text = input("Enter text: ")

# Replace ":)" with the happy face emoji "🙂" and ":(" with the sad face emoji "🙁" using the 'replace()' method.
# This replaces specific text sequences with corresponding emojis.
text_emoji = text.replace(":)", "🙂").replace(":(", "🙁")

# Print the text with emojis substituted for the respective emoticons.
print(text_emoji)