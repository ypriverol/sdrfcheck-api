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
