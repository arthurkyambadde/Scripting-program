#!/bin/bash

# download the zip file bla bla bla
wget -P  ../data/raw https://github.com/kipkurui/Intro2Linux2019/raw/master/Data/genomic_data.zip

#extract contents from zip file

unzip ../data/raw/genomic_data.zip -d ../data/processed

#dnfdn cknvkd djbfjd
echo "Number of files"
find ../data/processed/genomic_data/ -maxdepth 1 -type f | wc -l

echo "Number of fasta files"
find ../data/processed/genomic_data/ -maxdepth 1 -type f -iname "*.fa" | wc -l fasta