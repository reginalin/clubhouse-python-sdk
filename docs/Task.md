# Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** | True/false boolean indicating whether the Task has been completed. | 
**completed_at** | **datetime, none_type** | The time/date the Task was completed. | 
**created_at** | **datetime** | The time/date the Task was created. | 
**description** | **str** | Full text of the Task. | 
**entity_type** | **str** | A string description of this resource. | 
**external_id** | **str, none_type** | This field can be set to another unique ID. In the case that the Task has been imported from another tool, the ID in the other tool can be indicated here. | 
**group_mention_ids** | **[str]** | An array of UUIDs of Groups mentioned in this Task. | 
**id** | **int** | The unique ID of the Task. | 
**member_mention_ids** | **[str]** | An array of UUIDs of Members mentioned in this Task. | 
**mention_ids** | **[str]** | Deprecated: use member_mention_ids. | 
**owner_ids** | **[str]** | An array of UUIDs of the Owners of this Task. | 
**position** | **int** | The number corresponding to the Task&#39;s position within a list of Tasks on a Story. | 
**story_id** | **int** | The unique identifier of the parent Story. | 
**updated_at** | **datetime, none_type** | The time/date the Task was updated. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


