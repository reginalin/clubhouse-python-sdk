# CreateStoryContents

A map of story attributes this template populates.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deadline** | **datetime, none_type** | The due date of the story. | [optional] 
**description** | **str** | The description of the story. | [optional] 
**entity_type** | **str** | A string description of this resource. | [optional] 
**epic_id** | **int, none_type** | The ID of the epic the to be populated. | [optional] 
**estimate** | **int, none_type** | The numeric point estimate to be populated. | [optional] 
**external_links** | **[str]** | An array of external links to be populated. | [optional] 
**external_tickets** | [**[CreateEntityTemplateExternalTicket]**](CreateEntityTemplateExternalTicket.md) | An array of the external ticket IDs to be populated. | [optional] 
**file_ids** | **[int]** | An array of the attached file IDs to be populated. | [optional] 
**files** | [**[File]**](File.md) | An array of files attached to the story. | [optional] 
**follower_ids** | **[str]** | An array of UUIDs for any Members listed as Followers. | [optional] 
**iteration_id** | **int, none_type** | The ID of the iteration the to be populated. | [optional] 
**labels** | [**[CreateLabelParams]**](CreateLabelParams.md) | An array of labels to be populated by the template. | [optional] 
**linked_file_ids** | **[int]** | An array of the linked file IDs to be populated. | [optional] 
**linked_files** | [**[LinkedFile]**](LinkedFile.md) | An array of linked files attached to the story. | [optional] 
**name** | **str** | The name of the story. | [optional] 
**owner_ids** | **[str]** | An array of UUIDs of the owners of this story. | [optional] 
**project_id** | **int** | The ID of the project the story belongs to. | [optional] 
**story_type** | **str** | The type of story (feature, bug, chore). | [optional] 
**tasks** | [**[EntityTemplateTask]**](EntityTemplateTask.md) | An array of tasks to be populated by the template. | [optional] 
**workflow_state_id** | **int** | The ID of the workflow state the story is currently in. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


