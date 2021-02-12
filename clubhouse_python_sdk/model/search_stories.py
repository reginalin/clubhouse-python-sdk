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


class SearchStories(ModelNormal):
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
        ('story_type',): {
            'BUG': "bug",
            'CHORE': "chore",
            'FEATURE': "feature",
        },
        ('workflow_state_types',): {
            'DONE': "done",
            'STARTED': "started",
            'UNSTARTED': "unstarted",
        },
    }

    validations = {
        ('epic_ids',): {
        },
        ('group_ids',): {
        },
        ('iteration_ids',): {
        },
        ('label_ids',): {
        },
        ('owner_ids',): {
        },
        ('project_ids',): {
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'archived': (bool,),  # noqa: E501
            'completed_at_end': (datetime,),  # noqa: E501
            'completed_at_start': (datetime,),  # noqa: E501
            'created_at_end': (datetime,),  # noqa: E501
            'created_at_start': (datetime,),  # noqa: E501
            'deadline_end': (datetime,),  # noqa: E501
            'deadline_start': (datetime,),  # noqa: E501
            'epic_id': (int, none_type,),  # noqa: E501
            'epic_ids': ([int],),  # noqa: E501
            'estimate': (int,),  # noqa: E501
            'external_id': (str,),  # noqa: E501
            'group_id': (str, none_type,),  # noqa: E501
            'group_ids': ([str],),  # noqa: E501
            'includes_description': (bool,),  # noqa: E501
            'iteration_id': (int, none_type,),  # noqa: E501
            'iteration_ids': ([int],),  # noqa: E501
            'label_ids': ([int],),  # noqa: E501
            'label_name': (str,),  # noqa: E501
            'owner_id': (str, none_type,),  # noqa: E501
            'owner_ids': ([str],),  # noqa: E501
            'project_id': (int,),  # noqa: E501
            'project_ids': ([int],),  # noqa: E501
            'requested_by_id': (str,),  # noqa: E501
            'story_type': (str,),  # noqa: E501
            'updated_at_end': (datetime,),  # noqa: E501
            'updated_at_start': (datetime,),  # noqa: E501
            'workflow_state_id': (int,),  # noqa: E501
            'workflow_state_types': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'archived': 'archived',  # noqa: E501
        'completed_at_end': 'completed_at_end',  # noqa: E501
        'completed_at_start': 'completed_at_start',  # noqa: E501
        'created_at_end': 'created_at_end',  # noqa: E501
        'created_at_start': 'created_at_start',  # noqa: E501
        'deadline_end': 'deadline_end',  # noqa: E501
        'deadline_start': 'deadline_start',  # noqa: E501
        'epic_id': 'epic_id',  # noqa: E501
        'epic_ids': 'epic_ids',  # noqa: E501
        'estimate': 'estimate',  # noqa: E501
        'external_id': 'external_id',  # noqa: E501
        'group_id': 'group_id',  # noqa: E501
        'group_ids': 'group_ids',  # noqa: E501
        'includes_description': 'includes_description',  # noqa: E501
        'iteration_id': 'iteration_id',  # noqa: E501
        'iteration_ids': 'iteration_ids',  # noqa: E501
        'label_ids': 'label_ids',  # noqa: E501
        'label_name': 'label_name',  # noqa: E501
        'owner_id': 'owner_id',  # noqa: E501
        'owner_ids': 'owner_ids',  # noqa: E501
        'project_id': 'project_id',  # noqa: E501
        'project_ids': 'project_ids',  # noqa: E501
        'requested_by_id': 'requested_by_id',  # noqa: E501
        'story_type': 'story_type',  # noqa: E501
        'updated_at_end': 'updated_at_end',  # noqa: E501
        'updated_at_start': 'updated_at_start',  # noqa: E501
        'workflow_state_id': 'workflow_state_id',  # noqa: E501
        'workflow_state_types': 'workflow_state_types',  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SearchStories - a model defined in OpenAPI

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
            archived (bool): A true/false boolean indicating whether the Story is in archived state.. [optional]  # noqa: E501
            completed_at_end (datetime): Stories should have been completed before this date.. [optional]  # noqa: E501
            completed_at_start (datetime): Stories should have been competed after this date.. [optional]  # noqa: E501
            created_at_end (datetime): Stories should have been created before this date.. [optional]  # noqa: E501
            created_at_start (datetime): Stories should have been created after this date.. [optional]  # noqa: E501
            deadline_end (datetime): Stories should have a deadline before this date.. [optional]  # noqa: E501
            deadline_start (datetime): Stories should have a deadline after this date.. [optional]  # noqa: E501
            epic_id (int, none_type): The Epic IDs that may be associated with the Stories.. [optional]  # noqa: E501
            epic_ids ([int]): The Epic IDs that may be associated with the Stories.. [optional]  # noqa: E501
            estimate (int): The number of estimate points associate with the Stories.. [optional]  # noqa: E501
            external_id (str): An ID or URL that references an external resource. Useful during imports.. [optional]  # noqa: E501
            group_id (str, none_type): The Group ID that is associated with the Stories. [optional]  # noqa: E501
            group_ids ([str]): The Group IDs that are associated with the Stories. [optional]  # noqa: E501
            includes_description (bool): Whether to include the story description in the response.. [optional]  # noqa: E501
            iteration_id (int, none_type): The Iteration ID that may be associated with the Stories.. [optional]  # noqa: E501
            iteration_ids ([int]): The Iteration IDs that may be associated with the Stories.. [optional]  # noqa: E501
            label_ids ([int]): The Label IDs that may be associated with the Stories.. [optional]  # noqa: E501
            label_name (str): The name of any associated Labels.. [optional]  # noqa: E501
            owner_id (str, none_type): An array of UUIDs for any Users who may be Owners of the Stories.. [optional]  # noqa: E501
            owner_ids ([str]): An array of UUIDs for any Users who may be Owners of the Stories.. [optional]  # noqa: E501
            project_id (int): The IDs for the Projects the Stories may be assigned to.. [optional]  # noqa: E501
            project_ids ([int]): The IDs for the Projects the Stories may be assigned to.. [optional]  # noqa: E501
            requested_by_id (str): The UUID of any Users who may have requested the Stories.. [optional]  # noqa: E501
            story_type (str): The type of Stories that you want returned.. [optional]  # noqa: E501
            updated_at_end (datetime): Stories should have been updated before this date.. [optional]  # noqa: E501
            updated_at_start (datetime): Stories should have been updated after this date.. [optional]  # noqa: E501
            workflow_state_id (int): The unique IDs of the specific Workflow States that the Stories should be in.. [optional]  # noqa: E501
            workflow_state_types ([str]): The type of Workflow State the Stories may be in.. [optional]  # noqa: E501
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

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
