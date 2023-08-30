import rdflib
from rdflib import Graph, Namespace, RDF, RDFS, URIRef, Literal, XSD
import random

# Creating the empty graph
g = Graph()

# Defining the RDF namespaces
product_entity =  Namespace("https://kastle-lab.org/ontology/")
#part_entity =  Namespace("https://kastle-lab.org/ontology/Part#")

schema = Namespace("http://schema.org/")
rdf = RDF
rdfs = RDFS

# Bind the prefixes into the graph
g.bind("supply_chain", product_entity)
g.bind("schema", schema)
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)

# Total number of products
N = 5 

# Generate products and their parts
products = [f"N_{i}" for i in range(1, N + 1)]
parts = [f"P_{i}" for i in range(1, 10)]

# Create a dictionary to store part relationships
part_relationships = {part: [] for part in parts}

# Initialize a dictionary to track sub parts
part_descendants = {part: [] for part in parts}

#recursive function to add child parts
def parts_tree(part, product_uri):
    part_uri = product_entity[part]
    g.add((part_uri, rdf.type, schema.Part))
    g.add((part_uri, rdfs.label, Literal(part)))
    g.add((product_uri, schema.hasPart, part_uri))

    if part in part_relationships:
        descendants = part_relationships[part]
        for descendant in descendants:
            parts_tree(descendant, product_uri)

# Create relationships
for part in parts:
    num_related_parts = random.randint(0, len(parts) // 2)
    # exclude the same part and inverse sub part relation to be added
    related_parts = random.sample([p for p in parts if p != part and p not in part_descendants[part]], num_related_parts)
    part_relationships[part] = related_parts
    # Update part descendants
    for related_part in related_parts:
        part_descendants[related_part].extend(part_descendants[part] + [part])


print("related parts are",part_relationships)

for product in products:
    product_uri = product_entity[product]
    g.add((product_uri, rdf.type, schema.Product))
    g.add((product_uri, rdfs.label, Literal(product)))

    # Generate random parts for the product
    num_parts = random.randint(1, len(parts))
    selected_parts = random.sample(parts, num_parts)

    for part in selected_parts:
        parts_tree(part, product_uri)
# Add relationships between parts
for part, related_parts in part_relationships.items():
    part_uri = product_entity[part]
    for related_part in related_parts:
        related_part_uri = product_entity[related_part]
        g.add((part_uri, schema.isPartOf, related_part_uri))



# Serializing the graph into turtle format
output_file = "product_parts_graph.ttl"
g.serialize(destination=output_file, format="turtle")
