# Comment

A Comment is any note added within the Comment field of a Story.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Clubhouse application url for the Comment. | 
**author_id** | **str, none_type** | The unique ID of the Member who is the Comment&#39;s author. | 
**created_at** | **datetime** | The time/date when the Comment was created. | 
**entity_type** | **str** | A string description of this resource. | 
**external_id** | **str, none_type** | This field can be set to another unique ID. In the case that the Comment has been imported from another tool, the ID in the other tool can be indicated here. | 
**group_mention_ids** | **[str]** | The unique IDs of the Group who are mentioned in the Comment. | 
**id** | **int** | The unique ID of the Comment. | 
**member_mention_ids** | **[str]** | The unique IDs of the Member who are mentioned in the Comment. | 
**mention_ids** | **[str]** | Deprecated: use member_mention_ids. | 
**position** | **int** | The Comments numerical position in the list from oldest to newest. | 
**reactions** | [**[Reaction]**](Reaction.md) | A set of Reactions to this Comment. | 
**story_id** | **int** | The ID of the Story on which the Comment appears. | 
**text** | **str** | The text of the Comment. | 
**updated_at** | **datetime, none_type** | The time/date when the Comment was updated. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


