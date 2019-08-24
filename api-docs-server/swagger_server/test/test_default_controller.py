# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_retrive_voice_note_downloadable_url(self):
        """Test case for get_retrive_voice_note_downloadable_url

        Get downloadable link of voice note by pilot id and voice note id
        """
        response = self.client.open(
            '/api/v1/pilots/{pilot_id}/voicenotes/{voice_note_id}'.format(pilot_id=56, voice_note_id='voice_note_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_retrive_voice_notes_for_specific_pilot(self):
        """Test case for get_retrive_voice_notes_for_specific_pilot

        Retrieve voice notes which are uploaded by specific pilot
        """
        response = self.client.open(
            '/api/v1/pilots/{pilot_id}/voicenotes'.format(pilot_id=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_sending_new_voice_note(self):
        """Test case for post_sending_new_voice_note

        Upload new voice note
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/v1/pilots/{pilot_id}/voicenotes'.format(pilot_id=56),
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
