# UpdateEpic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_id** | **int** | The ID of the Epic we want to move this Epic after. | [optional] 
**archived** | **bool** | A true/false boolean indicating whether the Epic is in archived state. | [optional] 
**before_id** | **int** | The ID of the Epic we want to move this Epic before. | [optional] 
**completed_at_override** | **datetime, none_type** | A manual override for the time/date the Epic was completed. | [optional] 
**deadline** | **datetime, none_type** | The Epic&#39;s deadline. | [optional] 
**description** | **str** | The Epic&#39;s description. | [optional] 
**epic_state_id** | **int** | The ID of the Epic State. | [optional] 
**follower_ids** | **[str]** | An array of UUIDs for any Members you want to add as Followers on this Epic. | [optional] 
**group_id** | **str, none_type** | The ID of the group to associate with the epic. | [optional] 
**labels** | [**[CreateLabelParams]**](CreateLabelParams.md) | An array of Labels attached to the Epic. | [optional] 
**milestone_id** | **int, none_type** | The ID of the Milestone this Epic is related to. | [optional] 
**name** | **str** | The Epic&#39;s name. | [optional] 
**owner_ids** | **[str]** | An array of UUIDs for any members you want to add as Owners on this Epic. | [optional] 
**planned_start_date** | **datetime, none_type** | The Epic&#39;s planned start date. | [optional] 
**requested_by_id** | **str** | The ID of the member that requested the epic. | [optional] 
**started_at_override** | **datetime, none_type** | A manual override for the time/date the Epic was started. | [optional] 
**state** | **str** | &#x60;Deprecated&#x60; The Epic&#39;s state (to do, in progress, or done); will be ignored when &#x60;epic_state_id&#x60; is set. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


