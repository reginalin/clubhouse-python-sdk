# CreateIteration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** | The date this Iteration ends, e.g. 2019-07-01. | 
**name** | **str** | The name of this Iteration. | 
**start_date** | **str** | The date this Iteration begins, e.g. 2019-07-01. | 
**description** | **str** | The description of the Iteration. | [optional] 
**follower_ids** | **[str]** | An array of UUIDs for any Members you want to add as Followers. | [optional] 
**group_ids** | **[str]** | An array of UUIDs for any Groups you want to add as Followers. Currently, only one Group association is presented in our web UI. | [optional] 
**labels** | [**[CreateLabelParams]**](CreateLabelParams.md) | An array of Labels attached to the Iteration. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


