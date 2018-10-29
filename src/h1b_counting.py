import sys

# Read Input file
with open(sys.argv[1],'r') as file:
	data = file.read()
	records = data.split('\n')

# Obtain header from the data
	header = records[0].split(';')


# Required Information for the problem: -
# Occupation name as per SOC and corresponding number of certified applications
# Total number of certified applications
# State for work place and corresponding number of certified applications


# It has been mentioned that data can have different columns. So, the required information
# will be parsed after determining the position of column in data file
# Find the column number corresponding to required information

	state_cols = []
	for i in range(len(header)):
# Find the column corresponding to status
		if "status" in header[i].lower():
			status_col = i
# Find the column corresponding to occupation name
		elif "soc_name" in header[i].lower(): 
			occupation_col = i
# For 2014 data file, there are 2 work locations which will have to be counted for both locations
		elif (header[i].lower()=="worksite_state") or (("workloc" in header[i].lower()) and ("state" in header[i].lower())):
			state_cols.append(i)

# Store data in dictionaries
	occupations = {}
	total_certified_applications_occupation = 0
	total_certified_applications_states = 0
	states = {}
	for record in records:
		info = record.split(';')
		if len(info)==1:
			continue
# Check if this record belongs to a certified application
		if info[status_col].lower()=='certified':
			

# Store the counter in the occupations dictionary
			if info[occupation_col] == "":
				continue
			elif info[occupation_col] in occupations:
				occupations[info[occupation_col]] += 1
				total_certified_applications_occupation += 1
			else:
				occupations[info[occupation_col]] = 1
				total_certified_applications_occupation += 1

# Store the counter in the states dictionary
			for col in state_cols:
				if info[col] == "":
					continue
				elif info[col] in states:
					states[info[col]] += 1
					total_certified_applications_states += 1
				else:
					states[info[col]] = 1
					total_certified_applications_states += 1


# Counters have been stored for occupations and states
# Evaluate metrics for occupations
with open(sys.argv[2],'w') as file:
	file.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
	ct = 0
	for key, value in sorted(sorted(occupations.items(), key= lambda x: x[0]),key = lambda x : x[1],reverse=True):
		file.write("%s;%d;%3.1f%%\n"%(key,value,100*value/total_certified_applications_occupation))
		ct=ct+1
		if ct==10:
			break

with open(sys.argv[3],'w') as file:
	file.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
	ct = 0
	for key, value in sorted(sorted(states.items(), key= lambda x: x[0]),key = lambda x : x[1],reverse=True):
		file.write("%s;%d;%3.1f%%\n"%(key,value,100*value/total_certified_applications_states))
		ct=ct+1
		if ct==10:
			break