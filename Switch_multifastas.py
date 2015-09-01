'''take a set of multifastas and re-order as by filename a set of multifastas
 For dealing with hyb_baits bowtie to fasta outputs
 needs alist f the fasta file names and a list of the loci (as in the fasta_files)
 set at the default - can change to querry for list names
 needs an output folder called By_locus'''


def fasta_dict(fastafile):
	file = open(fastafile)
	name2seq = {}

	for line in file:
		if line.startswith(">"):
			seq = ''
			split_line = line.split(' ')
			name = split_line[0]
			name = name.rstrip()
			name = name.lstrip('>')
		else:
			seq = seq + str(line)
			seq = seq.rstrip()

		name2seq[name] = seq
	
	return name2seq

print ("Hello world")

fastafile_list = "fasta_files"
locus_list_file = "locus_list"

#fastafile_list = input("Which list of fasta files (full file name please)?\n")
#locus_list_file = input("Which file for names of loci?\n")

#open files for each locus (for reading and writting) ready to feed in the fastas

if locus_list_file != None:
	locus_list = open(locus_list_file)
	for name in locus_list:
		name = name.rstrip("\n")
		out_file_name = name + ".fasta"

		outfile = open(out_file_name, "w")
		outfile.close()

# go through each fasta file pulling out the match to each locus and putting into the file

if fastafile_list != None:
	fastafiles = open(fastafile_list)
	for file_name in fastafiles: 
		file_name = file_name.rstrip("\n")
		accession = file_name.rstrip(".fna")

		#Make a dict of that fasta file

		ifasta_dict = fasta_dict(file_name)

		keep_lines_processed = 0
		keep_seq_found = 0
		missing_list = []

		if locus_list_file != None:
			locus_list = open(locus_list_file)
			#for a locus pull out the hit and append to the correct file
			for name in locus_list:
				name = name.rstrip("\n")
				found_fasta = ">" +  accession + "_" + name + "\n"
				keep_lines_processed += 1


				fasta_seq = ifasta_dict.get(name, "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
				if name in ifasta_dict.keys():
					keep_seq_found +=1
				else:
					missing_list.append(name)

				found_fasta = found_fasta + fasta_seq + "\n"
				locus_file_to_write = "By_locus/" + name + ".fasta"
				with open(locus_file_to_write, "a") as myfile:
					myfile.write(found_fasta)



		print("Keep lines processed for " + file_name + "  = " + str(keep_lines_processed))
		print("Keep sequences found for " + file_name + " = " + str(keep_seq_found))
		print("Missing for " + file_name + " = " + str("\n".join(missing_list)))
	



	
			
	
