#The program requesting from the bed file from the user
#for each chromosome calculate the number of reads 
# calculate the average read quality
#load the menu DONE
#Select an option
  #[R] Display read counts in each Chromosome
  #[D] Display the average read quality for each chromosome
  #[X] Exit
  
  #below is the logic for the program me
  
#add a comment h
counts={}
total_read_quality={}

bed_file=input("Please enter the name of the bed file: ")

working_bedfile = open(bed_file ,"r")


for line in working_bedfile:
    line=line.strip()
    
    if line.startswith("#"): 
        continue
    
    columns=line.split()
    
    chromosome=columns[0]
    read_quality = float(columns[3])
    if chromosome not in counts: 
        counts[chromosome]=1
        total_read_quality[chromosome] =  read_quality
        
    else:
        counts[chromosome] = counts[chromosome]+1 
        
        total_read_quality[chromosome] = total_read_quality[chromosome] + read_quality

    
working_bedfile.close() 
  
  
  
while True: 
    print("Select an option")
    print("[R] Display read counts in each Chromosome")
    print("[D] Display the average read quality for each chromosome")
    print("[X] Exit")
    option=input("Please select an option from the menu: ").upper()
    if option=="R":
        sorted_chromosomes = sorted(counts,key=lambda chr:counts[chr], reverse=True)
        chr_heading="Chr "
        count_heading="count"
        output=f"{chr_heading}    {count_heading}\n"
        print(output)
        
        
     
        for each_chromosome in sorted_chromosomes:
            output = output + f"{each_chromosome}    {str(counts[each_chromosome])}\n"
            
        output_file = open("./output/read_counts.txt", "w")  
        output_file.write(output)
        output_file.close()
        
        
        
        print(output)
        # print("columns", sorted_chromosomes)
        
        
    elif option=="D":
        output = ""
        for chromosome in counts:
           average = total_read_quality[chromosome]/counts[chromosome]
           output = output + f"{chromosome}   {average:.3f}\n"
           print(output)
        output_file = open("./output/average_counts.txt", "w")  
        output_file.write(output)
        output_file.close()
        
    elif option=="X":
        print("You have exited the program")  
        break   
    else:
        print("Invalid option, please select a valid option from the menu")
        
        
