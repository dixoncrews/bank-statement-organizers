import re
from pathlib import Path

folder_regex = re.compile(r'(\d{3})$')
file_regex = re.compile(r'.*_([\d-]*)_(\d{3}).pdf')

# '1234' -> Path(/1234)
account_num_to_folder = {}

# Rename .PDF and build account_num_to_folder
files = Path().rglob("*")
for file in files:
	if file.suffix == '.PDF':
		file.rename(file.with_suffix('.pdf'))
	
	if file.is_dir():
		if match := re.search(folder_regex, file.name):
			account_num_to_folder[match.group(1)] = file

for k,v in account_num_to_folder.items():
	print(f"{k}: {v}")

# Rename files
count = 0
files = Path().rglob("*")
for file in files:
	if match := re.search(file_regex, file.name):
		new_filename = f'{match.group(1)}.pdf'
		new_folder = account_num_to_folder[match.group(2)]
		print(f'{file.name} --> {new_folder}/{new_filename}')
		file.rename(new_folder / new_filename)
		count += 1

print(f"Moved {count} file(s)")
