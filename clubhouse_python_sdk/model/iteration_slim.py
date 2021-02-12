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
    from clubhouse_python_sdk.model.iteration_stats import IterationStats
    from clubhouse_python_sdk.model.label import Label
    globals()['IterationStats'] = IterationStats
    globals()['Label'] = Label


class IterationSlim(ModelNormal):
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
            'created_at': (datetime,),  # noqa: E501
            'end_date': (datetime,),  # noqa: E501
            'entity_type': (str,),  # noqa: E501
            'follower_ids': ([str],),  # noqa: E501
            'group_ids': ([str],),  # noqa: E501
            'group_mention_ids': ([str],),  # noqa: E501
            'id': (int,),  # noqa: E501
            'labels': ([Label],),  # noqa: E501
            'member_mention_ids': ([str],),  # noqa: E501
            'mention_ids': ([str],),  # noqa: E501
            'name': (str,),  # noqa: E501
            'start_date': (datetime,),  # noqa: E501
            'stats': (IterationStats,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'app_url': 'app_url',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'end_date': 'end_date',  # noqa: E501
        'entity_type': 'entity_type',  # noqa: E501
        'follower_ids': 'follower_ids',  # noqa: E501
        'group_ids': 'group_ids',  # noqa: E501
        'group_mention_ids': 'group_mention_ids',  # noqa: E501
        'id': 'id',  # noqa: E501
        'labels': 'labels',  # noqa: E501
        'member_mention_ids': 'member_mention_ids',  # noqa: E501
        'mention_ids': 'mention_ids',  # noqa: E501
        'name': 'name',  # noqa: E501
        'start_date': 'start_date',  # noqa: E501
        'stats': 'stats',  # noqa: E501
        'status': 'status',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
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
    def __init__(self, app_url, created_at, end_date, entity_type, follower_ids, group_ids, group_mention_ids, id, labels, member_mention_ids, mention_ids, name, start_date, stats, status, updated_at, *args, **kwargs):  # noqa: E501
        """IterationSlim - a model defined in OpenAPI

        Args:
            app_url (str): The Clubhouse application url for the Iteration.
            created_at (datetime): The instant when this iteration was created.
            end_date (datetime): The date this iteration begins.
            entity_type (str): A string description of this resource
            follower_ids ([str]): An array of UUIDs for any Members listed as Followers.
            group_ids ([str]): An array of UUIDs for any Groups you want to add as Followers. Currently, only one Group association is presented in our web UI.
            group_mention_ids ([str]): An array of Group IDs that have been mentioned in the Story description.
            id (int): The ID of the iteration.
            labels ([Label]): An array of labels attached to the iteration.
            member_mention_ids ([str]): An array of Member IDs that have been mentioned in the Story description.
            mention_ids ([str]): Deprecated: use member_mention_ids.
            name (str): The name of the iteration.
            start_date (datetime): The date this iteration begins.
            stats (IterationStats):
            status (str): The status of the iteration. Values are either \"unstarted\", \"started\", or \"done\".
            updated_at (datetime): The instant when this iteration was last updated.

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
        self.created_at = created_at
        self.end_date = end_date
        self.entity_type = entity_type
        self.follower_ids = follower_ids
        self.group_ids = group_ids
        self.group_mention_ids = group_mention_ids
        self.id = id
        self.labels = labels
        self.member_mention_ids = member_mention_ids
        self.mention_ids = mention_ids
        self.name = name
        self.start_date = start_date
        self.stats = stats
        self.status = status
        self.updated_at = updated_at
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
