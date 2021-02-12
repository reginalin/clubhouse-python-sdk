# Milestone

A Milestone is a collection of Epics that represent a release or some other large initiative that your organization is working on.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Clubhouse application url for the Milestone. | 
**categories** | [**[Category]**](Category.md) | An array of Categories attached to the Milestone. | 
**completed** | **bool** | A true/false boolean indicating if the Milestone has been completed. | 
**completed_at** | **datetime, none_type** | The time/date the Milestone was completed. | 
**completed_at_override** | **datetime, none_type** | A manual override for the time/date the Milestone was completed. | 
**created_at** | **datetime** | The time/date the Milestone was created. | 
**description** | **str** | The Milestone&#39;s description. | 
**entity_type** | **str** | A string description of this resource. | 
**id** | **int** | The unique ID of the Milestone. | 
**name** | **str** | The name of the Milestone. | 
**position** | **int** | A number representing the position of the Milestone in relation to every other Milestone within the Organization. | 
**started** | **bool** | A true/false boolean indicating if the Milestone has been started. | 
**started_at** | **datetime, none_type** | The time/date the Milestone was started. | 
**started_at_override** | **datetime, none_type** | A manual override for the time/date the Milestone was started. | 
**state** | **str** | The workflow state that the Milestone is in. | 
**updated_at** | **datetime** | The time/date the Milestone was updated. | 
**stats** | [**MilestoneStats**](MilestoneStats.md) |  | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


