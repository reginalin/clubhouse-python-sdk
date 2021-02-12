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
    from clubhouse_python_sdk.model.epic_stats import EpicStats
    from clubhouse_python_sdk.model.external_ticket import ExternalTicket
    from clubhouse_python_sdk.model.label import Label
    from clubhouse_python_sdk.model.support_ticket import SupportTicket
    globals()['EpicStats'] = EpicStats
    globals()['ExternalTicket'] = ExternalTicket
    globals()['Label'] = Label
    globals()['SupportTicket'] = SupportTicket


class EpicSlim(ModelNormal):
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
            'completed': (bool,),  # noqa: E501
            'completed_at': (datetime, none_type,),  # noqa: E501
            'completed_at_override': (datetime, none_type,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'deadline': (datetime, none_type,),  # noqa: E501
            'entity_type': (str,),  # noqa: E501
            'epic_state_id': (int,),  # noqa: E501
            'external_id': (str, none_type,),  # noqa: E501
            'external_tickets': ([ExternalTicket],),  # noqa: E501
            'follower_ids': ([str],),  # noqa: E501
            'group_id': (str, none_type,),  # noqa: E501
            'group_mention_ids': ([str],),  # noqa: E501
            'id': (int,),  # noqa: E501
            'labels': ([Label],),  # noqa: E501
            'member_mention_ids': ([str],),  # noqa: E501
            'mention_ids': ([str],),  # noqa: E501
            'milestone_id': (int, none_type,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'owner_ids': ([str],),  # noqa: E501
            'planned_start_date': (datetime, none_type,),  # noqa: E501
            'position': (int,),  # noqa: E501
            'project_ids': ([int],),  # noqa: E501
            'requested_by_id': (str,),  # noqa: E501
            'started': (bool,),  # noqa: E501
            'started_at': (datetime, none_type,),  # noqa: E501
            'started_at_override': (datetime, none_type,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'stats': (EpicStats,),  # noqa: E501
            'support_tickets': ([SupportTicket],),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'description': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'app_url': 'app_url',  # noqa: E501
        'archived': 'archived',  # noqa: E501
        'completed': 'completed',  # noqa: E501
        'completed_at': 'completed_at',  # noqa: E501
        'completed_at_override': 'completed_at_override',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'deadline': 'deadline',  # noqa: E501
        'entity_type': 'entity_type',  # noqa: E501
        'epic_state_id': 'epic_state_id',  # noqa: E501
        'external_id': 'external_id',  # noqa: E501
        'external_tickets': 'external_tickets',  # noqa: E501
        'follower_ids': 'follower_ids',  # noqa: E501
        'group_id': 'group_id',  # noqa: E501
        'group_mention_ids': 'group_mention_ids',  # noqa: E501
        'id': 'id',  # noqa: E501
        'labels': 'labels',  # noqa: E501
        'member_mention_ids': 'member_mention_ids',  # noqa: E501
        'mention_ids': 'mention_ids',  # noqa: E501
        'milestone_id': 'milestone_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'owner_ids': 'owner_ids',  # noqa: E501
        'planned_start_date': 'planned_start_date',  # noqa: E501
        'position': 'position',  # noqa: E501
        'project_ids': 'project_ids',  # noqa: E501
        'requested_by_id': 'requested_by_id',  # noqa: E501
        'started': 'started',  # noqa: E501
        'started_at': 'started_at',  # noqa: E501
        'started_at_override': 'started_at_override',  # noqa: E501
        'state': 'state',  # noqa: E501
        'stats': 'stats',  # noqa: E501
        'support_tickets': 'support_tickets',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'description': 'description',  # noqa: E501
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
    def __init__(self, app_url, archived, completed, completed_at, completed_at_override, created_at, deadline, entity_type, epic_state_id, external_id, external_tickets, follower_ids, group_id, group_mention_ids, id, labels, member_mention_ids, mention_ids, milestone_id, name, owner_ids, planned_start_date, position, project_ids, requested_by_id, started, started_at, started_at_override, state, stats, support_tickets, updated_at, *args, **kwargs):  # noqa: E501
        """EpicSlim - a model defined in OpenAPI

        Args:
            app_url (str): The Clubhouse application url for the Epic.
            archived (bool): True/false boolean that indicates whether the Epic is archived or not.
            completed (bool): A true/false boolean indicating if the Epic has been completed.
            completed_at (datetime, none_type): The time/date the Epic was completed.
            completed_at_override (datetime, none_type): A manual override for the time/date the Epic was completed.
            created_at (datetime, none_type): The time/date the Epic was created.
            deadline (datetime, none_type): The Epic's deadline.
            entity_type (str): A string description of this resource.
            epic_state_id (int): The ID of the Epic State.
            external_id (str, none_type): This field can be set to another unique ID. In the case that the Epic has been imported from another tool, the ID in the other tool can be indicated here.
            external_tickets ([ExternalTicket]):
            follower_ids ([str]): An array of UUIDs for any Members you want to add as Followers on this Epic.
            group_id (str, none_type):
            group_mention_ids ([str]): An array of Group IDs that have been mentioned in the Epic description.
            id (int): The unique ID of the Epic.
            labels ([Label]): An array of Labels attached to the Epic.
            member_mention_ids ([str]): An array of Member IDs that have been mentioned in the Epic description.
            mention_ids ([str]): Deprecated: use member_mention_ids.
            milestone_id (int, none_type): The ID of the Milestone this Epic is related to.
            name (str): The name of the Epic.
            owner_ids ([str]): An array of UUIDs for any members you want to add as Owners on this new Epic.
            planned_start_date (datetime, none_type): The Epic's planned start date.
            position (int): The Epic's relative position in the Epic workflow state.
            project_ids ([int]): The IDs of Projects related to this Epic.
            requested_by_id (str): The ID of the Member that requested the epic.
            started (bool): A true/false boolean indicating if the Epic has been started.
            started_at (datetime, none_type): The time/date the Epic was started.
            started_at_override (datetime, none_type): A manual override for the time/date the Epic was started.
            state (str): `Deprecated` The workflow state that the Epic is in.
            stats (EpicStats):
            support_tickets ([SupportTicket]):
            updated_at (datetime, none_type): The time/date the Epic was updated.

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
            description (str): The Epic's description.. [optional]  # noqa: E501
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
        self.completed = completed
        self.completed_at = completed_at
        self.completed_at_override = completed_at_override
        self.created_at = created_at
        self.deadline = deadline
        self.entity_type = entity_type
        self.epic_state_id = epic_state_id
        self.external_id = external_id
        self.external_tickets = external_tickets
        self.follower_ids = follower_ids
        self.group_id = group_id
        self.group_mention_ids = group_mention_ids
        self.id = id
        self.labels = labels
        self.member_mention_ids = member_mention_ids
        self.mention_ids = mention_ids
        self.milestone_id = milestone_id
        self.name = name
        self.owner_ids = owner_ids
        self.planned_start_date = planned_start_date
        self.position = position
        self.project_ids = project_ids
        self.requested_by_id = requested_by_id
        self.started = started
        self.started_at = started_at
        self.started_at_override = started_at_override
        self.state = state
        self.stats = stats
        self.support_tickets = support_tickets
        self.updated_at = updated_at
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
