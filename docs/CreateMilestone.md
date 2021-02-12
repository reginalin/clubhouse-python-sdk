# CreateMilestone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Milestone. | 
**categories** | [**[CreateCategoryParams]**](CreateCategoryParams.md) | An array of IDs of Categories attached to the Milestone. | [optional] 
**completed_at_override** | **datetime** | A manual override for the time/date the Milestone was completed. | [optional] 
**description** | **str** | The Milestone&#39;s description. | [optional] 
**started_at_override** | **datetime** | A manual override for the time/date the Milestone was started. | [optional] 
**state** | **str** | The workflow state that the Milestone is in. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


