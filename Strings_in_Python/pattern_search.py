import re

text = "My name is Mithu Gambler and I am not a gambler."
pattern = r"\bgambler\b"

matches = re.finditer(pattern, text)
for match in matches:
    print(f"Pattern found at index {match.start()} to {match.end()}")
