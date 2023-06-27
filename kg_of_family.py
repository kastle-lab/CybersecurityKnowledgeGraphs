import csv
from rdflib import Graph, Namespace, RDF, RDFS, URIRef, Literal

# Creating the empty graph
g = Graph()

# Defining the RDF namespaces
fam = Namespace("http://kandula.com/family")
rdf = RDF
rdfs = RDFS

# Bind the prefixes into the graph
g.bind("fam", fam)
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)

# Reading the family data from csv file
# for a better experience we can pass the file through CLI arguments
with open('family_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Name']
        age = row['Age']
        gender = row['Gender']
        father = row['Father']
        mother = row['Mother']
        spouse = row['Spouse']
        children = row['Children']
        occupation = row['Occupation']
        city = row['City']
        country = row['Country']

        # Creating URI for the person
        # strip the spaces it creates problem while creating URI
        person_uri = fam[name.strip()]

        # Adding triples related to the person
        g.add((person_uri, rdf.type, fam.Person))
        g.add((person_uri, rdfs.label, Literal(name)))
        g.add((person_uri, fam.age, Literal(age)))
        g.add((person_uri, fam.gender, Literal(gender)))
        g.add((person_uri, fam.occupation, Literal(occupation)))
        g.add((person_uri, fam.residesInCity, Literal(city)))
        g.add((person_uri, fam.residesInCountry, Literal(country)))

        # Add father info if present in data
        if father:
            #linking the parent with the uri.
            father_uri = fam[father.strip()]
            g.add((person_uri, fam.hasFather, father_uri))
            #defining inverse relationships
            g.add((father_uri, fam.isFatherOf,person_uri ))
            g.add((father_uri, rdf.type, fam.Parent))
            g.add((father_uri, rdfs.label, Literal(father)))

        # Add mother info if present in data
        if mother:
            #linking the parent with the uri.
            mother_uri = fam[mother.strip()]
            g.add((person_uri, fam.hasMother, mother_uri))
            #defining inverse relationships
            g.add((mother_uri, fam.isMotherOf,person_uri ))
            g.add((mother_uri, rdf.type, fam.Parent))
            g.add((mother_uri, rdfs.label, Literal(mother)))

        # Add spouse info if present in data
        if spouse:
            spouse_uri = fam[spouse.strip()]
            if gender == "Male":
                g.add((person_uri, fam.hasWife, spouse_uri))
                g.add((spouse_uri, rdf.type, fam.Person))
                g.add((spouse_uri, rdfs.label, Literal(spouse)))
            elif gender == "Female":
                g.add((person_uri, fam.hasHusband, spouse_uri))
                g.add((spouse_uri, rdf.type, fam.Person))
                g.add((spouse_uri, rdfs.label, Literal(spouse)))

        # Add children info if present in data
        if children:
            # One person can have multiple children. Data is seperate with commas.
            children_list = children.split(',')
            for child in children_list:
                child_uri = fam[child.strip()]
                g.add((person_uri, fam.hasChild, child_uri))
                g.add((child_uri, rdf.type, fam.Person))
                g.add((child_uri, rdfs.label, Literal(child)))

# Serializing the graph into turtle format to query using SPARQL
output_file = "family_graph.ttl"
g.serialize(destination=output_file, format="turtle")