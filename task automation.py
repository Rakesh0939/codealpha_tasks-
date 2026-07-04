import re

# Input and output file names
input_file = "input.txt"
output_file = "emails.txt"

# Read the text file
with open(input_file, "r") as file:
    content = file.read()

# Regular expression to find email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Save email addresses to a new file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print(f"Found {len(emails)} email(s).")
print(f"Email addresses have been saved to '{output_file}'.")