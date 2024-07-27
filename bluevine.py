import re
from datetime import datetime
from pathlib import Path

file_regex = re.compile(r'statement_(\d{4})_(\d{1,2}).pdf')

# Rename files
count = 0
files = Path().rglob("*.pdf")
for file in files:
	if match := re.search(file_regex, file.name):
		new_filename = datetime(int(match.group(1)), int(match.group(2)), 1).strftime('%Y-%m') + '.pdf'
		print(f'{file.name} --> {new_filename}')
		file.rename(new_filename)
		count += 1

print(f"Moved {count} file(s)")
