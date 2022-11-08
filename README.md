# Election_Analysis
## Project Overview
A Colorado Board of Elections employee needs the following tasks to be completed in order to carry out the election audit of a recent local congressional election.
 1. Calculate the total number of votes cast.
 2. Get a complete list of candidates who received votes.
 3. Calculate the total number of votes each candidate received.
 4. Calculate the percentage of votes each candidate won.
 5. Determine the winner of the election based on popular vote.
## Resources
  - Data Source: election_results.csv
  - Software: Python 3.7.6, Visual Studio Code, 1.73.0
## Summary
The analysis of the election shows that:

  - There were 369,711 votes cast in the election.
  - The counties in the election were:
    - Jefferson County
    - Denver County
    - Arapahoe County
  - Breakdown of votes by county:
    - Jefferson County: 10.5% of votes cast with 38,855 votes.
    - Denver County: 82.8% of votes cast with 306,055 votes.
    - Arapahoe County: 6.7% of votes cast with 24,801 votes.
  - The county with the largest number of votes:
    - Denver County: 82.8% of the vote and 306,055 votes. 
  - The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
  - The candidate results breakdown:
    - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
    - Diana DeGette received 73.8% of the vote with 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
  - The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote with 272,892 votes.
## Election Audit Summary
This code was written so that it could be applied to any local election with minimal manual changes. One area where the code is sensitive to change is format of the source data. The candidate and county names must remain in the same columns, or the script will not function properly. If the data source has a different format, the script will need to be altered to accommodate. 

Image 1: Candidate Name Code

![Candidate name code]( https://github.com/TravisTornquist/Election-Analysis/blob/main/Resources/Candidate_Name_Code.png?raw=true)

If the format for the source data is different, the index of the row variable will need to be changed so that the script is pulling the candidate name from the correct column. Remember that the index starts at 0 for the first column.

Image 2: County Name Code

![County name code](https://github.com/TravisTornquist/Election-Analysis/blob/main/Resources/County_Name_Code.png?raw=true)

If the format for the source data is different, the index of the row variable will need to be changed so that the script is pulling the county name from the correct column. Remember that the index starts at 0 for the first column.
