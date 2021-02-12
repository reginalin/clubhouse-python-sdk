# StorySlim

StorySlim represents the same resource as a Story, but is more light-weight. For certain fields it provides ids rather than full resources (e.g., `comment_ids` and `file_ids`) and it also excludes certain aggregate values (e.g., `cycle_time`). The `description` field can be optionally included. Use the [Get Story](#Get-Story) endpoint to fetch the unabridged payload for a Story.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Clubhouse application url for the Story. | 
**archived** | **bool** | True if the story has been archived or not. | 
**blocked** | **bool** | A true/false boolean indicating if the Story is currently blocked. | 
**blocker** | **bool** | A true/false boolean indicating if the Story is currently a blocker of another story. | 
**comment_ids** | **[int]** | An array of IDs of Comments attached to the story. | 
**completed** | **bool** | A true/false boolean indicating if the Story has been completed. | 
**completed_at** | **datetime, none_type** | The time/date the Story was completed. | 
**completed_at_override** | **datetime, none_type** | A manual override for the time/date the Story was completed. | 
**created_at** | **datetime** | The time/date the Story was created. | 
**deadline** | **datetime, none_type** | The due date of the story. | 
**entity_type** | **str** | A string description of this resource. | 
**epic_id** | **int, none_type** | The ID of the epic the story belongs to. | 
**estimate** | **int, none_type** | The numeric point estimate of the story. Can also be null, which means unestimated. | 
**external_id** | **str, none_type** | This field can be set to another unique ID. In the case that the Story has been imported from another tool, the ID in the other tool can be indicated here. | 
**external_links** | **[str]** | An array of external link (strings) associated with a Story | 
**external_tickets** | [**[ExternalTicket]**](ExternalTicket.md) | An array of External Tickets associated with a Story | 
**file_ids** | **[int]** | An array of IDs of Files attached to the story. | 
**follower_ids** | **[str]** | An array of UUIDs for any Members listed as Followers. | 
**group_id** | **str, none_type** | The ID of the group associated with the story. | 
**group_mention_ids** | **[str]** | An array of Group IDs that have been mentioned in the Story description. | 
**id** | **int** | The unique ID of the Story. | 
**iteration_id** | **int, none_type** | The ID of the iteration the story belongs to. | 
**labels** | [**[Label]**](Label.md) | An array of labels attached to the story. | 
**linked_file_ids** | **[int]** | An array of IDs of LinkedFiles attached to the story. | 
**member_mention_ids** | **[str]** | An array of Member IDs that have been mentioned in the Story description. | 
**mention_ids** | **[str]** | Deprecated: use member_mention_ids. | 
**moved_at** | **datetime, none_type** | The time/date the Story was last changed workflow-state. | 
**name** | **str** | The name of the story. | 
**num_tasks_completed** | **int** | The number of tasks on the story which are complete. | 
**owner_ids** | **[str]** | An array of UUIDs of the owners of this story. | 
**position** | **int** | A number representing the position of the story in relation to every other story in the current project. | 
**previous_iteration_ids** | **[int]** | The IDs of the iteration the story belongs to. | 
**project_id** | **int** | The ID of the project the story belongs to. | 
**requested_by_id** | **str** | The ID of the Member that requested the story. | 
**started** | **bool** | A true/false boolean indicating if the Story has been started. | 
**started_at** | **datetime, none_type** | The time/date the Story was started. | 
**started_at_override** | **datetime, none_type** | A manual override for the time/date the Story was started. | 
**stats** | [**StoryStats**](StoryStats.md) |  | 
**story_links** | [**[TypedStoryLink]**](TypedStoryLink.md) | An array of story links attached to the Story. | 
**story_type** | **str** | The type of story (feature, bug, chore). | 
**support_tickets** | [**[SupportTicket]**](SupportTicket.md) |  | 
**task_ids** | **[int]** | An array of IDs of Tasks attached to the story. | 
**updated_at** | **datetime, none_type** | The time/date the Story was updated. | 
**workflow_state_id** | **int** | The ID of the workflow state the story is currently in. | 
**cycle_time** | **int** | The cycle time (in seconds) of this story when complete. | [optional] 
**description** | **str** | The description of the Story. | [optional] 
**lead_time** | **int** | The lead time (in seconds) of this story when complete. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


