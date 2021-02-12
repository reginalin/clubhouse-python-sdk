# UpdateStory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_id** | **int** | The ID of the story we want to move this story after. | [optional] 
**archived** | **bool** | True if the story is archived, otherwise false. | [optional] 
**before_id** | **int** | The ID of the story we want to move this story before. | [optional] 
**branch_ids** | **[int]** | An array of IDs of Branches attached to the story. | [optional] 
**commit_ids** | **[int]** | An array of IDs of Commits attached to the story. | [optional] 
**completed_at_override** | **datetime, none_type** | A manual override for the time/date the Story was completed. | [optional] 
**deadline** | **datetime, none_type** | The due date of the story. | [optional] 
**description** | **str** | The description of the story. | [optional] 
**epic_id** | **int, none_type** | The ID of the epic the story belongs to. | [optional] 
**estimate** | **int, none_type** | The numeric point estimate of the story. Can also be null, which means unestimated. | [optional] 
**external_links** | **[str]** | An array of External Links associated with this story. | [optional] 
**file_ids** | **[int]** | An array of IDs of files attached to the story. | [optional] 
**follower_ids** | **[str]** | An array of UUIDs of the followers of this story. | [optional] 
**group_id** | **str, none_type** | The ID of the group to associate with this story | [optional] 
**iteration_id** | **int, none_type** | The ID of the iteration the story belongs to. | [optional] 
**labels** | [**[CreateLabelParams]**](CreateLabelParams.md) | An array of labels attached to the story. | [optional] 
**linked_file_ids** | **[int]** | An array of IDs of linked files attached to the story. | [optional] 
**move_to** | **str** |  | [optional] 
**name** | **str** | The title of the story. | [optional] 
**owner_ids** | **[str]** | An array of UUIDs of the owners of this story. | [optional] 
**project_id** | **int** | The ID of the project the story belongs to. | [optional] 
**pull_request_ids** | **[int]** | An array of IDs of Pull/Merge Requests attached to the story. | [optional] 
**requested_by_id** | **str** | The ID of the member that requested the story. | [optional] 
**started_at_override** | **datetime, none_type** | A manual override for the time/date the Story was started. | [optional] 
**story_type** | **str** | The type of story (feature, bug, chore). | [optional] 
**workflow_state_id** | **int** | The ID of the workflow state to put the story in. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


