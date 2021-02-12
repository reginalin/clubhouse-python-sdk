# UpdateStories

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**story_ids** | **[int]** | The Ids of the Stories you wish to update. | 
**after_id** | **int** | The ID of the story that the stories are to be moved below. | [optional] 
**archived** | **bool** | If the Stories should be archived or not. | [optional] 
**before_id** | **int** | The ID of the story that the stories are to be moved before. | [optional] 
**deadline** | **datetime, none_type** | The due date of the story. | [optional] 
**epic_id** | **int, none_type** | The ID of the epic the story belongs to. | [optional] 
**estimate** | **int, none_type** | The numeric point estimate of the story. Can also be null, which means unestimated. | [optional] 
**external_links** | **[str]** | An array of External Links associated with this story. | [optional] 
**follower_ids_add** | **[str]** | The UUIDs of the new followers to be added. | [optional] 
**follower_ids_remove** | **[str]** | The UUIDs of the followers to be removed. | [optional] 
**group_id** | **str, none_type** | The Id of the Group the Stories should belong to. | [optional] 
**iteration_id** | **int, none_type** | The ID of the iteration the story belongs to. | [optional] 
**labels_add** | [**[CreateLabelParams]**](CreateLabelParams.md) | An array of labels to be added. | [optional] 
**labels_remove** | [**[CreateLabelParams]**](CreateLabelParams.md) | An array of labels to be removed. | [optional] 
**move_to** | **str** |  | [optional] 
**owner_ids_add** | **[str]** | The UUIDs of the new owners to be added. | [optional] 
**owner_ids_remove** | **[str]** | The UUIDs of the owners to be removed. | [optional] 
**project_id** | **int** | The ID of the Project the Stories should belong to. | [optional] 
**requested_by_id** | **str** | The ID of the member that requested the story. | [optional] 
**story_type** | **str** | The type of story (feature, bug, chore). | [optional] 
**workflow_state_id** | **int** | The ID of the workflow state to put the stories in. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


