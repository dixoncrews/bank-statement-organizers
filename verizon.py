import re
from pathlib import Path
from dotenv import dotenv_values

# Config
config = dotenv_values(".env")
file_regex = re.compile(r'^MyBill_(?P<month>\d{2}).(?P<day>\d{2}).(?P<year>\d{4}).pdf$')
path = config['VERIZON_PATH']
print(f"Using path: {path}")

# Rename files
count = 0
files = Path(path).rglob("*.pdf")
for file in files:
	if match := re.search(file_regex, file.name):
		new_filename = f"{match.group('year')}-{match.group('month')}-{match.group('day')}.pdf"
		print(f'{file.name} --> {new_filename}')
		file.rename(f"{path}/{new_filename}")
		count += 1

print(f"Moved {count} file(s)")
