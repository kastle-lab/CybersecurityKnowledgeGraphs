from rdflib import Graph, Namespace, Literal, RDF, RDFS
import csv

# Create an RDF graph
g = Graph()

# Define namespaces
ns = {
    "kastle": Namespace("https://kastle-lab.org/ontology/"),
    "schema" : Namespace("http://schema.org/"),
    "rdf": RDF,
    "rdfs": RDFS,
}

# Bind namespaces to the graph
for prefix, namespace in ns.items():
    g.bind(prefix, namespace)

# Initialize empty lists to store data
hardware_components_data = []
vulnerabilities_data = []

# Read hardware components from the CSV file
with open('hardware_components.csv', 'r') as hardware_file:
    hardware_reader = csv.DictReader(hardware_file)
    for row in hardware_reader:
        hardware_components_data.append(row)

# Read vulnerabilities from the CSV file
with open('vulnerabilities.csv', 'r') as vulnerabilities_file:
    vulnerabilities_reader = csv.DictReader(vulnerabilities_file)
    for row in vulnerabilities_reader:
        vulnerabilities_data.append(row)

# Create triples for hardware components and vulnerabilities
for component in hardware_components_data:
    component_uri = ns["kastle"][component['Name']]
    g.add((component_uri, ns["rdf"].type, ns["schema"]["Product"]))
    g.add((component_uri, ns["rdfs"].label, Literal(component['Name'])))

for vulnerability in vulnerabilities_data:
    vulnerability_uri = ns["kastle"][vulnerability['Name']]
    g.add((vulnerability_uri, ns["rdf"].type, ns["schema"]["Vulnerability"]))
    g.add((vulnerability_uri, ns["rdfs"].label, Literal(vulnerability['Name'])))

# Read relationships from the CSV file
relationships_data = []
with open('relationships.csv', 'r') as relationships_file:
    relationships_reader = csv.DictReader(relationships_file)
    for row in relationships_reader:
        relationships_data.append(row)

# Define relationships from the CSV data
for relationship in relationships_data:
    vulnerability = relationship['Vulnerability']
    component = relationship['Hardware_Component']
    g.add((ns["kastle"][vulnerability], ns["kastle"]["affects"], ns["kastle"][component]))

# Serialize the RDF graph in Turtle format
output_file = "hw_vuln_kg.ttl"
g.serialize(destination=output_file, format="turtle")
