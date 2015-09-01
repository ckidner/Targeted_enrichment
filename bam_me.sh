#! /bin/bash -x
# to trim again using cutadapt
#Catherine Kidner 28 Oct 2014
# Assumes all your reads are in a folder called trimmed and all are gzipped.

echo "Hello world"

acc=$1

echo "Working on $1"
score=G,320,8
fwd_p=../trimmed/${acc}_trimmed_1.fastq.gz
rev_p=../trimmed/${acc}_trimmed_2.fastq.gz
un_p=../trimmed/${acc}_trimmed_1u.fastq.gz,../trimmed/${acc}_trimmed_2u.fastq.gz
sam=${acc}.sam
index=${acc}_sorted.bam
pileup=${acc}.pileup
vcf=${acc}.vcf
bowtie=${acc}_bowtie_output
sorted=${acc}_sorted

bowtie2 --local --score-min $score -x ~/bowtie2-2.0.2/Inga_unique_baits -1 $fwd_p  -2 $rev_p  -U $un_p  -S $sam 2>$bowtie
samtools view -bS $sam | samtools sort - $sorted
samtools index $index
samtools mpileup -E -uf Ref_new.fna  $index > $pileup
bcftools view -cg $pileup > $vcf
rm *.sam
rm *.pileup

exit 0

