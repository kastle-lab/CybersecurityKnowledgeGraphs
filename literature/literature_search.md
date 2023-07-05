Paper-1: Hardware-agnostic computation for large-scale knowledge graph embeddings
================================================================================
Authors: Caglar Demir, Axel-Cyrille Ngonga Ngomo
==========================================
Abstract: 
==================
Knowledge graph embedding research has mainly focused on learning continuous representations of knowledge graphs towards the link prediction problem. 
Recently developed frameworks can be effectively applied in research related applications. Yet, these frameworks do not fulfill many requirements of 
real-world applications. As the size of the knowledge graph grows, moving computation from a commodity computer to a cluster of computers in these 
frameworks becomes more challenging. Finding suitable hyperparameter settings w.r.t. time and computational budgets are left to practitioners. In 
addition, the continual learning aspect in knowledge graph embedding frameworks is often ignored, although continual learning plays an important role in 
many real-world (deep) learning-driven applications. Arguably, these limitations explain the lack of publicly available knowledge graph embedding models 
for large knowledge graphs. We developed a framework based on the frameworks DASK, Pytorch Lightning and Hugging Face to compute embeddings for 
large-scale knowledge graphs in a hardware-agnostic manner, which is able to address real-world challenges pertaining to the scale of real application. We 
provide an open-source version of our framework along with a hub of pre-trained models having more than 11.4 B parameters.

Paper2: Knowledge Graph Embedding and Visualization for Pre-Silicon Detection of Hardware Trojans
================================================================================
Authors: Dmitry Utyamishev, Inna Partin-Vaisband
==========================================
Abstract: 
==================
While financially preferable, pre-silicon hardware Trojan (HT) detection remains a primary security challenge in modern integrated circuits (ICs) In this 
paper, a pre-silicon framework is developed for identifying rarely triggered nets (including those of HTs) Unsupervised knowledge graph embedding is 
utilized to transform the conditional triggering probability of IC nets into the Euclidean distance between the nets’ embeddings The proposed approach is 
not limited by HT types/IC sizes and is reference-free The framework is evaluated with TrustHub benchmarks, fully supporting the theoretical results HTs 
are identified in the center of the embeddings’ cloud, reducing the HT search space by over 10X.

Paper3: Exposing Hardware Trojans in Zero-Knowledge
================================================================================
Authors: Dimitris Mouris, Charles Gouert, Nektarios Georgios Tsoutsos
==========================================
Abstract: 
==================
As integrated circuit (IC) design and manufacturing have become highly globalized, hardware security risks become more prominent as malicious parties can 
exploit multiple stages of the supply chain for profit. Two potential targets in this chain are third-party intellectual property (3PIP) vendors and their 
customers. Untrusted parties can insert hardware Trojans into 3PIP circuit designs that can both alter device functionalities when triggered or create a 
side channel to leak sensitive information such as cryptographic keys. To mitigate this risk, the absence of Trojans in 3PIP designs should be verified 
before integration, imposing a major challenge for vendors who have to argue their IPs are safe to use, while also maintaining the privacy of their 
designs before ownership is transferred. To achieve this goal, in this work we employ modern cryptographic protocols for zero-knowledge proofs and enable 
3PIP vendors prove an IP design is free of Trojan triggers without disclosing the corresponding netlist. Our approach uses a specialized circuit compiler 
that transforms arbitrary netlists into a zero-knowledge-friendly format, and introduces a versatile Trojan detection module that maintains the privacy of 
the actual netlist

Paper4: A Knowledge Graph Perspective on Supply Chain Resilience
================================================================================
Authors: Yushan Liu, Bailan He, Marcel Hildebrandt, Maximilian Buchner,Daniela Inzko, Roger Wernert, Emanuel Weigel, Dagmar Beyer, Martin Berbalk and Volker Tresp
==========================================
Abstract: 
==================
Global crises and regulatory developments require increased supply chain transparency and resilience. 
Companies do not only need to react to a dynamic environment but have to act proactively and implement
measures to prevent production delays and reduce risks in the supply chains. However, information
about supply chains, especially at the deeper levels, is often intransparent and incomplete, making it
difficult to obtain precise predictions about prospective risks. By connecting different data sources,
we model the supply network as a knowledge graph and achieve transparency up to tier-3 suppliers.
To predict missing information in the graph, we apply state-of-the-art knowledge graph completion
methods and attain a mean reciprocal rank of 0.4377 with the best model. Further, we apply graph
analysis algorithms to identify critical entities in the supply network, supporting supply chain managers
in automated risk identification.

Paper5: Supply Chain Link Prediction on Uncertain Knowledge Graph
================================================================================
Authors: Nils Brockmann, Edward Elson Kosasih ,Alexandra Brintrup
=========================================
Abstract: 
==================
With manufacturing companies outsourcing to each other, multi-echelon supply chain networks emerge in which risks can propagate over multiple entities. 
Considerable structural and organizational barriers hamper obtaining the supply chain visibility that would be required for a company to monitor and 
mitigate these risks. Our work proposes to combine the automated extraction of supply chain relations from web data using NLP with augmenting the results 
using link prediction. For this, the first graph neural network based approach to model uncertainty in supply chain knowledge graph reasoning is shown. We 
illustrate our approach on a novel dataset and manage to improve the state-of-the-art performance by 60% in uncertainty link prediction. Generated 
confidence scores support real-world decision-making.

Paper6: The Construction of a Domain Knowledge Graph and Its Application in Supply Chain Risk Analysis
================================================================================
Authors: Wanyue Zhang, Yonggang Liu, Lihong Jiang, Nazaraf Shah, Xiang Fei, Hongming Cai 
=========================================
Abstract: 
==================
Domain knowledge graphs, which compose scattered information about domain entities, are expressive when organizing information for enterprise systems in 
the decision-making process. Such knowledge graphs can give us semantically-rich information which can later be applied to fuel different graph mining 
services to conduct analytical work. In this paper, we discuss a subject-oriented domain knowledge graph based on multi-source heterogenous data 
consisting of dynamic data generated from daily transactions among companies in interlacing supply-chains and relatively static data demonstrating the 
basic properties of these enterprises to assist with analytical work. Such high-dimensional graph with strong heterogeneity is rich in semantics and is 
casted into lower dimensions to be used as inputs for graph mining services, giving us various enterprise correlation chains, aiming to support 
upper-level application like credit risk assessment. The framework has been testified in real-life information systems.

Paper7: KnowGraph-PM: a Knowledge Graph based Pricing Model for Semiconductors Supply Chains
================================================================================
Authors: Nour Ramzy, Soren Auer, Javad Chamanara 
=========================================
Abstract: 
==================
Semiconductor supply chains are described by significant demand fluctuation that increases as one moves up the supply chain, the so-called bullwhip 
effect. To counteract, semiconductor manufacturers aim to optimize capacity utilization, to deliver with shorter lead times and exploit this to generate 
revenue. Additionally, in a competitive market, firms seek to maintain customer relationships while applying revenue management strategies such as dynamic 
pricing. Price change potentially generates conflicts with customers. In this paper, we present KnowGraph-PM, a knowledge graph-based dynamic pricing 
model. The semantic model uses the potential of faster delivery and shorter lead times to define premium prices, thus entail increased profits based on 
the customer profile. The knowledge graph enables the integration of customer-related information, e.g., customer class and location to customer order 
data. The pricing algorithm is realized as a SPARQL query that relies on customer profile and order behavior to determine the corresponding price premium. 
We evaluate the approach by calculating the revenue generated after applying the pricing algorithm. Based on competency questions that translate to SPARQL 
queries, we validate the created knowledge graph. We demonstrate that semantic data integration enables customertailored revenue management

Paper8: Smart supply chain management in Industry 4.0: the review, research agenda and strategies in North America
================================================================================
Authors: Guoqing Zhang, Yiqin Yang, Guoqing Yang 
=========================================
Abstract: 
==================
The emerging information and communication technologies (ICT) related to Industry 4.0 play a critical role to enhance supply chain 
performance. Employing the smart technologies has led to so-called smart supply chains. Understanding how Industry 4.0 and related ICT 
affect smart supply chains and how smart supply chains evolve with the support of the advanced technologies are vital to practical and 
academic communities. Existing review works on smart supply chains with ICT mainly rely on the academic literature alone. This paper 
presents an integrated approach to explore the effects of Industry 4.0 and related ICT on smart supply chains, by combining 
introduction of the current national strategies in North America, the research status analysis on ICT assisted supply chains from the 
major North American national research councils, and a systematic literature review of the subject. Besides, we introduce a smart 
supply chain hierarchical framework with multi-level intelligence. Furthermore, the challenges faced by supply chains under Industry 
4.0 and future research directions are discussed as well.

Paper9: Enhancing Industry 4.0 standards interoperability via knowledge graphs with natural language processing
================================================================================
Authors: Nicola Melluso, Irlan Grangel-González, Gualtiero Fantoni
=========================================
Abstract: 
==================
Industry 4.0 (I4.0) has brought several challenges related to the need to acquire and integrate large amounts of data from multiple 
sources in order to integrate these elements into an automated manufacturing system. Establishing interoperability is crucial to meet 
these challenges, and standards development and adoptions play a key role in achieving this. Therefore, academics and industrial 
stakeholders must join their forces in order to develop methods to enhance interoperability and to mitigate possible conflicts between 
standards. The aim of this paper is to propose an approach that enhances interoperability between standards through the combined use of 
Natural Language Processing (NLP) and Knowledge Graphs (KG). In particular, the proposed method is based on the measurement of semantic 
similarity among the textual content of standards documents belonging to different standardization frameworks. The present study 
contributes to the research and practice in three ways. First, it fills research gaps concerning the synergy of NLP, KGs and I4.0. 
Second, it provides an automatic method that improves the process of creating, curating and enriching a KG. Third, it provides 
qualitative and quantitative evidence of Semantic Interoperability Conflicts (SICs). The experimental results of the application of the 
proposed method to the I4.0 Standards Knowledge Graph (I40KG) show that different standards are still struggling to use a shared 
language and that there exists a strong different in the view of I4.0 proposed by the two main standardization frameworks (RAMI and 
IIRA). By automatically enriching the I40KG with a solid experimental approach, we are paving the way for actionable knowledge which 
has been extracted from the PDFs and made available in the I40KG.

Paper10: Developing an Ontology for Cyber Security Knowledge Graphs
================================================================================
Authors: Michael Iannacone, Shawn Bohn, Grant Nakamura, John Gerth, Kelly Huffer, Robert Bridges, Erik Ferragut, John Goodall
=========================================
Abstract: 
==================
In this paper we describe an ontology developed for a cyber security knowledge graph database. This is intended to provide an organized 
schema that incorporates information from a large variety of structured and unstructured data sources, and includes all relevant 
concepts within the domain. We compare the resulting ontology with previous efforts, discuss its strengths and limitations, and 
describe areas for future work.

Paper11: A review of knowledge graph application scenarios in cyber security
================================================================================
Authors: Kai Liu, Fei Wang, Zhaoyun Ding, Sheng Liang, Zhengfei Yu, Yun Zhou
=========================================
Abstract: 
==================
Facing the dynamic complex cyber environments, internal and external cyber threat intelligence, and the increasing risk of cyber-
attack, knowledge graphs show great application potential in the cyber security area because of their capabilities in knowledge 
aggregation, representation, management, and reasoning. However, while most research has focused on how to develop a complete knowledge 
graph, it remains unclear how to apply the knowledge graph to solve industrial real challenges in cyber-attack and defense scenarios. 
In this review, we provide a brief overview of the basic concepts, schema, and construction approaches for the cyber security knowledge 
graph. To facilitate future research on cyber security knowledge graphs, we also present a curatedcollection of datasets and open-
source libraries on the knowledge construction and information extraction task. In the major part of this article, we conduct a 
comparative review of the different works that elaborate on the recent progress in the application scenarios of cyber security 
knowledge graph. Furthermore, a novel comprehensive classification framework is created to describe the connected works from nine 
primary categories and eighteen subcategories. Finally, we have a thorough outlook on several promising research directions based on 
the discussion of existing research flaws.

Paper12: A Practical Approach to Constructing a Knowledge Graph for Cybersecurit
================================================================================
Authors: Yan Jia, Yulu Qi, Huaijun Shang, Rong Jiang, Aiping Li
=========================================
Abstract: 
==================
Cyberattack forms are complex and varied, and the detection and prediction of dynamic types of attack are always challenging tasks. 
Research on knowledge graphs is becoming increasingly mature in many fields. At present, it is very significant that certain scholars 
have combined the concept of the knowledge graph with cybersecurity in order to construct a cybersecurity knowledge base. This paper 
presents a cybersecurity knowledge base and deduction rules based on a quintuple model. Using machine learning, we extract entities and 
build ontology to obtain a cybersecurity knowledge base. New rules are then deduced by calculating formulas and using the path-ranking 
algorithm. The Stanford named entity recognizer (NER) is also used to train an extractor to extract useful information. Experimental 
results show that the Stanford NER provides many features and the useGazettes parameter may be used to train a recognizer in the 
cybersecurity domain in preparation for future work.

Paper13: Creating Cybersecurity Knowledge Graphs From Malware After Action Reports
================================================================================
Authors: Aritran Piplai, Sudip Mittal, Anupam Joshi, Tim Finin, James Holt, Richard Zak
=========================================
Abstract: 
==================
After Action Reports (AARs) provide incisive analysis of cyber-incidents. Extracting cyber-knowledge from these sources would provide 
security analysts with credible information, which they can use to detect or find patterns indicative of a cyber-attack. In this paper, 
we describe a system to extract information from AARs, aggregate the extracted information by fusing similar entities together, and 
represent that extracted information in a Cybersecurity Knowledge Graph (CKG). We extract entities by building a customized named 
entity recognizer called `Malware Entity Extractor' (MEE). We then build a neural network to predict how pairs of `malware entities' 
are related to each other. When we have predicted entity pairs and the relationship between them, we assert the `entity-relationship 
set' in a CKG. Our next step in the process is to fuse similar entities, to improve our CKG. This fusion helps represent intelligence 
extracted from multiple documents and reports. The fused CKG has knowledge from multiple AARs, with relationships between entities 
extracted from separate reports. As a result of this fusion, a security analyst can execute queries and retrieve better answers on the 
fused CKG, than a knowledge graph with no fusion. We also showcase various reasoning capabilities that can be leveraged by a security 
analyst using our fused CKG.

Paper14: Application of Knowledge Service in Integrated Supply Chain of Agricultural Products based on Knowledge Graph
================================================================================
Authors: Bo Yang and Yang Mengying
=========================================
Abstract: 
==================
Based on the review of the existing research, this paper summarizes the application of knowledge services in supply chain. Using 
CiteSpace software for visualization analysis, it can be found that there is a lack of cooperation between research authors and 
institutions of agricultural products integrated supply chain, but the research content is relatively relevant. "Internet+" and "fresh 
agricultural products supply chain" will be the frontier hot spots of agricultural products integrated supply chain in the future. 
Therefore, enterprises need to combine some big data technology to further integrate and optimize the agricultural product supply chain.

Paper15: Building and Using a Supply Chain Knowledge Graph applied to the rail transit industry
================================================================================
Authors: Shuo Li, Yu Zhang, Mengxing Huang, Hongwen Wu, Weihua Cai
=========================================
Abstract: 
==================
In recent years, data-driven research in specific vertical fields has gained tremendous momentum. There is a huge amount of supply 
chains data spread across the enterprise information systems and web that we can use to build knowledge graphs. For the rail transit 
industry, the knowledge graph can systematically, structure and integrate the basic facts of the rail transit field, and it is also a 
powerful tool for storing, querying, and processing big data. However, analyzing these data to build knowledge graphs is difficult due 
to the heterogeneity of the sources and scale of the amount of data. This article proposes an approach to building supply chain 
knowledge graph by exploiting semantic technologies to reconcile the data continuously crawled from diverse sources and to support 
interactive queries on the data and further assist decision-making. The graph realizes the reconstruction and storage of important 
data, and uses Neo4j to realize the visualization of the graph. Case studies on a realistic example have shown that the approach has 
major potential in building supply chain knowledge graph, therefore improving the supply chain performance of the rail transit industry.

Paper16: Applications of knowledge graphs for food science and industry
================================================================================
Authors: Weiqing Min, Chunlin Liu, Leyi Xu, Shuqiang Jiang
=========================================
Abstract: 
==================
The deployment of various networks (e.g., Internet of Things [IoT] and mobile networks), databases (e.g., nutrition tables and food 
compositional databases), and social media (e.g., Instagram and Twitter) generates huge amounts of food data, which present researchers 
with an unprecedented opportunity to study various problems and applications in food science and industry via data-driven computational 
methods. However, these multi-source heterogeneous food data appear as information silos, leading to difficulty in fully exploiting 
these food data. The knowledge graph provides a unified and standardized conceptual terminology in a structured form, and thus can 
effectively organize these food data to benefit various applications. In this review, we provide a brief introduction to knowledge 
graphs and the evolution of food knowledge organization mainly from food ontology to food knowledge graphs. We then summarize seven 
representative applications of food knowledge graphs, such as new recipe development, diet-disease correlation discovery, and 
personalized dietary recommendation. We also discuss future directions in this field, such as multimodal food knowledge graph 
construction and food knowledge graphs for human health.

Paper17: A Cybersecurity Knowledge Graph for Advanced Persistent Threat Organization Attribution
================================================================================
Authors: Yitong Ren, Yanjun Xiao, Yinghai Zhou, Zhiyong Zhang, Zhihong Tian
=========================================
Abstract: 
==================
Open-source cyber threat intelligence (OSCTI) is becoming more influential in obtaining current network security information. Most 
studies on cyber threat intelligence (CTI) focus on automating the extraction of threat entities from public sources that describe 
attack events. The cybersecurity knowledge graph aims to change the expression of threat knowledge so that security researchers can 
accurately and efﬁciently obtain various types of threat information for preliminary intelligent decisions. The attribution technology 
can not only assist security analysts in detecting advanced persistent threats, but can also identify the same threat from different 
attack events. Therefore, it is important to trace the attack threat actor. In this study, we used the knowledge graph technology, 
considered the latest research on cyber threat attack attribution, and thoroughly examined key related technologies and theories in the 
process of constructing and applying the advanced persistent threat (APT) knowledge graph from OSCTI. We designed a cybersecurity 
platform named CSKG4APT based on a knowledge graph. Inspired by the theory of ontology, we constructed CSKG4APT as an APT knowledge 
graph model based on real APT attack scenarios. We then designed an APT threat knowledge extraction algorithm for completing and 
updating the knowledge graph using deep learning and expert knowledge. Finally, we proposed a practical APT attack attribution method 
with attribution and countermeasures. CSKG4APT is not a passive defense method in traditional network confrontation but one that 
integrates a large amount of fragmented intelligence and can actively adjust its defense strategy. It lays the foundation for further 
dominance in network attack and defense.

Paper18: The SEPSES Knowledge Graph: An Integrated Resource for Cybersecurity
================================================================================
Authors: Elmar Kiesling, Andreas Ekelhart, Kabul Kurniawan, Fajar Ekaputra 
=========================================
Abstract: 
==================
This paper introduces an evolving cybersecurity knowledge graph that integrates and links critical information on real-world 
vulnerabilities, weaknesses and attack patterns from various publicly available sources. Cybersecurity constitutes a particularly 
interesting domain for the development of a domain-specific public knowledge graph, particularly due to its highly dynamic landscape 
characterized by time-critical, dispersed, and heterogeneous information. To build and continually maintain a knowledge graph, we 
provide and describe an integrated set of resources, including vocabularies derived from well-established standards in the 
cybersecurity domain, an ETL workflow that updates the knowledge graph as new information becomes available, and a set of services that 
provide integrated access through multiple interfaces. The resulting semantic resource offers comprehensive and integrated up-to-date 
instance information to security researchers and professionals alike. Furthermore, it can be easily linked to locally available 
information, as we demonstrate by means of two use cases in the context of vulnerability assessment and intrusion detection.

Paper19: Social engineering in cybersecurity: a domain ontology and knowledge graph application examples
================================================================================
Authors: Zuoguang Wang, Hongsong Zhu, Peipei Liu, Limin Sun 
=========================================
Abstract: 
==================
Social engineering has posed a serious threat to cyberspace security. To protect against social engineering attacks, a fundamental work 
is to know what constitutes social engineering. This paper first develops a domain ontology of social engineering in cybersecurity and 
conducts ontology evaluation by its knowledge graph application. The domain ontology defines 11 concepts of core entities that 
significantly constitute or affect social engineering domain, together with 22 kinds of relations describing how these entities related 
to each other. It provides a formal and explicit knowledge schema to understand, analyze, reuse and share domain knowledge of social 
engineering. Furthermore, this paper builds a knowledge graph based on 15 social engineering attack incidents and scenarios. 7 
knowledge graph application examples (in 6 analysis patterns) demonstrate that the ontology together with knowledge graph is useful to 
1) understand and analyze social engineering attack scenario and incident, 2) find the top ranked social engineering threat elements
(e.g. the most exploited human vulnerabilities and most used attack mediums), 3) find potential social engineering threats to
victims, 4) find potential targets for social engineering attackers, 5) find potential attack paths from specific attacker to specific
target, and 6) analyze the same origin attacks.

Paper20: Fraud Detection in Non-Network Knowledge Graph
================================================================================
Authors: Liu, Xinyang
=========================================
Abstract: 
==================
Fraud is becoming an increasingly severe problem in all industries, and one of the most widely-used techniques in fraud detection is 
data mining. However, most of the existing research revolve around credit card frauds, and studies on fraud detection in other fields 
are still extremely limited. Therefore, in this thesis, we develop an automated fraud detection system for both reporting and 
prediction in Contract Management, and use the contract data from Defence Construction Canada (DCC) to evaluate the approaches 
employed. As we lack practical training data, we use a weak-supervision approach to generate labels for our data and build two machine 
learning models, Logistic Regression and Random Forest. We also propose a graph-based approach that transforms our dataset into 
graphical representations, which results in a non-network knowledge graph, and learns both structural and statistical features of this 
graph to identify potential anomalies. Results from both approaches reveal relatively high recall.

Paper21: Semantic Web and Knowledge Graphs for Industry 4.0
================================================================================
Authors: Muhammad Yahya ,John G. Breslin, Muhammad Intizar Ali
=========================================
Abstract: 
==================
In recent years, due to technological advancements, the concept of Industry 4.0 (I4.0) is gaining popularity, while presenting several 
technical challenges being tackled by both the industrial and academic research communities. Semantic Web including Knowledge Graphs is 
a promising technology that can play a significant role in realizing I4.0 implementations. This paper surveys the use of the Semantic 
Web and Knowledge Graphs for I4.0 from different perspectives such as managing information related to equipment maintenance, resource 
optimization, and the provision of on-time and on-demand production and services. Moreover, to solve the challenges of limited depth 
and expressiveness in the current ontologies, we have proposed an enhanced reference generalized ontological model (RGOM) based on 
Reference Architecture Model for I4.0 (RAMI 4.0). RGOM can facilitate a range of I4.0 concepts including improved asset monitoring, 
production enhancement, reconfiguration of resources, process optimizations, product orders and deliveries, and the life cycle of 
products. Our proposed RGOM can be used to generate a knowledge graph capable of providing answers in response to any real-time query.

Paper22: KNOWLEDGE GRAPH BASED SEMANTIC MODELING FOR PROFILING IN INDUSTRY 4.0
================================================================================
Authors: Siraj Munir, Syed Imran Jami, Shaukat Wasi
=========================================
Abstract: 
==================
In this paper we present a framework for profiling of workers and employees in industry setting using the camera feeds. With the 
incorporation of Internet of Things with Big Data and Semantic Web, we provide fast communication and cooperation among humans in real-
time within the industry. It aims at supporting intelligent queries about the workers working in the Industry by using temporal 
knowledge graph generated from the multi attributed logs identified from the surveillance video. The paper facilitates integration of 
the profiling knowledge graph with existing industry knowledge graph for unified view of profiling log with worker’s information. 
Decentralized decision making in real time can be made with this system which is one of the core areas of Industry 4.0. Knowledge Graph 
is proposed as generic for reusability in any industries and enterprise for profiling purpose. The results show the highlights of the 
queries about working in the industry without the involvement of any resource. The paper is concluded with shortcomings in this work 
along with the solution

Paper23: Knowledge Representation in Modeling and Simulation: A survey for the production and logistic domain
================================================================================
Authors: Franz Georg Listl; Jan Fischer; Dagmar Beyer; Michael Weyrich
=========================================
Abstract: 
==================
Recently, ontologies and semantic data technologies have increasingly come back into the focus of research due to the emerging use of 
knowledge graphs. However, even though the modeling and simulation community has recognized the potential of using this technology for 
the modeling process, for example for automatic model generation, adaptation or to represent simulation expert knowledge, a general and 
reusable approach for the aforementioned purposes is still missing. Therefore, in this paper a state of the art review for using 
knowledge representation during modeling and simulation processes of complex technical systems is conducted, such as factories or 
process plants with specific focus on the production and logistic domain. Based on that, requirements and benefits of knowledge graphs 
in this specific domain are evaluated.

Paper24: Knowledge-Based Mining of Exceptional Patterns in Logistics Data: Approaches and Experiences in an Industry 4.0 Context
================================================================================
Authors: Eric Sternberg, Martin Atzmueller 
=========================================
Abstract: 
==================
In the context of Industry 4.0 and smart production, industrial large-scale enterprise data is applied for enabling data-driven 
analysis and modeling methods. However, the majority of the currently applied approaches consider the data in isolated fashion such 
that data from different sources, e.g., from large data warehouses are only considered independently. Furthermore, connections and 
relations between those data, i.e., relating to semantic dependencies are typically not considered, while these would open up 
integrated semantic approaches for effective data mining methods. This paper tackles these issues and demonstrates approaches and 
experiences in the context of a real-world case study in the industrial logistics domain: We propose knowledge-based data analysis 
applying subgroup discovery for identifying exceptional patterns in a semantic approach using appropriately constructed knowledge 
graphs.

Paper25: Towards knowledge graph reasoning for supply chain risk management using graph neural networks
================================================================================
Authors: Edward Elson Kosasiha ,Fabrizio Margaroli, Simone Gelli, Ajmal Aziz, Nick Wildgoose, Alexandra Brintrup
=========================================
Abstract: 
==================
Modern supply chains are complex, interconnected systems that contain emergent, invisible dependencies. Lack of visibility often 
hinders effective risk planning and results in delayed discovery of supply chain problems, with examples ranging from product 
contamination, unsustainable production practices, or exposure to suppliers clustered in geographical areas prone to natural or man-
made disasters. Initiatives that rely on manual collection of data often fail due to supply chain complexity and unwillingness of 
suppliers to share data. In this paper, we propose a neurosymbolic machine learning technique to proactively uncover hidden risks in 
supply chains and discover new information. Our method uses a combination of graph neural networks and knowledge graph reasoning. 
Unlike existing research our model is able to infer multiple types of hidden relationship risks, presenting a step change in automated 
supply chain surveillance. The approach has been tested on two empirical datasets from the automotive and energy industries, 
illustrating that it can provide inference in multiple types of links such as companies, products, production capabilities, 
certifications; thereby facilitating complex queries that go beyond who-supplies-whom. As such, additional risk insights can emerge 
from graph structure, providing practitioners with new knowledge.

Paper26: Knowgraph-TT: Knowledge-Graph-Based Transit Time Matching in Semiconductor Supply Chains
================================================================================
Authors: Ramzy Nour, Ehm Hans, Durst Sandra, Wibmer Konstanze, Bick Werner
=========================================
Abstract: 
==================
The semiconductor supply chain is characterized by a global and complex production network in a competitive market. The time when work 
at one location ends and can be resumed at another is defined as Transit Time (TT). Therefore, planning Transit Time accurately and 
minimizing delays is crucial as it is used in the execution system to determine the Available to Promise (ATP) and thus important for 
daily order confirmation. By determining the ATP, the customer receives a response to the resource availability and a due date to the 
customer requests. Due to tool inherent differences, we choose semantic integration via Knowledge Graph (KG) to match the planned TT 
used in the execution system and the actual TT measured in the monitoring tool. KnowGraph-TT thereby serves as a role model for further 
matching and alignment tasks using KG. It connects actual and planned TT, highlights the gaps via applied queries, and enables an 
optimized update of planned TT. With our solution, deviations of actual and planned TT can be minimized and confirmations of 
unrealizable deliverable times are avoided.

Paper27: KnowGraph-MDM: A Methodology for Knowledge-Graph-based Master Data Management
================================================================================
Authors: Nour Ramzy, Sandra Durst,  Martin Schreiber, Sören Auer, Javad Chamanara, Hans Ehm
=========================================
Abstract: 
==================
In highly globalized, digitized, and complex Supply Chains (SCs), the view of SCs is based on seemingly siloed or outdated data-sets. 
Integrated analysis capabilities, that rely on consistent data structures and applications, facilitate grasping, controlling, and 
ultimately enhancing SC behavior. Master Data (MD) is defined as the high-value core information of an enterprise, shared across the 
business processes and systems of an organization. Master Data Management (MDM) is an essential prerequisite for companies to make 
agile reporting and correct decisions. Traditional MDM approaches are limited in integrating enterprise information as well as meeting 
requirements, e.g., stakeholders' involvement for MD analysis and reporting. Therefore, we propose a methodology for a knowledge-graph-
based MDM, which relies on establishing a knowledge-graph (KG) layer for building a common understanding of the key business entities 
and semantic mappings from and to the original data sources. KnowGraph-MDM (KG-MDM) relies on iterations to incorporate stakeholders' 
inputs, allowing evolutionary development of the MD model. Thus, the ingestion and adoption of the new model increases among the 
stakeholders via deployment in the organization. We apply the proposed approach in a use case for a semiconductor manufacturer. The 
resulting KG depicts the core MD model that can be iteratively extended to incorporate different stakeholders' perspectives. KnowGraph-
MDM enables integrated SC performance analysis and reporting, relying on consistent MD across the SC.
