import connexion
import six

from swagger_server.models.ontology_term import OntologyTerm  # noqa: E501
from swagger_server.models.post_translational_modification import PostTranslationalModification  # noqa: E501
from swagger_server import util
from unimod.unimod import UnimodDatabase


def find_data_properties(template=None):  # noqa: E501
    """Find properties for rows of the SDRF data files

     # noqa: E501

    :param template: Status values that need to be considered for filter
    :type template: str

    :rtype: List[OntologyTerm]
    """
    return 'do some magic!'


def find_post_translational_modifications(filter=None, page=0, pageSize=100):  # noqa: E501
    """Find values for an specific property, for example possible taxonomy values for Organism property

     # noqa: E501

    :param filter: Keyword to filter the list of possible values
    :type filter: str
    :param page: Number of the page with the possible values for the property
    :type page: int
    :param pageSize: Number of values with the possible values for the property
    :type pageSize: int

    :rtype: List[PostTranslationalModification]
    """

    unimod_database = UnimodDatabase()
    print(unimod_database)
    l = unimod_database.modifications
    list = l[(page*pageSize):(page*pageSize)+pageSize]
    return list


def find_sample_properties(template=None):  # noqa: E501
    """Find properties for rows of the SDRF samples

     # noqa: E501

    :param template: Status values that need to be considered for filter
    :type template: str

    :rtype: List[OntologyTerm]
    """
    return 'do some magic!'


def find_values_by_property(accesssion, ontology, filter=None, page=None, pageSize=None):  # noqa: E501
    """Find values for an specific property, for example possible taxonomy values for Organism property

     # noqa: E501

    :param accesssion: Accession of the property in the Ontology
    :type accesssion: str
    :param ontology: Ontology to loockup the property
    :type ontology: str
    :param filter: Keyword to filter the list of possible values
    :type filter: str
    :param page: Number of the page with the possible values for the property
    :type page: int
    :param pageSize: Number of values with the possible values for the property
    :type pageSize: int

    :rtype: List[OntologyTerm]
    """
    return 'do some magic!'
