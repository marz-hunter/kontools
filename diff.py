#import necessary modules 
import difflib 

#define input file names 
file_1 = input("Enter the first filename: ") 
file_2 = input("Enter the second filename: ")

#open the files and read the data 
with open(file_1) as f1, open(file_2) as f2:
    file1_data = f1.readlines()
    file2_data = f2.readlines()

#calculate the differences between files 
diff = difflib.ndiff(file1_data, file2_data) 

#print the differences 
print('\n'.join(diff))
