"""
    Clubhouse API

    Clubhouse API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from clubhouse_python_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
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


class Story(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'app_url': (str,),  # noqa: E501
            'archived': (bool,),  # noqa: E501
            'blocked': (bool,),  # noqa: E501
            'blocker': (bool,),  # noqa: E501
            'branches': ([Branch],),  # noqa: E501
            'comments': ([Comment],),  # noqa: E501
            'commits': ([Commit],),  # noqa: E501
            'completed': (bool,),  # noqa: E501
            'completed_at': (datetime, none_type,),  # noqa: E501
            'completed_at_override': (datetime, none_type,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'deadline': (datetime, none_type,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'entity_type': (str,),  # noqa: E501
            'epic_id': (int, none_type,),  # noqa: E501
            'estimate': (int, none_type,),  # noqa: E501
            'external_id': (str, none_type,),  # noqa: E501
            'external_links': ([str],),  # noqa: E501
            'external_tickets': ([ExternalTicket],),  # noqa: E501
            'files': ([File],),  # noqa: E501
            'follower_ids': ([str],),  # noqa: E501
            'group_id': (str, none_type,),  # noqa: E501
            'group_mention_ids': ([str],),  # noqa: E501
            'id': (int,),  # noqa: E501
            'iteration_id': (int, none_type,),  # noqa: E501
            'labels': ([Label],),  # noqa: E501
            'linked_files': ([LinkedFile],),  # noqa: E501
            'member_mention_ids': ([str],),  # noqa: E501
            'mention_ids': ([str],),  # noqa: E501
            'moved_at': (datetime, none_type,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'owner_ids': ([str],),  # noqa: E501
            'position': (int,),  # noqa: E501
            'previous_iteration_ids': ([int],),  # noqa: E501
            'project_id': (int,),  # noqa: E501
            'pull_requests': ([PullRequest],),  # noqa: E501
            'requested_by_id': (str,),  # noqa: E501
            'started': (bool,),  # noqa: E501
            'started_at': (datetime, none_type,),  # noqa: E501
            'started_at_override': (datetime, none_type,),  # noqa: E501
            'stats': (StoryStats,),  # noqa: E501
            'story_links': ([TypedStoryLink],),  # noqa: E501
            'story_type': (str,),  # noqa: E501
            'support_tickets': ([SupportTicket],),  # noqa: E501
            'tasks': ([Task],),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'workflow_state_id': (int,),  # noqa: E501
            'cycle_time': (int,),  # noqa: E501
            'lead_time': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'app_url': 'app_url',  # noqa: E501
        'archived': 'archived',  # noqa: E501
        'blocked': 'blocked',  # noqa: E501
        'blocker': 'blocker',  # noqa: E501
        'branches': 'branches',  # noqa: E501
        'comments': 'comments',  # noqa: E501
        'commits': 'commits',  # noqa: E501
        'completed': 'completed',  # noqa: E501
        'completed_at': 'completed_at',  # noqa: E501
        'completed_at_override': 'completed_at_override',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'deadline': 'deadline',  # noqa: E501
        'description': 'description',  # noqa: E501
        'entity_type': 'entity_type',  # noqa: E501
        'epic_id': 'epic_id',  # noqa: E501
        'estimate': 'estimate',  # noqa: E501
        'external_id': 'external_id',  # noqa: E501
        'external_links': 'external_links',  # noqa: E501
        'external_tickets': 'external_tickets',  # noqa: E501
        'files': 'files',  # noqa: E501
        'follower_ids': 'follower_ids',  # noqa: E501
        'group_id': 'group_id',  # noqa: E501
        'group_mention_ids': 'group_mention_ids',  # noqa: E501
        'id': 'id',  # noqa: E501
        'iteration_id': 'iteration_id',  # noqa: E501
        'labels': 'labels',  # noqa: E501
        'linked_files': 'linked_files',  # noqa: E501
        'member_mention_ids': 'member_mention_ids',  # noqa: E501
        'mention_ids': 'mention_ids',  # noqa: E501
        'moved_at': 'moved_at',  # noqa: E501
        'name': 'name',  # noqa: E501
        'owner_ids': 'owner_ids',  # noqa: E501
        'position': 'position',  # noqa: E501
        'previous_iteration_ids': 'previous_iteration_ids',  # noqa: E501
        'project_id': 'project_id',  # noqa: E501
        'pull_requests': 'pull_requests',  # noqa: E501
        'requested_by_id': 'requested_by_id',  # noqa: E501
        'started': 'started',  # noqa: E501
        'started_at': 'started_at',  # noqa: E501
        'started_at_override': 'started_at_override',  # noqa: E501
        'stats': 'stats',  # noqa: E501
        'story_links': 'story_links',  # noqa: E501
        'story_type': 'story_type',  # noqa: E501
        'support_tickets': 'support_tickets',  # noqa: E501
        'tasks': 'tasks',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'workflow_state_id': 'workflow_state_id',  # noqa: E501
        'cycle_time': 'cycle_time',  # noqa: E501
        'lead_time': 'lead_time',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, app_url, archived, blocked, blocker, branches, comments, commits, completed, completed_at, completed_at_override, created_at, deadline, description, entity_type, epic_id, estimate, external_id, external_links, external_tickets, files, follower_ids, group_id, group_mention_ids, id, iteration_id, labels, linked_files, member_mention_ids, mention_ids, moved_at, name, owner_ids, position, previous_iteration_ids, project_id, pull_requests, requested_by_id, started, started_at, started_at_override, stats, story_links, story_type, support_tickets, tasks, updated_at, workflow_state_id, *args, **kwargs):  # noqa: E501
        """Story - a model defined in OpenAPI

        Args:
            app_url (str): The Clubhouse application url for the Story.
            archived (bool): True if the story has been archived or not.
            blocked (bool): A true/false boolean indicating if the Story is currently blocked.
            blocker (bool): A true/false boolean indicating if the Story is currently a blocker of another story.
            branches ([Branch]): An array of Git branches attached to the story.
            comments ([Comment]): An array of comments attached to the story.
            commits ([Commit]): An array of commits attached to the story.
            completed (bool): A true/false boolean indicating if the Story has been completed.
            completed_at (datetime, none_type): The time/date the Story was completed.
            completed_at_override (datetime, none_type): A manual override for the time/date the Story was completed.
            created_at (datetime): The time/date the Story was created.
            deadline (datetime, none_type): The due date of the story.
            description (str): The description of the story.
            entity_type (str): A string description of this resource.
            epic_id (int, none_type): The ID of the epic the story belongs to.
            estimate (int, none_type): The numeric point estimate of the story. Can also be null, which means unestimated.
            external_id (str, none_type): This field can be set to another unique ID. In the case that the Story has been imported from another tool, the ID in the other tool can be indicated here.
            external_links ([str]): An array of external link (strings) associated with a Story
            external_tickets ([ExternalTicket]): An array of External Tickets associated with a Story
            files ([File]): An array of files attached to the story.
            follower_ids ([str]): An array of UUIDs for any Members listed as Followers.
            group_id (str, none_type): The ID of the group associated with the story.
            group_mention_ids ([str]): An array of Group IDs that have been mentioned in the Story description.
            id (int): The unique ID of the Story.
            iteration_id (int, none_type): The ID of the iteration the story belongs to.
            labels ([Label]): An array of labels attached to the story.
            linked_files ([LinkedFile]): An array of linked files attached to the story.
            member_mention_ids ([str]): An array of Member IDs that have been mentioned in the Story description.
            mention_ids ([str]): Deprecated: use member_mention_ids.
            moved_at (datetime, none_type): The time/date the Story was last changed workflow-state.
            name (str): The name of the story.
            owner_ids ([str]): An array of UUIDs of the owners of this story.
            position (int): A number representing the position of the story in relation to every other story in the current project.
            previous_iteration_ids ([int]): The IDs of the iteration the story belongs to.
            project_id (int): The ID of the project the story belongs to.
            pull_requests ([PullRequest]): An array of Pull/Merge Requests attached to the story.
            requested_by_id (str): The ID of the Member that requested the story.
            started (bool): A true/false boolean indicating if the Story has been started.
            started_at (datetime, none_type): The time/date the Story was started.
            started_at_override (datetime, none_type): A manual override for the time/date the Story was started.
            stats (StoryStats):
            story_links ([TypedStoryLink]): An array of story links attached to the Story.
            story_type (str): The type of story (feature, bug, chore).
            support_tickets ([SupportTicket]):
            tasks ([Task]): An array of tasks connected to the story.
            updated_at (datetime, none_type): The time/date the Story was updated.
            workflow_state_id (int): The ID of the workflow state the story is currently in.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            cycle_time (int): The cycle time (in seconds) of this story when complete.. [optional]  # noqa: E501
            lead_time (int): The lead time (in seconds) of this story when complete.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.app_url = app_url
        self.archived = archived
        self.blocked = blocked
        self.blocker = blocker
        self.branches = branches
        self.comments = comments
        self.commits = commits
        self.completed = completed
        self.completed_at = completed_at
        self.completed_at_override = completed_at_override
        self.created_at = created_at
        self.deadline = deadline
        self.description = description
        self.entity_type = entity_type
        self.epic_id = epic_id
        self.estimate = estimate
        self.external_id = external_id
        self.external_links = external_links
        self.external_tickets = external_tickets
        self.files = files
        self.follower_ids = follower_ids
        self.group_id = group_id
        self.group_mention_ids = group_mention_ids
        self.id = id
        self.iteration_id = iteration_id
        self.labels = labels
        self.linked_files = linked_files
        self.member_mention_ids = member_mention_ids
        self.mention_ids = mention_ids
        self.moved_at = moved_at
        self.name = name
        self.owner_ids = owner_ids
        self.position = position
        self.previous_iteration_ids = previous_iteration_ids
        self.project_id = project_id
        self.pull_requests = pull_requests
        self.requested_by_id = requested_by_id
        self.started = started
        self.started_at = started_at
        self.started_at_override = started_at_override
        self.stats = stats
        self.story_links = story_links
        self.story_type = story_type
        self.support_tickets = support_tickets
        self.tasks = tasks
        self.updated_at = updated_at
        self.workflow_state_id = workflow_state_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
