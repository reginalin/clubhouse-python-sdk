# SearchStories

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** | A true/false boolean indicating whether the Story is in archived state. | [optional] 
**completed_at_end** | **datetime** | Stories should have been completed before this date. | [optional] 
**completed_at_start** | **datetime** | Stories should have been competed after this date. | [optional] 
**created_at_end** | **datetime** | Stories should have been created before this date. | [optional] 
**created_at_start** | **datetime** | Stories should have been created after this date. | [optional] 
**deadline_end** | **datetime** | Stories should have a deadline before this date. | [optional] 
**deadline_start** | **datetime** | Stories should have a deadline after this date. | [optional] 
**epic_id** | **int, none_type** | The Epic IDs that may be associated with the Stories. | [optional] 
**epic_ids** | **[int]** | The Epic IDs that may be associated with the Stories. | [optional] 
**estimate** | **int** | The number of estimate points associate with the Stories. | [optional] 
**external_id** | **str** | An ID or URL that references an external resource. Useful during imports. | [optional] 
**group_id** | **str, none_type** | The Group ID that is associated with the Stories | [optional] 
**group_ids** | **[str]** | The Group IDs that are associated with the Stories | [optional] 
**includes_description** | **bool** | Whether to include the story description in the response. | [optional] 
**iteration_id** | **int, none_type** | The Iteration ID that may be associated with the Stories. | [optional] 
**iteration_ids** | **[int]** | The Iteration IDs that may be associated with the Stories. | [optional] 
**label_ids** | **[int]** | The Label IDs that may be associated with the Stories. | [optional] 
**label_name** | **str** | The name of any associated Labels. | [optional] 
**owner_id** | **str, none_type** | An array of UUIDs for any Users who may be Owners of the Stories. | [optional] 
**owner_ids** | **[str]** | An array of UUIDs for any Users who may be Owners of the Stories. | [optional] 
**project_id** | **int** | The IDs for the Projects the Stories may be assigned to. | [optional] 
**project_ids** | **[int]** | The IDs for the Projects the Stories may be assigned to. | [optional] 
**requested_by_id** | **str** | The UUID of any Users who may have requested the Stories. | [optional] 
**story_type** | **str** | The type of Stories that you want returned. | [optional] 
**updated_at_end** | **datetime** | Stories should have been updated before this date. | [optional] 
**updated_at_start** | **datetime** | Stories should have been updated after this date. | [optional] 
**workflow_state_id** | **int** | The unique IDs of the specific Workflow States that the Stories should be in. | [optional] 
**workflow_state_types** | **[str]** | The type of Workflow State the Stories may be in. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


