#! /bin/bash -x
# to remove tricky stuff from the vcf files and make the fasta
# Input on comnad line is the accession stem
#Catherine Kidner 11 Nov 2014


echo "Hello world"

acc=$1

echo "You're working on accession $1"


vcf=${acc}.vcf
clean=${acc}_clean.vcf
fasta=${acc}.fasta

grep -v "INDEL" $vcf | awk '{if ($6 >= 36) print $0}' > $clean

vcfutils_fasta.pl vcf2fq $clean > $fasta

rm $clean

exit 0
