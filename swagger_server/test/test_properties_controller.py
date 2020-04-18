# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from models.map_template_column import MapTemplateColumn  # noqa: E501
from models.ontology_term import OntologyTerm  # noqa: E501
from models.post_translational_modification import PostTranslationalModification  # noqa: E501
from models.template import Template  # noqa: E501
from models.template_column import TemplateColumn  # noqa: E501
from test import BaseTestCase


class TestPropertiesController(BaseTestCase):
    """PropertiesController integration test stubs"""

    def test_find_data_properties(self):
        """Test case for find_data_properties

        Find properties for rows of the SDRF data files
        """
        query_string = [('template', 'template_example')]
        response = self.client.open(
            '/v2/properties/findDataProperties',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_post_translational_modifications(self):
        """Test case for find_post_translational_modifications

        Find values for an specific property, for example possible taxonomy values for Organism property
        """
        query_string = [('filter', 'filter_example'),
                        ('page', 0),
                        ('pageSize', 100)]
        response = self.client.open(
            '/v2/complexproperties/findPostTranslationalModifications',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_sample_properties(self):
        """Test case for find_sample_properties

        Find properties for rows of the SDRF samples
        """
        query_string = [('template', 'template_example')]
        response = self.client.open(
            '/v2/properties/findSampleProperties',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_values_by_property(self):
        """Test case for find_values_by_property

        Find values for an specific property, for example possible taxonomy values for Organism property
        """
        query_string = [('accession', 'accession_example'),
                        ('ontology', 'ontology_example'),
                        ('filter', 'filter_example'),
                        ('page', 0),
                        ('pageSize', 100)]
        response = self.client.open(
            '/v2/properties/findValuesByProperty',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_properties_from_text(self):
        """Test case for get_properties_from_text

        Get the templates for Sample metadata and Data files
        """
        query_string = [('sdrfProperties', 'sdrfProperties_example')]
        response = self.client.open(
            '/v2/properties/getPropertiesFromText',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_templates(self):
        """Test case for get_templates

        Get the templates for Sample metadata and Data files
        """
        response = self.client.open(
            '/v2/properties/getTemplates',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
