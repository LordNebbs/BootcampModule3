
from optparse import Values


counties=["Arapahone","Denver","Jefferson"]
counties_tuple=["Arapahoe","Denver","Jefferson"]

counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]



for county in counties:
    print(county)

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for key, value in counties_dict.items():
    print(key,value)


# same solution but different appoaches ^v
for key, value in counties_dict.items():
    print(key,' county has ',value,' registered voters.')

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")




for i in range(len(voting_data)):
    print(voting_data[i]['county'])


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#How many votes did you get?
candidate_votes = int(input("How many votes did the candidate get in the election?"))

#Total votes in the election
total_votes = int(input("What is the total votes in the election?"))

#Calculate the percentage of votes you received.

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes/total_votes*100:.2f}% of the total votes."
)

print(message_to_candidate)


for county,voters in counties_dict.items():
    print(
    f"{county} county has {voters:,} registered voters."
)

#for county_dict in voting_data:
#    for key, value in counties_dict.items():
 #       print(
  #          f"{county} county has {voters:,} registered voters."
   #     )