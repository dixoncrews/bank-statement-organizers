import re
from datetime import datetime
from pathlib import Path

folder_regex = re.compile(r'(\d{4})$')
file_regex = re.compile(r'(\d{8})-statements-(\d{4})-.pdf')

# '1234' -> Path(/1234)
account_num_to_folder = {}

# Build account_num_to_folder
files = Path().glob("*")
for file in files:	
	if file.is_dir():
		if match := re.search(folder_regex, file.name):
			account_num_to_folder[match.group(1)] = file

for k,v in account_num_to_folder.items():
	print(f"{k}: {v}")

# Rename files
count = 0
files = Path().glob("*.pdf")
for file in files:
	if match := re.search(file_regex, file.name):
		new_filename = datetime.strptime(match.group(1), '%Y%m%d').strftime('%Y-%m-%d') + '.pdf'
		new_folder = account_num_to_folder[match.group(2)]
		print(f'{file.name} --> {new_folder}/{new_filename}')
		file.rename(new_folder / new_filename)
		count += 1

print(f"Moved {count} file(s)")
