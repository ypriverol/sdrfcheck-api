# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.ontology_term import OntologyTerm  # noqa: E501
from swagger_server.models.post_translational_modification import PostTranslationalModification  # noqa: E501
from swagger_server.test import BaseTestCase


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
        query_string = [('accesssion', 'accesssion_example'),
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


if __name__ == '__main__':
    import unittest
    unittest.main()
