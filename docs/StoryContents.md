# StoryContents

A container entity for the attributes this template should populate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deadline** | **datetime** | The due date of the story. | [optional] 
**description** | **str** | The description of the story. | [optional] 
**entity_type** | **str** | A string description of this resource. | [optional] 
**epic_id** | **int** | The ID of the epic the story belongs to. | [optional] 
**estimate** | **int** | The numeric point estimate of the story. Can also be null, which means unestimated. | [optional] 
**external_links** | **[str]** | An array of external links connected to the story. | [optional] 
**external_tickets** | [**[ExternalTicket]**](ExternalTicket.md) | An array of external tickets connected to the story. | [optional] 
**files** | [**[File]**](File.md) | An array of files attached to the story. | [optional] 
**follower_ids** | **[str]** | An array of UUIDs for any Members listed as Followers. | [optional] 
**iteration_id** | **int** | The ID of the iteration the story belongs to. | [optional] 
**labels** | [**[Label]**](Label.md) | An array of labels attached to the story. | [optional] 
**linked_files** | [**[LinkedFile]**](LinkedFile.md) | An array of linked files attached to the story. | [optional] 
**name** | **str** | The name of the story. | [optional] 
**owner_ids** | **[str]** | An array of UUIDs of the owners of this story. | [optional] 
**project_id** | **int** | The ID of the project the story belongs to. | [optional] 
**story_type** | **str** | The type of story (feature, bug, chore). | [optional] 
**tasks** | [**[StoryContentsTask]**](StoryContentsTask.md) | An array of tasks connected to the story. | [optional] 
**workflow_state_id** | **int** | The ID of the workflow state the story is currently in. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


