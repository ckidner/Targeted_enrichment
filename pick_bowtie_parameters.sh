#! /bin/bash -x
# to take the hyb baits reads listed, bowtie to Inga baits, , convert to bam, make index, pileup and vcf
#Catherine Kidner 28 Oct 2014

echo "Hello world"
echo -n "Which accession would you like to run through from reads to vcf?  Type just the accession name  "
read acc
echo "You picked to work with: $acc  "
echo -n "which starting intercept would you like to use?  "
read n1
echo -n "Which intercept would you like to end with?  "
read n2
echo -n "Which step would you like to take?  Make sure this is divisible into the interval between starting and ending intercept values  "
read step

intercept=$n1

while [ $intercept -le $n2 ]

do

score=G,${intercept},8
fwd_p=../trimmed/${acc}_trimmed_1.fastq.gz
rev_p=../trimmed/${acc}_trimmed_2.fastq.gz
un_p=../trimmed/${acc}_trimmed_1u.fastq,../trimmed/${acc}_trimmed_2u.fastq
sam=${acc}.sam
index=${acc}_${intercept}_sorted.bam
pileup=${acc}_${intercept}.pileup
vcf=${acc}_${intercept}.vcf
bowtie=${acc}_${intercept}_bowtie_output
sorted=${acc}_${intercept}_sorted

bowtie2 --local --score-min $score -x ~/bowtie2-2.0.2/Inga_unique_baits -1 $fwd_p  -2 $rev_p  -U $un_p  -S $sam 2>$bowtie
samtools view -bS $sam | samtools sort - $sorted
samtools index $index
samtools mpileup -E -uf Ref_new.fna  $index > $pileup
bcftools view -cg $pileup > $vcf
rm *.sam
rm *.bam
rm *.pileup
rm *.bai
intercept=$(($intercept + $step))

done

exit 0

