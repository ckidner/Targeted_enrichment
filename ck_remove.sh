#!/usr/bin/env bash
cat $1_trimmed_2.fastq | paste - - - - | grep -F -v -w -f $1.empties - | tr "\t" "\n" | gzip > $1_2.fastq.test.gz; mv $1_2.fastq.test.gz $1_trimmed_2.fastq.gz
cat $1_trimmed_1.fastq | paste - - - - | grep -F -v -w -f $1.empties - | tr "\t" "\n" | gzip > $1_1.fastq.test.gz; mv $1_1.fastq.test.gz $1_trimmed_1.fastq.gz
