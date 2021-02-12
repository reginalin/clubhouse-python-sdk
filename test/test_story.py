"""
    Clubhouse API

    Clubhouse API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import clubhouse_python_sdk
from clubhouse_python_sdk.model.branch import Branch
from clubhouse_python_sdk.model.comment import Comment
from clubhouse_python_sdk.model.commit import Commit
from clubhouse_python_sdk.model.external_ticket import ExternalTicket
from clubhouse_python_sdk.model.file import File
from clubhouse_python_sdk.model.label import Label
from clubhouse_python_sdk.model.linked_file import LinkedFile
from clubhouse_python_sdk.model.pull_request import PullRequest
from clubhouse_python_sdk.model.story_stats import StoryStats
from clubhouse_python_sdk.model.support_ticket import SupportTicket
from clubhouse_python_sdk.model.task import Task
from clubhouse_python_sdk.model.typed_story_link import TypedStoryLink
globals()['Branch'] = Branch
globals()['Comment'] = Comment
globals()['Commit'] = Commit
globals()['ExternalTicket'] = ExternalTicket
globals()['File'] = File
globals()['Label'] = Label
globals()['LinkedFile'] = LinkedFile
globals()['PullRequest'] = PullRequest
globals()['StoryStats'] = StoryStats
globals()['SupportTicket'] = SupportTicket
globals()['Task'] = Task
globals()['TypedStoryLink'] = TypedStoryLink
from clubhouse_python_sdk.model.story import Story


class TestStory(unittest.TestCase):
    """Story unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStory(self):
        """Test Story"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Story()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
