#The program requesting from the bed file from the user
#for each chromosome calculate the number of reads 
# calculate the average read quality
#load the menu DONE
#Select an option
  #[R] Display read counts in each Chromosome
  #[D] Display the average read quality for each chromosome
  #[X] Exit
  
  #below is the logic for the program me
  
#add a comment
counts={}
bed_file=input("Please enter the name of the bed file: ")

for line in open(bed_file):
    line=line.strip()
    
    if line.startswith("#"): 
        continue
    
    columns=line.split()
    
    chromosome=columns[0]
    
    if chromosome not in counts: 
        counts[chromosome]=1
    else:
        counts[chromosome] = counts[chromosome]+1 
bed_file.close() 
    
    

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
while True: 
    print("Select an option")
    print("[R] Display read counts in each Chromosome")
    print("[D] Display the average read quality for each chromosome")
    print("[X] Exit")
    option=input("Please select an option from the menu: ").upper()
    if option=="R":
        sorted_chromosomes = sorted(counts,key=lambda chr:counts[chr], reverse=True)
        print("columns", sorted_chromosomes)
        
    elif option=="D":
        print("D")
    elif option=="X":
        print("You have exited the program")  
        break   
    else:
        print("Invalid option, please select a valid option from the menu")
        
        
