# EntityTemplateTask

Request parameters for specifying how to pre-populate a task through a template.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The Task description. | 
**complete** | **bool** | True/false boolean indicating whether the Task is completed. Defaults to false. | [optional] 
**external_id** | **str** | This field can be set to another unique ID. In the case that the Task has been imported from another tool, the ID in the other tool can be indicated here. | [optional] 
**owner_ids** | **[str]** | An array of UUIDs for any members you want to add as Owners on this new Task. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


