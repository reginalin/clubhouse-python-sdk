# StoryContentsTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Full text of the Task. | 
**complete** | **bool** | True/false boolean indicating whether the Task has been completed. | [optional] 
**external_id** | **str, none_type** | This field can be set to another unique ID. In the case that the Task has been imported from another tool, the ID in the other tool can be indicated here. | [optional] 
**owner_ids** | **[str]** | An array of UUIDs of the Owners of this Task. | [optional] 
**position** | **int** | The number corresponding to the Task&#39;s position within a list of Tasks on a Story. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


