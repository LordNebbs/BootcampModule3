#### BootcampModule3

# Election_Analysis

## Overview of Election Audit:
Using a provided data, we are auditing raw voter data covering a Colorado congressional precinct covering Jefferson, Denver, and Arapahoe counties. Using various code to filter and create useable information, we were able to determine the candidates, how many votes they received, where they came from and the winner of the election.

## Election-Audit Results:

![Election count](https://github.com/LordNebbs/BootcampModule3/blob/main/Resources/Election%20Vote%20count.png)

The precinct had a total vote count of 369,711 votes accross the three counties.

This was determined by isolating and defining the ammount of rows (minus the header) to count the unique vote entries. 

        for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1


We then sorted each vote based on the county that provided it, calculate the percentages and format it so it was easily understood.

        for county_name in county_votes:
        # Retrieve the county vote count (new variable).
        cvotes=county_votes.get(county_name)
        # Calculate the percentage of votes for the county.
        cvote_percentage=float(cvotes)/float(total_votes)*100
         # Print the county results to the terminal.
        county_results = (f"{county_name}: {cvote_percentage: .1f}% ({cvotes:,})\n")
        print(county_results)
         # Print the county votes on the text file.
        txt_file.write(county_results)


Denver, with ~83% of the total made up the majority of the total count. We also were able to sort the data by the Candidates to output how many votes each received.

    #Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

Using this script we were able to call the election and declare that Diana DeGette, with 73.8% (272,892) of the total vote tally, won the election in a landslide.

![Election Results](https://github.com/LordNebbs/BootcampModule3/blob/main/Resources/Election%20results.png)

## Election-Audit Summary:
 This script provided a concise summary of the Colorado congressional election. However it would not take much to modify this program to handle other types of election or polling. For example (dataset/csv provided), you could exchange all the variables related to the candidates for Ballot Propositions. You could also expand this to run statewide senate races by expanding the lists and dictionaries to include every county, not just those in this particular election. Or further extrapolating to national races provided the county and state parameters were added to the dictionaries.