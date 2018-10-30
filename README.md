# H1B insights
This is the submission for the Insight Data Engineering Coding Challenge
# Problem Statement
The problem involves obtaining relevant metrics for the H1B data. We have to identify the top 10 occupations which were certified for the H1-B visa. In addition to this, we have to identify top 10 states of job postings for which applications were accepted.
# Approach
The input file provides a wide range of data fields like employer-employee details. In order to make the source code robust to input file structure, this approach involves traversing through data fields and determining which labels correspond to status, work location and occupation title as SOC code.  
A broad overview of the approach can be traversing through data and counting certified applications corresponding to each occupation and state. The following steps were followed in the implementation.
1. Importing data using csv module of python to create ordered dictionaries for data storage
2. The file structure can change for different files, hence, the keys corresponding to required information are determined
3. The ordered dictionaries are accessed and the counters for occupations and states are implemented for certified applications. The counters are maintained in dictionaries for O(1) access complexity.
4. The dictionaries are sorted to find top 10 occupations and states and results are written to the output files    
  
The data structures used involved ordered dictionaries as output of csv reader and dictionaries to store counters. The counter dictionaries enable access complexity of O(1). The ties in top 10 occupations and states are broken by lexicographical order, so single sort in reverse order will result in tie-breaking by reversed lexicographical order. So, dictionaries are sorted twice to obtain the top 10 entities.
# Source code information  
The source code has been developed in python3.6 and so is executed as per python3 in shell script. The modules from standard library of python like sys and csv are used. Execution of "run.sh" script should generate output files in ./output directory for the input file in ./input directory
