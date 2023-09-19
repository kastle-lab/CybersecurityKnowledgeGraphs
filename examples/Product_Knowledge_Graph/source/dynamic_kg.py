import rdflib
from rdflib import Graph, Namespace, RDF, RDFS, Literal, XSD
import random,sys

# Create an RDF graph
g = Graph()

# Define RDF namespaces
product_entity = Namespace("https://kastle-lab.org/ontology/")
gnis = Namespace("http://gnis-ld.org/lod/gnis/ontology/country")
schema = Namespace("http://schema.org/")
rdf = RDF
rdfs = RDFS

# Bind namespaces to the graph
g.bind("supply_chain", product_entity)
g.bind("schema", schema)
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("gnis",gnis)

#function to generate the products and parts in a sequence
def generate_products_and_parts(N,P):
    products = [f"N_{i}" for i in range(1, N + 1)]
    parts = [f"P_{i}" for i in range(1, P)]
    return products, parts

#function to create the part relationships
def create_part_relationships(parts):
    part_relationships = {part: [] for part in parts}
    part_descendants = {part: [] for part in parts}
    for part in parts:
        num_related_parts = random.randint(1, 6)
        related_parts = random.sample(
            [p for p in parts if p != part and p not in part_descendants[part] and part not in part_descendants[p]],
            num_related_parts
        )
        part_relationships[part] = related_parts
        for related_part in related_parts:
            part_descendants[related_part].extend(part_descendants[part] + [part])

    return part_relationships, part_descendants

#function to check if their is any cyclic relationships between parts
def is_cyclic(part, descendant, part_relationships):
    visited = set()
    stack = [(part, iter(part_relationships[part]))]

    while stack:
        part, descendants = stack[-1]
        for next_descendant in descendants:
            if next_descendant == descendant:
                return True
            if next_descendant not in visited:
                visited.add(next_descendant)
                stack.append((next_descendant, iter(part_relationships[next_descendant])))
                break
        else:
            stack.pop()

    return False

# function to make part heirarchy
def add_part_and_descendants(part, product_uri, part_relationships):
    part_uri = product_entity[part]

    g.add((product_uri, schema.hasPart, part_uri))

    if part in part_relationships:
        descendants = part_relationships[part]
        for descendant in descendants:
            if not is_cyclic(part, descendant, part_relationships):
                add_part_and_descendants(descendant, product_uri, part_relationships)
            else:
                print(f"Cyclic relationship detected between {part} and {descendant}")

# function to generate the random data for manfacturing details
def gen_manfacturing_data():
    countries = ["USA", "China", "India", "Taiwan", "Vietnam","SouthKorea","Russia","Canada","UK","Japan","HongKong"]
    manufacturing_units = ["FoxconnUnit", "TataIndustriesUnit", "AppleUnit", "NvidiaUnit", "TSMCUnit","3MUnit","Intel","Redington"]
    organizations = ["Apple", "Samsung", "Nvidia", "Acer", "Asus","AMD","Intel","Redington"]

    #creating country uris
    for country in countries:
        country_uri = gnis[country]
        g.add((country_uri, rdf.type, schema.Country))
        g.add((country_uri, rdfs.label, Literal(country)))

    manufactured_data={}
    
    manufactured_data["countryOfAssembly"] = random.choice(countries)
    manufactured_data['countryOfLastProcessing'] = random.choice(countries)
    manufactured_data['countryOfOrigin'] = random.choice(countries)
    manufactured_data['manufacturer'] = random.choice(organizations)

    return manufactured_data

# Funcion to create and serialize(.ttl format) the knowledge graph
def create_and_serialize_knowledge_graph(products, parts):
    product_relationships, part_descendants = create_part_relationships(parts)
    flag = False

    for product in products:
        product_uri = product_entity[product]
        
        g.add((product_uri, rdf.type, schema.Product))
        g.add((product_uri, rdfs.label, Literal(product)))
        
        #function call to generate the product details
        product_details = gen_manfacturing_data()
        #organization uri
        org_uri = product_entity[product_details["manufacturer"]]
        g.add((org_uri, rdf.type, schema.Organization))
        g.add((org_uri, rdfs.label, Literal(product_details["manufacturer"])))
        #adding manufacturing details to the knwoledge graph
        g.add((product_uri, schema.countryOfAssembly, gnis[product_details["countryOfAssembly"]]))
        g.add((product_uri, schema.countryOfLastProcessing,gnis[product_details["countryOfLastProcessing"]]))
        g.add((product_uri, schema.countryOfOrigin, gnis[product_details["countryOfOrigin"]]))
        g.add((product_uri, schema.manufacturer,org_uri))
        num_parts = random.randint(1, len(parts)//2)
        selected_parts = random.sample(parts, num_parts)

        for part in selected_parts:
            add_part_and_descendants(part, product_uri, product_relationships)

    for part, related_parts in product_relationships.items():
        part_uri = product_entity[part]
        #function call to generate the part details
        product_details = gen_manfacturing_data()
        #organization uri
        org_uri = product_entity[product_details["manufacturer"]]
        g.add((org_uri, rdf.type, schema.Organization))
        g.add((org_uri, rdfs.label, Literal(product_details["manufacturer"])))
        #adding manufacturing details to the knwoledge graph
        g.add((part_uri, schema.countryOfAssembly, gnis[product_details["countryOfAssembly"]]))
        g.add((part_uri, schema.countryOfLastProcessing,gnis[product_details["countryOfLastProcessing"]]))
        g.add((part_uri, schema.countryOfOrigin, gnis[product_details["countryOfOrigin"]]))
        g.add((part_uri, schema.manufacturer,org_uri))
        for related_part in related_parts:
            related_part_uri = product_entity[related_part]
            g.add((part_uri, rdf.type, schema.Part))
            g.add((part_uri, rdfs.label, Literal(part)))
            g.add((part_uri, schema.isPartOf, related_part_uri))
    output_file = "product_parts_graph.ttl"
    g.serialize(destination=output_file, format="turtle")

    if flag == False:
        print(f"Knowledge Graph Created Successfully and stored in {output_file}")

if __name__ == "__main__":
    # Number of products through CLI args
    N = int(sys.argv[1])
    # Number of parts through CLI args
    P = int(sys.argv[2])
    products, parts = generate_products_and_parts(N,P)
    create_and_serialize_knowledge_graph(products, parts)
