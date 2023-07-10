import csv
from rdflib import Graph, Namespace, RDF, RDFS, URIRef, Literal , XSD

# Creating the empty graph
g = Graph()

# Defining the RDF namespaces
fam = Namespace("http://kandula.com/family#")
schema = Namespace("http://schema.org/")
rdf = RDF
rdfs = RDFS

# Bind the prefixes into the graph
g.bind("fam", fam)
g.bind("schema", schema)
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
        g.add((person_uri, rdf.type, schema.Person))
        g.add((person_uri, rdfs.label, Literal(name)))
        g.add((person_uri, schema.hasAge, Literal(age,datatype=XSD.integer)))
        g.add((person_uri, schema.gender, Literal(gender)))

        
        # Creating the URI for the country if present in data   
        if country:
            country_uri = fam[country.strip()]
            g.add((person_uri, schema.livesInCountry, country_uri))
            g.add((country_uri, rdf.type, schema.Country))
            g.add((country_uri, rdfs.label, Literal(country)))
        
        # creating uri for city if present in data
        if city:
            city_uri = fam[city.strip()]
            country_uri = fam[country.strip()]
            g.add((person_uri, schema.livesInCity, city_uri))
            g.add((city_uri, schema.containedInPlace, country_uri))
            g.add((city_uri, rdf.type, schema.Place))
            g.add((city_uri, rdfs.label, Literal(city)))
            
        # creating uri for occupation if present in data
        if occupation:
            occupation_uri = fam[occupation.strip().replace(" ", "_")]
            g.add((person_uri, schema.hasOccupation, occupation_uri))
            g.add((occupation_uri, rdf.type, schema.Occupation))
            g.add((occupation_uri, rdfs.label, Literal(occupation)))
        

        # Add father info if present in data
        if father:
            #linking the parent with the uri
            father_uri = fam[father.strip()]
            g.add((person_uri, schema.father, father_uri))
            #defining inverse relationships
            g.add((father_uri, fam.isFatherOf,person_uri ))
            g.add((father_uri, rdf.type, schema.Person))
            g.add((father_uri, rdfs.label, Literal(father)))

        # Add mother info if present in data
        if mother:
            #linking the parent with the uri.
            mother_uri = fam[mother.strip()]
            g.add((person_uri, schema.mother, mother_uri))
            #defining inverse relationships
            g.add((mother_uri, fam.isMotherOf,person_uri ))
            g.add((mother_uri, rdf.type, schema.Person))
            g.add((mother_uri, rdfs.label, Literal(mother)))

        # Add spouse info if present in data
        if spouse:
            spouse_uri = fam[spouse.strip()]
            if gender == "Male":
                g.add((person_uri, schema.hasWife, spouse_uri))
                g.add((spouse_uri, rdf.type, schema.Person))
                g.add((spouse_uri, rdfs.label, Literal(spouse)))
            elif gender == "Female":
                g.add((person_uri, schema.hasHusband, spouse_uri))
                g.add((spouse_uri, rdf.type, schema.Person))
                g.add((spouse_uri, rdfs.label, Literal(spouse)))

        # Add children info if present in data
        if children:
            # One person can have multiple children. Data is seperate with commas.
            children_list = children.split(',')
            for child in children_list:
                child_uri = fam[child.strip()]
                g.add((person_uri, schema.child, child_uri))
                g.add((child_uri, rdf.type, schema.Person))
                g.add((child_uri, rdfs.label, Literal(child)))

# Serializing the graph into turtle format to query using SPARQL
output_file = "family_graph.ttl"
g.serialize(destination=output_file, format="turtle")