#!/bin/sh
cat $1_trimmed_1.fastq $1_trimmed_2.fastq | grep -B1 "^$" | grep "^@" | cut -f1 -d " " - > $1.empties
