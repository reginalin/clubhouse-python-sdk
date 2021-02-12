# ThreadedComment

Comments associated with Epic Discussions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Clubhouse application url for the Comment. | 
**author_id** | **str** | The unique ID of the Member that authored the Comment. | 
**comments** | [**[ThreadedComment]**](ThreadedComment.md) | A nested array of threaded comments. | 
**created_at** | **datetime** | The time/date the Comment was created. | 
**deleted** | **bool** | True/false boolean indicating whether the Comment is deleted. | 
**entity_type** | **str** | A string description of this resource. | 
**external_id** | **str, none_type** | This field can be set to another unique ID. In the case that the Comment has been imported from another tool, the ID in the other tool can be indicated here. | 
**group_mention_ids** | **[str]** | An array of Group IDs that have been mentioned in this Comment. | 
**id** | **int** | The unique ID of the Comment. | 
**member_mention_ids** | **[str]** | An array of Member IDs that have been mentioned in this Comment. | 
**mention_ids** | **[str]** | Deprecated: use member_mention_ids. | 
**text** | **str** | The text of the Comment. | 
**updated_at** | **datetime** | The time/date the Comment was updated. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


