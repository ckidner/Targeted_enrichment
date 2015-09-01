#! /bin/bash -x
# to fastQC the raw files from the EvoDevo server
#Catherine Kidner 3 July 2015


echo "Hello world"

acc=$1
call=${acc}

smbclient //nased05/EvoDevo -U rbg-nt\\ckidner%t@tws2bresych -c "$call"
fastqc *.gz
rm *.gz



exit 0