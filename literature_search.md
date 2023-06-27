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


