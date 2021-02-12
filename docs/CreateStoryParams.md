# CreateStoryParams

Used to create multiple stories in a single request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the story. | 
**project_id** | **int** | The ID of the project the story belongs to. | 
**archived** | **bool** | Controls the story&#39;s archived state. | [optional] 
**comments** | [**[CreateStoryCommentParams]**](CreateStoryCommentParams.md) | An array of comments to add to the story. | [optional] 
**completed_at_override** | **datetime** | A manual override for the time/date the Story was completed. | [optional] 
**created_at** | **datetime** | The time/date the Story was created. | [optional] 
**deadline** | **datetime, none_type** | The due date of the story. | [optional] 
**description** | **str** | The description of the story. | [optional] 
**epic_id** | **int, none_type** | The ID of the epic the story belongs to. | [optional] 
**estimate** | **int, none_type** | The numeric point estimate of the story. Can also be null, which means unestimated. | [optional] 
**external_id** | **str** | This field can be set to another unique ID. In the case that the Story has been imported from another tool, the ID in the other tool can be indicated here. | [optional] 
**external_links** | **[str]** | An array of External Links associated with this story. | [optional] 
**external_tickets** | [**[CreateExternalTicketParams]**](CreateExternalTicketParams.md) | An array of External Tickets associated with this story. These External Tickets must have unquie external id. Duplicated External Tickets will be removed. | [optional] 
**file_ids** | **[int]** | An array of IDs of files attached to the story. | [optional] 
**follower_ids** | **[str]** | An array of UUIDs of the followers of this story. | [optional] 
**group_id** | **str, none_type** | The id of the group to associate with this story. | [optional] 
**iteration_id** | **int, none_type** | The ID of the iteration the story belongs to. | [optional] 
**labels** | [**[CreateLabelParams]**](CreateLabelParams.md) | An array of labels attached to the story. | [optional] 
**linked_file_ids** | **[int]** | An array of IDs of linked files attached to the story. | [optional] 
**owner_ids** | **[str]** | An array of UUIDs of the owners of this story. | [optional] 
**requested_by_id** | **str** | The ID of the member that requested the story. | [optional] 
**started_at_override** | **datetime** | A manual override for the time/date the Story was started. | [optional] 
**story_links** | [**[CreateStoryLinkParams]**](CreateStoryLinkParams.md) | An array of story links attached to the story. | [optional] 
**story_type** | **str** | The type of story (feature, bug, chore). | [optional] 
**support_tickets** | [**[CreateExternalTicketParams]**](CreateExternalTicketParams.md) |  | [optional] 
**tasks** | [**[CreateTaskParams]**](CreateTaskParams.md) | An array of tasks connected to the story. | [optional] 
**updated_at** | **datetime** | The time/date the Story was updated. | [optional] 
**workflow_state_id** | **int** | The ID of the workflow state the story will be in. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


