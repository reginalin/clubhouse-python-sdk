# EntityTemplate

An entity template can be used to prefill various fields when creating new stories.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | The unique ID of the member who created the template. | 
**created_at** | **datetime** | The time/date when the entity template was created. | 
**entity_type** | **str** | A string description of this resource. | 
**id** | **str** | The unique identifier for the entity template. | 
**last_used_at** | **datetime** | The last time that someone created an entity using this template. | 
**name** | **str** | The template&#39;s name. | 
**story_contents** | [**StoryContents**](StoryContents.md) |  | 
**updated_at** | **datetime** | The time/date when the entity template was last updated. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


