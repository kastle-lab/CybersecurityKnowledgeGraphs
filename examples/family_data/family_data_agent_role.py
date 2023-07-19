import csv
from rdflib import Graph, Namespace, RDF, RDFS, URIRef, Literal, XSD

# Creating the empty graph
g = Graph()

# Defining the RDF namespaces
fam = Namespace("http://kandula.com/family#")
schema = Namespace("http://schema.org/")
rdf = RDF
rdfs = RDFS
time = Namespace("http://www.w3.org/2006/time#")

# Bind the prefixes into the graph
g.bind("fam", fam)
g.bind("schema", schema)
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("time", time)

# Reading the family data from csv file
# for a better experience, we can pass the file name through CLI arguments
with open('Agent_Role_Data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Name']
        age = row['Age']
        gender = row['Gender']
        dob = row['DOB']
        father = row['Father']
        mother = row['Mother']
        spouse = row['Spouse']
        children = row['Children']
        occupation = row['Occupation']
        parent_te = row['Parent_TE']
        marriage_te = row['Marriage_TE']

        # Creating URI for the person
        # strip the spaces it creates a problem while creating URI
        person_uri = fam[name.strip()]

        # Adding triples related to the person
        g.add((person_uri, rdf.type, schema.Person))
        g.add((person_uri, rdfs.label, Literal(name)))
        g.add((person_uri, schema.hasAge, Literal(age, datatype=XSD.integer)))
        g.add((person_uri, schema.gender, Literal(gender)))
        g.add((person_uri, schema.dateOfBirth, Literal(dob, datatype=XSD.date)))

        # Define temporal extent for father role, it just has the start time
        if gender =="Male" and parent_te:
            father_extent_uri = fam[name.strip() + "_FatherRole"]
            g.add((father_extent_uri, rdf.type, time.Interval))
            g.add((father_extent_uri, time.hasBeginning, URIRef(father_extent_uri + "_Begin")))
            g.add((URIRef(father_extent_uri + "_Begin"), rdf.type, time.Instant))
            g.add((URIRef(father_extent_uri + "_Begin"), time.inXSDDate, Literal(parent_te, datatype=XSD.gYear)))
            g.add((person_uri, schema.hasRole, father_extent_uri))

        # Define temporal extent for mother role, it just has the start time
        if gender == "Female" and parent_te:
            mother_extent_uri = fam[name.strip() + "_MotherRole"]
            g.add((mother_extent_uri, rdf.type, time.Interval))
            g.add((mother_extent_uri, time.hasBeginning, URIRef(mother_extent_uri + "_Begin")))
            g.add((URIRef(mother_extent_uri + "_Begin"), rdf.type, time.Instant))
            g.add((URIRef(mother_extent_uri + "_Begin"), time.inXSDDate, Literal(parent_te, datatype=XSD.gYear)))
            g.add((person_uri, schema.hasRole, mother_extent_uri))

        # Define temporal extent for marriage role, it just has the start time(as of now as no one is divorced till now, hope it just contains the start date only)
        if spouse and marriage_te:
            marriage_extent_uri = fam[name.strip() + "_MarriageRole"]
            g.add((marriage_extent_uri, rdf.type, time.Interval))
            g.add((marriage_extent_uri, time.hasBeginning, URIRef(marriage_extent_uri + "_Begin")))
            g.add((URIRef(marriage_extent_uri + "_Begin"), rdf.type, time.Instant))
            g.add((URIRef(marriage_extent_uri + "_Begin"), time.inXSDDate, Literal(marriage_te, datatype=XSD.gYear)))
            g.add((person_uri, schema.hasRole, marriage_extent_uri))
        # Define temporal extent for child role.
        # Child role begins for every at the time of birth for every individual. it just has the start role as once a child, he/she is child for whole life.
        if dob:
            child_extent_uri = fam[name.strip() + "_ChildRole"]
            g.add((child_extent_uri, rdf.type, time.Interval))
            g.add((child_extent_uri, time.hasBeginning, URIRef(child_extent_uri + "_Begin")))
            g.add((URIRef(child_extent_uri + "_Begin"), rdf.type, time.Instant))
            g.add((URIRef(child_extent_uri + "_Begin"), time.inXSDDate, Literal(dob, datatype=XSD.gYear)))
            g.add((person_uri, schema.hasRole, child_extent_uri))
            

        # Add father info if present in data
        if father:
            # Linking the parent with the URI
            father_uri = fam[father.strip()]
            g.add((person_uri, schema.father, father_uri))
            # Defining inverse relationships
            g.add((father_uri, fam.isFatherOf, person_uri))
            g.add((father_uri, rdf.type, schema.Person))
            g.add((father_uri, rdfs.label, Literal(father)))

        # Add mother info if present in data
        if mother:
            # Linking the parent with the URI.
            mother_uri = fam[mother.strip()]
            g.add((person_uri, schema.mother, mother_uri))
            # Defining inverse relationships
            g.add((mother_uri, fam.isMotherOf, person_uri))
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
            # One person can have multiple children. Data is separate with commas.
            children_list = children.split(',')
            for child in children_list:
                child_uri = fam[child.strip()]
                g.add((person_uri, schema.hasChild, child_uri))
                g.add((child_uri, rdf.type, schema.Person))
                g.add((child_uri, rdfs.label, Literal(child)))

# Serializing the graph into turtle format to query using SPARQL
output_file = "family_graph_agent_roles.ttl"
g.serialize(destination=output_file, format="turtle")
