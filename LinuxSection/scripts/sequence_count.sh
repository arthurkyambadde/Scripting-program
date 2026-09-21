#!/bin/bash

dir="../data/processed/genomic_data"

for file in $dir/*.fa*; do

    count=$(grep -c "^>" "$file") 

    echo -e "$(basename "$file")\t\t\t$count"

    printf "%s\t\t%s\n" "$(basename "$file")" "$count"

done

