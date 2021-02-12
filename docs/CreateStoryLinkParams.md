# CreateStoryLinkParams

Request parameters for creating a Story Link within a Story.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verb** | **str** | How the subject Story acts on the object Story. This can be \&quot;blocks\&quot;, \&quot;duplicates\&quot;, or \&quot;relates to\&quot;. | 
**object_id** | **int** | The unique ID of the Story defined as object. | [optional] 
**subject_id** | **int** | The unique ID of the Story defined as subject. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


