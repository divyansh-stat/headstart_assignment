# headstart_assignment

Task to fetch github issues and some relevant information regarding those issues. Build visualisation on top of the fetched data from github using their API.

### Steps taken

1. Created a setup file with configurations of the fetch function

This setup file is the backbone of the Fetch commandline function that is created in the next steps. It calls the python module and the function inside that module that is to be run to implement the fetch commandline function.

2. Created a shell script to get token for authentication

In this step, using basic html authentication method, a token is created that is to be used to access the GitHub API. Input to this script are the credentials of my username. Output is a token and hashed token that is used to fetch the issues in the next step.

3. Created a shell script to fetch Issues of a particular Repository (randomly picked)

In this step, a random Repo is picked and using the token generated in the previous step and the guidelines of fetching issues mentioned the GitHub API documentation, 30 issues are picked. These issues are in order of time of last comment. The output is a json object (txt) with 30 issues and summary of emoji reactions. This script is not run yet, in fact, it will be passed in the click module's fetch function.

4. Created a Fetch python script

From the last step, the shell script is passed in the fetch module that pretty prints the relevant data and first 5 issues. Running the fetch command in the terminal gives the list of 5 issues within that repo sorted by latest comment time (default parameter).

5. Created a python script to convert the json to csv

This script is used to convert the json file to a csv with headers.

6. Created a plot python file that visualises the data fetched and processed using the GitHub API

This script has two plot scripts - First one plots the frequency of each emoji reactions and the Second plots the total number of reactions by number of comments. 

### Notes

Due to very less experience with API, could not fetch public issues. Instead picked a random Repo and fetch 30 issues sorted by latest comment. The resultant set had very few reactions and thus plotting 3 and 4 visualisations from the task didn't make sense. 

Overall, the task was very challenging as it focused more on software skills than data science/statistical knowledge. Can do better with more experience with APIs. 

### Speed

Total time taken was 7 hours. First two hours were spent on setting up laptop from scratch, installing brew, python and other packages. 
Due to very less experience with API, spent another 2 hours reading and testing different functions from the GitHub API. Struggled for 1 hour with the authentication and trying to write a python script. Next 1 hour was spent in writing the fetch function and the last 1 hour was spent in processing the json output and plotting the results.

### How to run

1. After extracting the whole package, change the credentials to own github profile's in the oauth.sh file. 
2. Run oauth.sh file in the terminal (which should create a txt file of token)
3. Run fetch.py from the command line (this should print the first 5 issues of the repo selected)
4. Run create_csv_of_json_issues.py
5. Run /visualisation/plot.py 
