# Team Project_OIM3640

## Fall 2022 Final project OIM3640

<h3><b>Team Members: Jean Albino, Sakshyam Tripathi </b></h3>
<br>

###  Big Idea
Create a program that generates food recipes that fit user criteria such as cuisine, dietary restrictions, or nutritional goals.

### Learning Goals
* Using new APIs and scraping techniques to interact with websites and parse website data.

* Improve text analysis skills in python through enhanced data cleaning and other methods.

* Collaborating through GitHub and simulate a real life coding project.


### Implementation Plan
* Look through available food APIs on the internet and decide on a suitable one that meets our needs. 

* Read through the documentation to understand the inner workings of the API and the structure of the data it returns.

* Classify each recipe into certain categories for each of the user’s possible criterion.

* Aggregate user’s criteria to sort recipes.

* Finally return a randomized recipe from the list of suitable recipes.

### Collaboration Plan
* One team member created a master repository that would be the base of the program. The other team member forked the repository to facilitate digital collaboration.

* Timely team meeting to brainstorm ideas and some possible pair programming and debugging.

### Risks
* Risk of being unable to obtain relevant data due to proprietary issues or to understand the data structure.

* A real risk for the success of the project will be the team’s ability to sufficiently clean the data of words in job descriptions that are not indicative of requirements

* Another risk will be the team’s ability to accurately categorize different words that describe the same skill into one “box” without excluding any requirements or generalizing



## Code Implementation 

### Imported Libraries
* json
* random
* request
* Flask

## Running the Code
### Only Run 'app.py'
The code is rather simple to run. All the required importations are already in the python script so no manual installation is required. Further our code requires no manual backend input. Simply running the app.py file will start running the flask application and generate a local host server. The user can then access the link by pressing on the server link created in the terminal. The webpage then has the required form entries where user input is needed to give a viable output. 
If consistent "error 404" is generated, verify that the app.route in app.py is set to '/'. The flask server port can be changed by editing the port variable in line 29 of app.py