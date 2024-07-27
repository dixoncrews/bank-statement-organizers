from pathlib import Path
import re
from datetime import datetime, timedelta

folder_regex = re.compile(r'(\d{4})$')
file_regex = re.compile(r'STMTCMB100_(\d{8})_(\d{4})_Crews_\d{7}_\d{5,6}.pdf')

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

# Rename STMT files
count = 0
files = Path().rglob("*")
for file in files:
	if match := re.search(file_regex, file.name):
		new_filename = (datetime.strptime(match.group(1), '%Y%m%d') - timedelta(days=1)).strftime('%Y-%m') + '.pdf'
		new_folder = account_num_to_folder[match.group(2)]
		print(f'{file.name} --> {new_folder}/{new_filename}')
		file.rename(new_folder / new_filename)
		count += 1

print(f"Moved {count} file(s)")
