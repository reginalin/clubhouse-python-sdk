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
    from clubhouse_python_sdk.model.pull_request_label import PullRequestLabel
    globals()['PullRequestLabel'] = PullRequestLabel


class PullRequest(ModelNormal):
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
            'branch_id': (int,),  # noqa: E501
            'branch_name': (str,),  # noqa: E501
            'closed': (bool,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'draft': (bool,),  # noqa: E501
            'entity_type': (str,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'num_added': (int,),  # noqa: E501
            'num_commits': (int, none_type,),  # noqa: E501
            'num_modified': (int, none_type,),  # noqa: E501
            'num_removed': (int,),  # noqa: E501
            'number': (int,),  # noqa: E501
            'target_branch_id': (int,),  # noqa: E501
            'target_branch_name': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'build_status': (str,),  # noqa: E501
            'review_status': (str,),  # noqa: E501
            'vcs_labels': ([PullRequestLabel], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'branch_id': 'branch_id',  # noqa: E501
        'branch_name': 'branch_name',  # noqa: E501
        'closed': 'closed',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'draft': 'draft',  # noqa: E501
        'entity_type': 'entity_type',  # noqa: E501
        'id': 'id',  # noqa: E501
        'num_added': 'num_added',  # noqa: E501
        'num_commits': 'num_commits',  # noqa: E501
        'num_modified': 'num_modified',  # noqa: E501
        'num_removed': 'num_removed',  # noqa: E501
        'number': 'number',  # noqa: E501
        'target_branch_id': 'target_branch_id',  # noqa: E501
        'target_branch_name': 'target_branch_name',  # noqa: E501
        'title': 'title',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'url': 'url',  # noqa: E501
        'build_status': 'build_status',  # noqa: E501
        'review_status': 'review_status',  # noqa: E501
        'vcs_labels': 'vcs_labels',  # noqa: E501
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
    def __init__(self, branch_id, branch_name, closed, created_at, draft, entity_type, id, num_added, num_commits, num_modified, num_removed, number, target_branch_id, target_branch_name, title, updated_at, url, *args, **kwargs):  # noqa: E501
        """PullRequest - a model defined in OpenAPI

        Args:
            branch_id (int): The ID of the branch for the particular pull request.
            branch_name (str): The name of the branch for the particular pull request.
            closed (bool): True/False boolean indicating whether the VCS pull request has been closed.
            created_at (datetime): The time/date the pull request was created.
            draft (bool): True/False boolean indicating whether the VCS pull request is in the draft state.
            entity_type (str): A string description of this resource.
            id (int): The unique ID associated with the pull request in Clubhouse.
            num_added (int): Number of lines added in the pull request, according to VCS.
            num_commits (int, none_type): The number of commits on the pull request.
            num_modified (int, none_type): Number of lines modified in the pull request, according to VCS.
            num_removed (int): Number of lines removed in the pull request, according to VCS.
            number (int): The pull requests unique number ID in VCS.
            target_branch_id (int): The ID of the target branch for the particular pull request.
            target_branch_name (str): The name of the target branch for the particular pull request.
            title (str): The title of the pull request.
            updated_at (datetime): The time/date the pull request was created.
            url (str): The URL for the pull request.

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
            build_status (str): The status of the Continuous Integration workflow for the pull request.. [optional]  # noqa: E501
            review_status (str): The status of the review for the pull request.. [optional]  # noqa: E501
            vcs_labels ([PullRequestLabel], none_type): An array of PullRequestLabels attached to the PullRequest.. [optional]  # noqa: E501
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

        self.branch_id = branch_id
        self.branch_name = branch_name
        self.closed = closed
        self.created_at = created_at
        self.draft = draft
        self.entity_type = entity_type
        self.id = id
        self.num_added = num_added
        self.num_commits = num_commits
        self.num_modified = num_modified
        self.num_removed = num_removed
        self.number = number
        self.target_branch_id = target_branch_id
        self.target_branch_name = target_branch_name
        self.title = title
        self.updated_at = updated_at
        self.url = url
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
