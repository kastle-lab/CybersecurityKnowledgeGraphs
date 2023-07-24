## Welcome to my independent study on Knowledge Graphs 

### Introduction to the Data :

The CSV file contains data of my family members.

There are 10 columns:

* `Name` : Name of Person.
* `Age` : 
* `Gender` : 
* `Father` : Father's name (if available)
* `Mother` :  Mother's name (if available)
* `Spouse` : Spouse name (if available)
* `Children` :  List of children (if available)
* `Occupation`: 
* `City`: City where the person lives.
* `Country`: Country of the City.

## Competency Questions:

1) Querying the data for finding the father or mother of particular person.
2) Querying the data for finding spouse/children of particular person.
3) Finding the brother/sister(s) for particular. (This should be done by inferencing, updating the rules)

## Challenges:
* If the relationship is not specified in the data, by applying rules for the graph, it should be able to find the relationship between persons. (We can say brother is level1 relation, grandparents is level2 and etc.)
* If we specify more relations/rules, there will be more noise created. We need to find the relation upto certain point?
