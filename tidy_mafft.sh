#! /bin/bash -x
# to go from the output of switch multifastas.py to the mafft files ready to trimal
#Catherine Kidner 18 Nov 2014


echo "Hello world"

acc=$1

echo "You're working on accession $1"


switched=${acc}.fasta
no_loci_name=${acc}_f.fna
mafft=${acc}_mafft.fasta
fna=${acc}.fna
fasta=${acc}.fasta

sed "s/_$acc//g" $switched > $no_loci_name 
sed "s/[rywsmkdvhb]/n/g" $no_loci_name  > $fna
tr '[:lower:]'  '[:upper:]' < $fna > $fasta
rm $no_loci_name
rm $fna
linsi --thread 8 $fasta > $mafft


exit 0
