#!/bin/bash

dir="../data/processed/genomic_data"

results_dir="../results"
output_file="$results_dir/all_sequence_headers.txt"

for file in "$dir"/*.fa*; do

    grep "^>" "$file" >> "$output_file"

done

