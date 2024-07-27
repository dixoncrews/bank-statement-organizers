import re
from datetime import datetime
from pathlib import Path

file_regex = re.compile(r'(.* \d{4}) Billing Statement.pdf')

# Rename files
count = 0
files = Path().rglob("*.pdf")
for file in files:
	if match := re.search(file_regex, file.name):
		new_filename = datetime.strptime(match.group(1), '%B %Y').strftime('%Y-%m') + '.pdf'
		print(f'{file.name} --> {new_filename}')
		file.rename(new_filename)
		count += 1

print(f"Moved {count} file(s)")
