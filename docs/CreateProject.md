# CreateProject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Project. | 
**team_id** | **int** | The ID of the team the project belongs to. | 
**abbreviation** | **str** | The Project abbreviation used in Story summaries. Should be kept to 3 characters at most. | [optional] 
**color** | **str** | The color you wish to use for the Project in the system. | [optional] 
**created_at** | **datetime** | Defaults to the time/date it is created but can be set to reflect another date. | [optional] 
**description** | **str** | The Project description. | [optional] 
**external_id** | **str** | This field can be set to another unique ID. In the case that the Project has been imported from another tool, the ID in the other tool can be indicated here. | [optional] 
**follower_ids** | **[str]** | An array of UUIDs for any members you want to add as Owners on this new Epic. | [optional] 
**iteration_length** | **int** | The number of weeks per iteration in this Project. | [optional] 
**start_time** | **datetime** | The date at which the Project was started. | [optional] 
**updated_at** | **datetime** | Defaults to the time/date it is created but can be set to reflect another date. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


