''' Concatenate interleaved nexus files into a single interleaved nexus 
cannot cope with missing data.  Assumes if data is missing for a locus for an accession there is a files of Ns replacing it'''

#read in file lists

#nexusfile_list = "nexus_files"
#accession_list_file = "acc_names"

# Read in the seq data to a holding file
# when read "MATRIX": next line is the beginning of the data
# read in until ";" into a string

def get_block(nexus_file):
	new_block = []
	with open(nexus_file) as input_data:
# Skips text before the beginning of the interesting block:
		for line in input_data:
			if line.strip() == 'MATRIX':  # Or whatever test is needed
				break
# Reads text until the end of the block:
		for line in input_data:  # This keeps reading the file
			if line.strip() == ';':
				break
			line = line.rstrip("\n")
			new_block.append(line)
	return(new_block)

# Count the resdidues in the file

def count_bp(block, name):
	counter = ''
	for line in block:
		line = str(line)
		if line.startswith(name):
# clean up line to just nucleotides and append to a counting list
			line = line.lstrip(name)
			line = line.lstrip()
			line = line.rstrip()
			counter = counter + str(line)
	return len(counter) - counter.count(' ')

nexus_list_file = input("Which list of nexus files (full file name please)?\n")
accession_list_file = input("Which file for names of accessions?\n")

#open files for each locus (for reading and writing) ready to feed in the nexuses

if accession_list_file != None:
	acc_list = open(accession_list_file)
	acc_name_list = []
	for name in acc_list:
		name = name.rstrip("\n")
		acc_name_list.append(name)

picked = acc_name_list[0]
n_acc = len(acc_name_list)

print(str(picked))

all_blocks = []

char_block = []

bp_beg = 1

if nexus_list_file != None:
	nexus_file_list = open(nexus_list_file)
	for nexus_file in nexus_file_list:
		nexus_file = nexus_file.rstrip()
		new_block = get_block(nexus_file)
		locus_name = nexus_file.rstrip(".nex")
#		all_blocks.append("[" + str(locus_name) +"]")
		all_blocks = all_blocks + new_block
		locus_count = count_bp(new_block, picked)
		bp_end = bp_beg + locus_count - 1
		print("Locus count is " + str(locus_count))
		char_line = "charset " + str(locus_name) + " = " + str(bp_beg) + " - " + str(bp_end) + ";"
		char_block.append(char_line)
		bp_beg = bp_end + 1
		print("Accumulated bp is " + str(bp_end))

total_bp = count_bp(all_blocks, picked)
print ("Total_bp is " + str(total_bp))

# rebuild the header

header_1 = "#NEXUS\n"
header_2 = "begin data;"
header_3 = "dimensions ntax=" + str(n_acc) + " nchar=" + str(bp_end) + ";"
header_4 = "format datatype=DNA interleave=yes gap=-;\n"
header_5 = "matrix"

header_list = [header_1, header_2, header_3, header_4, header_5]

# don't need this bit as the acc_data stuff is added by trimal to individual nexus files 
#acc_data = []
#for acc_name in acc_name_list:
#	line = "[Name: " + str(acc_name) + "			Len: " + str(bp_end) + " Check: 0]"
#	acc_data.append(line)
#acc_data.append("")
#acc_data.append("MATRIX")

footer_1 = ";"
footer_2 = "end;"
footer_3 = ""

footer_list = [footer_1, footer_2, footer_3]


char_block.insert(0,"begin sets;")
char_block.append("end;")

#new_nexus_list = header_list + acc_data + all_blocks + footer_list + char_block
new_nexus_list = header_list + all_blocks + footer_list + char_block

new_nexus = '\n'.join(new_nexus_list)

# print (new_nexus)



outfile = open("concat.nex", "w")
for item in new_nexus_list:
  outfile.write("%s\n" % item)








