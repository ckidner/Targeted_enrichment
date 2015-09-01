#! /bin/bash -x
# to trim the trimmomatic output one more time
# Needs ck_empties.sh and ck_remove.sh
#Catherine Kidner 3 Nov 2014


echo "Hello world"

acc=$1

echo "You're working on accession $1"


fwd_p=${acc}_forward_paired.fq.gz
rev_p=${acc}_reverse_paired.fq.gz
fwd_un_p=${acc}_forward_unpaired.fq.gz
rev_un_p=${acc}_reverse_unpaired.fq.gz

fwd_p_done=${acc}_trimmed_1.fastq
rev_p_done=${acc}_trimmed_2.fastq
fwd_u_done=${acc}_trimmed_1u.fastq
rev_u_done=${acc}_trimmed_2u.fastq

cutadapt -a AGATCGGAAGAGC $fwd_p > $fwd_p_done 2>> cut_out
cutadapt -a AGATCGGAAGAGC $rev_p > $rev_p_done 2>> cut_out
cutadapt -a AGATCGGAAGAGC $fwd_un_p > $fwd_u_done 2>> cut_out
cutadapt -a AGATCGGAAGAGC $rev_un_p > $rev_u_done 2>> cut_out
./ck_empties_fastq.sh $acc
./ck_remove_fastq.sh $acc


exit 0

