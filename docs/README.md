# SDRF Restful API

The SDRF RestFul  API allows to annotate datasets in [SDRF file format](https://github.com/bigbio/proteomics-metadata-standard/). Here, we presented the documentation of the API including all the endpoints and data structure.

## Endpoints

### GET /properties/getPropertiesFromText

This endpoint transform a text column (e.g. `characteristics[organism]` ) representation in an SDRF to an ontology-base. The GET query parameters should be provided comma-separated like:

```json
GET /properties/getPropertiesFromText?sdrf_properties=characteristics%5Borganism%5D
```
The output representation looks like:

```json
[
  {
    "freeTextColumn": "characteristics[organism]",
    "templateColumn": {
      "name": "organism",
      "ontologyTerm": {
        "id": "OBI:0100026",
        "iri_id": "http://purl.obolibrary.org/obo/OBI_0100026",
        "name": "organism",
        "ontology": "EFO"
      },
      "searchable": true,
      "typeNode": "characteristics"
    }
  }
]
```

The `TemplateColumn` object contains a set of properties that facilitate to search for values under the Ontology term:

- "name": Name of the Column
- "typeNode": The type of the Node in SDRF (e.g. characteristics, comment or None). This typeNode is the prefix for each column and represent if the property is related with the Sample or the Data file.
- "searchable": If the `searchable` is true, the values of that column can be search under the ontology term in [OLS](https://www.ebi.ac.uk/ols/index)

- Ontology Term:
   - "id": Obo accession or identifier for the ontology term in OLS
   - "iri_id": IRI accession for the ontology term in OLS
   - "name": Name of the ontology term
   - "ontology": Ontology that contains the ontology term.

### GET /properties/findValuesByProperty

This endpoint allows to search values under an specific Ontology term. For example, it allows to search taxonomies under characteristics[organism] like Homo sapiens. The endpoint has the following parameters:

- accession: IRI identifier in OLS for the pattern term to search under. For example for organism: http://purl.obolibrary.org/obo/OBI_0100026
- ontology: The ontology where the term belong to. Some terms (e.g. organism) use the same IRI identifier in different ontologies, for that reason the ontology prefix should be provided (e.g EFO)
- filter: The `keyword` to be search in the children terms.
- page: Page to be provided 0-based.
- pageSize: Number of elements or Ontology terms to be provided in the result list (default: 100)

An example result list, for the query:

```json
GET /properties/findValuesByProperty?accession=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0100026&ontology=EFO&filter=homo&pageSize=100
```

The results object list:

```json
[
  {
    "id": "NCBITaxon:9606",
    "iri_id": "http://purl.obolibrary.org/obo/NCBITaxon_9606",
    "name": "Homo sapiens",
    "ontology": "EFO"
  },
  {
    "id": "EFO:0004000",
    "iri_id": "http://www.ebi.ac.uk/efo/EFO_0004000",
    "name": "Mus musculus strain type",
    "ontology": "EFO"
  }
]
```

The result is a list of Ontology Terms.

