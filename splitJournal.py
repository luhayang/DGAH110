import re

# Input file
input_file = "JournalsOfLewis&Clark.txt"

# Output files
lewis_file = "lewis.txt"
clark_file = "clark.txt"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Split into entries [Lewis/Clark...] using regular expression
entries = re.split(r"(\[[A-Za-z]+,\s+[A-Za-z]+\s+\d{1,2},\s+\d{4}\])", text)

# Combine each header ([Lewis/Clark...]) with its following text body
combined_entries = []
for i in range(1, len(entries), 2):
    header = entries[i].strip()
    body = entries[i + 1].strip() if i + 1 < len(entries) else ""
    combined_entries.append((header, body))

# Separate by author and clean
def remove_date(text):
    lines = text.splitlines()
    remaining = [line for line in lines[1:] if line.strip()]
    return "\n".join(remaining).strip()

lewis_entries = []
clark_entries = []

for header, body in combined_entries:
    cleaned_body = remove_date(body)
    if header.startswith("[Lewis"):
        lewis_entries.append(cleaned_body + "\n\n")
    elif header.startswith("[Clark"):
        clark_entries.append(cleaned_body + "\n\n")

# Write to separate files
with open(lewis_file, "w", encoding="utf-8") as f:
    f.writelines(lewis_entries)

with open(clark_file, "w", encoding="utf-8") as f:
    f.writelines(clark_entries)

print(f"Split complete to {len(clark_entries)} Clark entries, {len(lewis_entries)} Lewis entries.")