 # Differential_Inga.py
 # """To read in the read counts, the glycine matches, glycien descriptions for the Triscriptome."""

import pickle, shelve

def read_counts_2_dict(read_counts_file):
	name2reads = {}
	read_counts = open(read_counts_file)
	for line in read_counts:
		data_list = line.split()
		name = data_list[0]
		reads = data_list[2]
		name2reads[name] = reads
	return name2reads


def EC_2_dict(EC_file):
	name2info = {}
	EC_data = open(EC_file)
	for line in EC_data:
		data_list = line.split('\t')
		name = data_list[0]
		EC = data_list[1]
		description = data_list[2]
		info = (EC + " " + description)
		name2info[name] = info
	return name2info

def blast_2_dict(blast_output):
	name2hit = {}
	blast_data = open(blast_output)
	for line in blast_data:
		data_list = line.split('\t')
		name = data_list[0]
		hit = data_list[1]
		e_value = data_list[8]
		e_value = e_value.rstrip('\n')
		info = (hit + " " + e_value)
		name2hit[name] = info
	return name2hit

def query_me():

	min_total = input("what's the minimum read number you want?  ")
	min_total = int(min_total.rstrip('\n'))
	min_percent_umb = input("what's the minimum % I. umbellifera reads you want?  ")
	min_percent_umb = int(min_percent_umb.rstrip('\n'))
	max_percent_umb = input("what's the maximum % I. umbellifera reads you want?  ")
	max_percent_umb = int(max_percent_umb.rstrip('\n'))

	min_percent_spec = input("what's the minimum % I. spectabilis reads you want?  ")
	min_percent_spec = int(min_percent_spec.rstrip('\n'))
	max_percent_spec = input("what's the maximum % I. spectabilis reads you want?  ")
	max_percent_spec = int(max_percent_spec.rstrip('\n'))

	min_percent_sap = input("what's the minimum % I. sapindoides reads you want?  ")
	min_percent_sap = int(min_percent_sap.rstrip('\n'))
	max_percent_sap = input("what's the maximum % I. sapindoides reads you want?  ")
	max_percent_sap = int(max_percent_sap.rstrip('\n'))


	min_e_value = input("what's the minimum e_value of the match to Glycine you'll accept? (in format 1e-40)  ")
	min_e_value = float(min_e_value.rstrip('\n'))

	Tri_data = []

	for name in name2umb_reads:
		soy_hit_info = name2soy.get(name, 'No_Glycine_match_info')
		if soy_hit_info != 'No_Glycine_match_info':
			line = soy_hit_info.split(' ')
			soy_name = line[0]
			e_value = line[1]
			e_value = float(e_value)
			description = name2soyinfo.get(soy_name, 'No_Glycine_info')
		else:
			soy_name = 'None'
			description = 'None'
			e_value = 1000
		umb_reads = int(name2umb_reads[name])
		spec_reads = int(name2spec_reads[name])
		sap_reads = int(name2sap_reads[name])

		total_reads = umb_reads + spec_reads + sap_reads

		if total_reads >= min_total and total_reads > 0:

			percent_umb = round(100*(umb_reads/103070782)/((umb_reads/103070782) + (spec_reads/126784303) + (sap_reads/126788818)),2)
			percent_spec = round(100*(spec_reads/126784303)/((umb_reads/103070782) + (spec_reads/126784303) + (sap_reads/126788818)),2)
			percent_sap = round(100*(sap_reads/126788818)/((umb_reads/103070782) + (spec_reads/126784303) + (sap_reads/126788818)),2)

			if (percent_umb >= min_percent_umb) and (percent_umb <= max_percent_umb) and (percent_spec >= min_percent_spec) and (percent_spec <= max_percent_spec) and (percent_sap >= min_percent_sap) and (percent_sap <= max_percent_sap) and (e_value <= min_e_value):


				New_line = (name + ", "  + str(total_reads) + ",  " + str(percent_umb) + ", " + str(percent_spec) + ", " + str(percent_sap) + soy_hit_info + ",  " + description + ",  ")

				Tri_data.append(New_line)
	print("There are " + str(len(Tri_data)) + " sequences that match those criteria")

	to_print = input("Do you want a list of them? Yes/No  ")
	if to_print == "Yes":
		title = input("What's the file to be called?  ")
	#outfile = open('Tri_data.txt', "w")
	#for line in Tri_data:
		#outfile.write(str(line))
	#outfile.close()

		outfile = open(title, "w")
		outfile.write('\n'.join(Tri_data))
		outfile.close()

	
	more = input("Any other querries? Yes/No  ")

	if more == "Yes":
		query_me()

	if more =="No":
		print("That's your lot then")	

name2sap_reads = read_counts_2_dict('tri_sap_read_counts')
name2spec_reads = read_counts_2_dict('tri_spec_read_counts')
name2umb_reads = read_counts_2_dict('tri_umb_read_counts')
name2soyinfo = EC_2_dict('soy_EC.txt')
name2soy = blast_2_dict('Tri_gly_blasts')

question = input("Do you have a querry? Yes/No   ")
if question =="Yes":
	query_me()
if question == "No":
	print("End now")

# tri_dict = fasta_dict.fasta_stuff(Tri_trinity.fasta)
# read in dict of glycine matches and e values
# read in dict of EC descriptions for Glycine

# umb_spec_diff







