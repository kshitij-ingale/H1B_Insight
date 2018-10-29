 import sys
import csv


# Read Input file using csv module
with open(sys.argv[1], newline='\n',encoding='utf-8') as csvfile:
	records = csv.DictReader(csvfile, delimiter=';')

# Obtain header from the data to find the labels for required information
	header = records.fieldnames

# Required Information for the problem: -
# Occupation name as per SOC and corresponding number of certified applications
# Total number of certified applications
# State for work place and corresponding number of certified applications


# It has been mentioned that data can have different columns. So required information
# will be parsed after determining the label of the required info in data file

# Find the label corresponding to required information

# For 2014 file, it was observed that there were 2 work locations associated with the
# application, so assumption was made that application was approved for all states specified 
# in the application
	state_cols = []
	for i in range(len(header)):
# Find the label corresponding to status
		if "status" in header[i].lower():
			status_col = header[i]
# Find the label corresponding to occupation name
		elif "soc_name" in header[i].lower(): 
			occupation_col = header[i]
		elif (header[i].lower()=="worksite_state") or (("workloc" in header[i].lower()) and ("state" in header[i].lower())):
			state_cols.append(header[i])
	
# Store data in dictionaries for occupations and states
	occupations = {}
	total_certified_applications_occupation = 0
	total_certified_applications_states = 0
	states = {}
	
	for record in records:
# Check if this record belongs to a certified application
		if record[status_col].lower()=='certified':
		# Count Certified Applications as per occupation
			# Check if occupation field is empty
			if record[occupation_col] == "":
				continue
			# Check if this occupation is new entry to dictionary
			elif record[occupation_col] in occupations:
				occupations[record[occupation_col]] += 1
				total_certified_applications_occupation += 1
			else:
				occupations[record[occupation_col]] = 1
				total_certified_applications_occupation += 1

		# Count Certified Applications as per states
			for col in state_cols:
				if record[col] == "":
					continue
				elif record[col] in states:
					states[record[col]] += 1
					total_certified_applications_states += 1
				else:
					states[record[col]] = 1
					total_certified_applications_states += 1


# Counters have been stored for occupations and states
# Evaluate metrics for occupations

# Check for number of occupations in data less than 10
if len(occupations)<10:
	end = len(occupations)
else:
	end = 10
with open(sys.argv[2],'w') as file:
	file.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
	ct = 0
	# Sort the occupations as per alphabetical order in name (since tie breaking is in alphabetical order) 
	# Sort data again to find the top 10 occupations corresponding to certified applications
	for key, value in sorted(sorted(occupations.items(), key= lambda x: x[0]),key = lambda x : x[1],reverse=True):
		file.write("%s;%d;%3.1f%%\n"%(key,value,100*value/total_certified_applications_occupation))
		ct=ct+1
		
		if ct==end:
			break

# Check for number of states in data less than 10
if len(states)<10:
	end = len(states)
else:
	end = 10
with open(sys.argv[3],'w') as file:
	file.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
	ct = 0
	# Sort the states as per alphabetical order in name (since tie breaking is in alphabetical order) 
	# Sort data again to find the top 10 states corresponding to certified applications
	for key, value in sorted(sorted(states.items(), key= lambda x: x[0]),key = lambda x : x[1],reverse=True):
		file.write("%s;%d;%3.1f%%\n"%(key,value,100*value/total_certified_applications_states))
		ct=ct+1
		if ct==end:
			break
