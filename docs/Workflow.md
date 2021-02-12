# Workflow

Details of the workflow associated with the Team.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_assign_owner** | **bool** | Indicates if an owner is automatically assigned when an unowned story is started. | 
**created_at** | **datetime** | The date the Workflow was created. | 
**default_state_id** | **int** | The unique ID of the default state that new Stories are entered into. | 
**description** | **str** | A description of the workflow. | 
**entity_type** | **str** | A string description of this resource. | 
**id** | **int** | The unique ID of the Workflow. | 
**name** | **str** | The name of the workflow. | 
**project_ids** | **[float]** | An array of IDs of projects within the Workflow. | 
**states** | [**[WorkflowState]**](WorkflowState.md) | A map of the states in this Workflow. | 
**team_id** | **int** | The ID of the team the workflow belongs to. | 
**updated_at** | **datetime** | The date the Workflow was updated. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


