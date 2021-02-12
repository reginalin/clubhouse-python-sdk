# Story

Stories are the standard unit of work in Clubhouse and represent individual features, bugs, and chores.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Clubhouse application url for the Story. | 
**archived** | **bool** | True if the story has been archived or not. | 
**blocked** | **bool** | A true/false boolean indicating if the Story is currently blocked. | 
**blocker** | **bool** | A true/false boolean indicating if the Story is currently a blocker of another story. | 
**branches** | [**[Branch]**](Branch.md) | An array of Git branches attached to the story. | 
**comments** | [**[Comment]**](Comment.md) | An array of comments attached to the story. | 
**commits** | [**[Commit]**](Commit.md) | An array of commits attached to the story. | 
**completed** | **bool** | A true/false boolean indicating if the Story has been completed. | 
**completed_at** | **datetime, none_type** | The time/date the Story was completed. | 
**completed_at_override** | **datetime, none_type** | A manual override for the time/date the Story was completed. | 
**created_at** | **datetime** | The time/date the Story was created. | 
**deadline** | **datetime, none_type** | The due date of the story. | 
**description** | **str** | The description of the story. | 
**entity_type** | **str** | A string description of this resource. | 
**epic_id** | **int, none_type** | The ID of the epic the story belongs to. | 
**estimate** | **int, none_type** | The numeric point estimate of the story. Can also be null, which means unestimated. | 
**external_id** | **str, none_type** | This field can be set to another unique ID. In the case that the Story has been imported from another tool, the ID in the other tool can be indicated here. | 
**external_links** | **[str]** | An array of external link (strings) associated with a Story | 
**external_tickets** | [**[ExternalTicket]**](ExternalTicket.md) | An array of External Tickets associated with a Story | 
**files** | [**[File]**](File.md) | An array of files attached to the story. | 
**follower_ids** | **[str]** | An array of UUIDs for any Members listed as Followers. | 
**group_id** | **str, none_type** | The ID of the group associated with the story. | 
**group_mention_ids** | **[str]** | An array of Group IDs that have been mentioned in the Story description. | 
**id** | **int** | The unique ID of the Story. | 
**iteration_id** | **int, none_type** | The ID of the iteration the story belongs to. | 
**labels** | [**[Label]**](Label.md) | An array of labels attached to the story. | 
**linked_files** | [**[LinkedFile]**](LinkedFile.md) | An array of linked files attached to the story. | 
**member_mention_ids** | **[str]** | An array of Member IDs that have been mentioned in the Story description. | 
**mention_ids** | **[str]** | Deprecated: use member_mention_ids. | 
**moved_at** | **datetime, none_type** | The time/date the Story was last changed workflow-state. | 
**name** | **str** | The name of the story. | 
**owner_ids** | **[str]** | An array of UUIDs of the owners of this story. | 
**position** | **int** | A number representing the position of the story in relation to every other story in the current project. | 
**previous_iteration_ids** | **[int]** | The IDs of the iteration the story belongs to. | 
**project_id** | **int** | The ID of the project the story belongs to. | 
**pull_requests** | [**[PullRequest]**](PullRequest.md) | An array of Pull/Merge Requests attached to the story. | 
**requested_by_id** | **str** | The ID of the Member that requested the story. | 
**started** | **bool** | A true/false boolean indicating if the Story has been started. | 
**started_at** | **datetime, none_type** | The time/date the Story was started. | 
**started_at_override** | **datetime, none_type** | A manual override for the time/date the Story was started. | 
**stats** | [**StoryStats**](StoryStats.md) |  | 
**story_links** | [**[TypedStoryLink]**](TypedStoryLink.md) | An array of story links attached to the Story. | 
**story_type** | **str** | The type of story (feature, bug, chore). | 
**support_tickets** | [**[SupportTicket]**](SupportTicket.md) |  | 
**tasks** | [**[Task]**](Task.md) | An array of tasks connected to the story. | 
**updated_at** | **datetime, none_type** | The time/date the Story was updated. | 
**workflow_state_id** | **int** | The ID of the workflow state the story is currently in. | 
**cycle_time** | **int** | The cycle time (in seconds) of this story when complete. | [optional] 
**lead_time** | **int** | The lead time (in seconds) of this story when complete. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


