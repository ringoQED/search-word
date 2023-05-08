#####################################################################################
#                                                                                   #
#                                   SEARCH & FOUND                                  #
#                                                                                   #
#####################################################################################
#program to read, find and display the lines in input text file matching the search term
#created by Ringo Cheung on 2023/4/20
#ver 1.1


import os
import sys
import re

#clear the console screen
os.system('cls')


#define the variables
greeting = 'Hi there!\n\nThis program will read the sample input file and find the lines which match the search term.'
inputFile = sys.argv[1]         #take the sample text file name as the input argument (e.g. sample.txt)
EMPTY = False                   #variable to remember if the input file is empty or not

#greet the program users
print(greeting + '\n')

#print the name of the sample file
print('Your input sample file is now : ' + '"' + inputFile + '".' + '\n')


#read the input file and find the search term at the last line of the file
with open(inputFile) as f:
    lines = f.read().splitlines()
    
if lines:                       #make sure the file is not empty
    searchTerm = lines[-1]      #search term is the last line of the file, just before the EOF
    print ('The search term is found to be ' + '"' + searchTerm + '".' + '\n')
else:
    EMPTY = True
    print ('Your input file is empty.')
    

#read the input file line by line, then find the lines which match the search term and display them
if not(EMPTY):
    print('Here is the output of the matching lines :' + '\n')

with open(inputFile) as f:

    for lines in f:
        if EMPTY:
            break

        #match each line with search string and print the line if they match, skip printing the search term itself
        if (searchTerm in lines) & (searchTerm != lines):           
            myline = re.sub("[^a-zA-Z]", " ", lines)    #replace all non-alphabet (e.g. @,#,$,!... etc.) with spaces
            myline = re.sub(' +', ' ', myline)          #replace multiple spaces with a single space
            print('[' + myline.strip() + ']')
           

print('\n')            
print('\n' + '...End of Program...' + '\n')