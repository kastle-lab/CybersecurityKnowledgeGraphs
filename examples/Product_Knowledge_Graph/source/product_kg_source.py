import csv
from rdflib import Graph, Namespace, RDF, RDFS, URIRef, Literal, XSD

#Creating the empty graph
g = Graph()

#Defining the RDF namespaces
supply_chain = Namespace("https://kastle-lab.org/ontology/supply_chain#")
schema = Namespace("http://schema.org/")
rdf = RDF
rdfs = RDFS

#Bind the prefixes into the graph
g.bind("supply_chain", supply_chain)
g.bind("schema", schema)
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)

#Defining trust scores of countries based on their political parties Just a Random Values
trust_scores = {
    "China": 0.78,
    "Vietnam": 0.75,
    "India": 0.80,
    "Taiwan": 0.75,
    "South Korea": 0.80,
    "Japan": 0.84,
    "USA": 0.85
}

#Reading the supply chain data from csv file
with open('supply_chain_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        organization = row['Organization']
        product = row['Product']
        facility = row['IndustrialFacility']
        location = row['Location']
        government = row['Government']

        # Creating URI for the organization, product, and facility
        # Replace the spaces it creates a problem while creating URI
        org_uri = supply_chain[organization.strip().replace(" ", "_")]
        product_uri = supply_chain[product.strip().replace(" ", "_")]
        facility_uri = supply_chain[facility.strip().replace(" ", "_")]

        # Adding triples related to the organization
        g.add((org_uri, rdf.type, schema.Organization))
        g.add((org_uri, rdfs.label, Literal(organization,datatype=XSD.string)))

        # Adding triples related to the product
        g.add((product_uri, rdf.type, schema.Product))
        g.add((product_uri, rdfs.label, Literal(product,datatype=XSD.string)))

        # Adding triples related to the facility
        g.add((facility_uri, rdf.type, schema.IndustrialFacility))
        g.add((facility_uri, rdfs.label, Literal(facility,datatype=XSD.string)))
        g.add((facility_uri, schema.residesInCountry, Literal(location,datatype=XSD.string)))
        g.add((facility_uri, schema.hasGovernment, Literal(government,datatype=XSD.string)))

        # Linking organization, product, and facility
        g.add((org_uri, schema.acquires, product_uri))
        g.add((facility_uri, schema.produces, product_uri))
        g.add((product_uri, schema.isManufacturedAt,facility_uri ))

# Reading the product parts data from csv file
with open('product_parts_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        product = row['Product']
        part = row['Part']
        facility = row['IndustrialFacility']
        location = row['Location']
        government = row['Government']

        # Creating URI for the product and part
        product_uri = supply_chain[product.strip().replace(" ", "_")]
        part_uri = supply_chain[part.strip().replace(" ", "_")]
        facility_uri = supply_chain[facility.strip().replace(" ", "_")]
        government_uri = supply_chain[government.strip().replace(" ", "_")]

        # Adding triples related to the part
        g.add((part_uri, rdf.type, schema.Part))
        g.add((part_uri, rdfs.label, Literal(part,datatype=XSD.string)))
        g.add((part_uri, schema.isMadeIn, facility_uri))
        g.add((part_uri, schema.hasGovernment, Literal(government,datatype=XSD.string)))

        # Linking product and part
        g.add((product_uri, schema.hasPart, part_uri))

        # Linking product with its manufacturing country and trust score
        country_uri = supply_chain[location.strip().replace(" ", "_")]
        g.add((country_uri, rdf.type, schema.Country))
        g.add((product_uri, schema.isManufacturedAt, facility_uri))
        g.add((facility_uri, schema.residesInCountry, country_uri))
        g.add((country_uri, schema.hasGovernment, Literal(government,datatype=XSD.string)))
        g.add((government_uri, schema.hasTrustScore, Literal(float(trust_scores.get(location, 0)), datatype=XSD.float)))

# Serializing the graph into turtle format for querying purposes
output_file = "product_knowledge_graph.ttl"
g.serialize(destination=output_file, format="turtle")
