#! /bin/bash -x
# mining vcf fiesl for quality stats
# Catherine Kidner 6 January 2015

echo "Hello world"
echo -n "Which accession would you like to gather the alignment stats for?  Type just the accession name  "
read acc
echo "You picked to work with: $acc  "
echo -n "which starting intercept did you use?  "
read n1
echo -n "Which intercept did you end with?  "
read n2
echo -n "Which step did you take"
read step

intercept=$n1
alltog=${acc}_stats.txt
echo "%_aligned,N_bases,Av_Qual_reads,Max_Qual_reads,Av_Qual_non_varient,Max_Qual_non_varient,Av_Qual_varient,Max_Qual_varient,N_varient,N_non_varient" > $alltog

while [ $intercept -le $n2 ]

do

vcf=${acc}_${intercept}.vcf
bowtie=${acc}_${intercept}_bowtie_output
output=${acc}_${intercept}_temp

# % aligned
grep  "overall alignment rate" $bowtie | awk '{print $1 }' >> $output

#Number of reads:
grep -c "comp" $vcf >> $output

#average Qual of reads:
grep  "comp" $vcf | awk 'BEGIN {max=0} {sum+=$6; if ($6>max) {max=$6}} END {print sum/NR "," max}' >> $output

#average Qual of non-varient
grep  "comp" $vcf | awk '{ if ($5 == ".") print $0 }' |awk 'BEGIN {max=0} {sum+=$6; if ($6>max) {max=$6}} END {print sum/NR "," max}' >> $output

#average Qual of variant:
grep  "comp" $vcf | awk '{ if ($5 != ".") print $0 }' |awk 'BEGIN {max=0} {sum+=$6; if ($6>max) {max=$6}} END {print sum/NR "," max}' >> $output

#Number of variants
grep  "comp" $vcf | awk '{ if ($5 != ".") print $0 }'| wc -l >> $output

#Number of non_varient
grep  "comp" $vcf | awk '{ if ($5 == ".") print $0 }'| wc -l >> $output

#re-arrange data into a single line per intercept with comma delinated fields

paste -s -d, $output >> $alltog

intercept=$(($intercept + $step))

done

rm *_temp

exit 0


