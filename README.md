# Ontology-Matching
Study: DBpedia and Wikidata

# Scenario:
DBpedia and Wikidata are Linked Open Data projects, and at first sight it seems that they are very similar, but in fact they have absolutely different approaches to deal with structured data. DBpedia extracts data from the infoboxes in Wikipedia, while Wikidata is more like Wikipedia for data—its primary source of information are users. Wikipedia itself replaces old infoboxes by Wikidata, so DBpedia could use Wikidata as a data provider and editing interface. But there is a problem of heterogeneity. Both projects use different tools and knowledge, and it leads to usage of different names for the same concepts (terminological heterogeneity). And it’s important to accurately wire up those concepts in ontologies of projects. One of the principles of Linked Data: “Include links to other URIs, so that they can discover more things.”

DBpedia: https://wiki.dbpedia.org/
Wikidata: https://www.wikidata.org/wiki/Wikidata:Main_Page

The goal of the project is to create a system that maps items and properties of Wikidata to classes and properties of DBpedia.

Here is an example for properties, that is location
 - https://www.wikidata.org/wiki/Property:P276
 - http://dbpedia.org/ontology/location

Here is an example for items and classes , that is Berlin
 - https://www.wikidata.org/wiki/Q64
 - http://dbpedia.org/page/Berlin

 
Steps to follow for Berlin:
1. Run a SPARQl Query, against DBpedia Virtuoso endpoint (https://dbpedia.org/sparql),
   to get all owl:sameAs resources and select from there, the one from Wikidata
PREFIX dbpedia:< http://dbpedia.org/resource/ >
PREFIX owl:< http://www.w3.org/2002/07/owl# >

SELECT ?obj WHERE {
    dbpedia:Berlin (owl:sameAs|^owl:sameAs)* ?obj
}
 
2. From DBpedia page extract information as:
 - rdfs:label ---> Berlin (en)
 - rdfs:comment --> Berlin (/bərˈlɪn/, German: [bɛɐ̯ˈliːn] ) is the capital and the largest city of Germany as well as one of its 16 states. With a population of approximately 3.6 million people, Berlin is the second most populous city proper and the seventh most populous urban area in the European Union. Located in northeastern Germany on the banks of Rivers Spree and Havel, it is the centre of the Berlin-Brandenburg Metropolitan Region, which has about 6 million residents from more than 180 nations. Due to its location in the European Plain, Berlin is influenced by a temperate seasonal climate. Around one-third of the city's area is composed of forests, parks, gardens, rivers and lakes. (en) 
 
3. From Wikidata page extract information as:
 - label --> Berlin 
 - aliases --> Berlin, Germany
 - description --> capital and largest city of Germany
 - To obtain the description you can also run a SPARQL Query against Wikidata endpoint(https://query.wikidata.org/)
 PREFIX wd:< http://www.wikidata.org/entity/ >
 PREFIX schema: < http://schema.org/ >

 SELECT ?o
 WHERE 
 {
  wd:Q64 schema:description ?o.
  FILTER ( lang(?o) = "en" )
 }
4. Next, for example, we get the two values for labels. First, we apply preprocessing methods. 
   The results are then used for matching methods as: 
 - Edit Distance
 - Jaccard Distance
 - Damerau-Levenshtein Edit Distance
 - We repeat this procedures for the other text and get the final outputs.

5. Final step is to write the interpretations regarding the matching between DBpedia and Wikidata.

Useful links from:
  - GSoC(Google Summer of Code) 2014: https://docs.google.com/document/d/16lAqKLAsAGQW0cp9SA0Egb1vlb6mPCcHYezVN-zB870/edit#
  - Natural Language Processing, Stanford University course: http://web.stanford.edu/class/cs224n/

