import connexion
import six

from swagger_server import util


def get_retrive_voice_note_downloadable_url(pilot_id, voice_note_id):  # noqa: E501
    """Get downloadable link of voice note by pilot id and voice note id

     # noqa: E501

    :param pilot_id: Pilot id
    :type pilot_id: int
    :param voice_note_id: voice note id
    :type voice_note_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_retrive_voice_notes_for_specific_pilot(pilot_id):  # noqa: E501
    """Retrieve voice notes which are uploaded by specific pilot

     # noqa: E501

    :param pilot_id: Pilot id
    :type pilot_id: int

    :rtype: None
    """
    return 'do some magic!'


def post_sending_new_voice_note(pilot_id, file):  # noqa: E501
    """Upload new voice note

     # noqa: E501

    :param pilot_id: Pilot id
    :type pilot_id: int
    :param file: The voice note to upload.
    :type file: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'
