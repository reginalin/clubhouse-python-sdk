"""
    Clubhouse API

    Clubhouse API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import clubhouse_python_sdk
from clubhouse_python_sdk.model.external_ticket import ExternalTicket
from clubhouse_python_sdk.model.file import File
from clubhouse_python_sdk.model.label import Label
from clubhouse_python_sdk.model.linked_file import LinkedFile
from clubhouse_python_sdk.model.story_contents_task import StoryContentsTask
globals()['ExternalTicket'] = ExternalTicket
globals()['File'] = File
globals()['Label'] = Label
globals()['LinkedFile'] = LinkedFile
globals()['StoryContentsTask'] = StoryContentsTask
from clubhouse_python_sdk.model.story_contents import StoryContents


class TestStoryContents(unittest.TestCase):
    """StoryContents unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStoryContents(self):
        """Test StoryContents"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StoryContents()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()