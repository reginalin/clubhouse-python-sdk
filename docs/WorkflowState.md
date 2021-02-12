# WorkflowState

Workflow State is any of the at least 3 columns. Workflow States correspond to one of 3 types: Unstarted, Started, or Done.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The hex color for this Workflow State. | 
**created_at** | **datetime** | The time/date the Workflow State was created. | 
**description** | **str** | The description of what sort of Stories belong in that Workflow state. | 
**entity_type** | **str** | A string description of this resource. | 
**id** | **int** | The unique ID of the Workflow State. | 
**name** | **str** | The Workflow State&#39;s name. | 
**num_stories** | **int** | The number of Stories currently in that Workflow State. | 
**num_story_templates** | **int** | The number of Story Templates associated with that Workflow State. | 
**position** | **int** | The position that the Workflow State is in, starting with 0 at the left. | 
**type** | **str** | The type of Workflow State (Unstarted, Started, or Finished) | 
**updated_at** | **datetime** | When the Workflow State was last updated. | 
**verb** | **str, none_type** | The verb that triggers a move to that Workflow State when making VCS commits. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


