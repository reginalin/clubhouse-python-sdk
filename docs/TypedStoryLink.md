# TypedStoryLink

The type of Story Link. The string can be subject or object. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time/date when the Story Link was created. | 
**entity_type** | **str** | A string description of this resource. | 
**id** | **int** | The unique identifier of the Story Link. | 
**object_id** | **int** | The ID of the object Story. | 
**subject_id** | **int** | The ID of the subject Story. | 
**type** | **str** | This indicates whether the Story is the subject or object in the Story Link. | 
**updated_at** | **datetime** | The time/date when the Story Link was last updated. | 
**verb** | **str** | How the subject Story acts on the object Story. This can be \&quot;blocks\&quot;, \&quot;duplicates\&quot;, or \&quot;relates to\&quot;. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


