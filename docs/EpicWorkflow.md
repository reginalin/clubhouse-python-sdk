# EpicWorkflow

Epic Workflow is the array of defined Epic States. Epic Workflow can be queried using the API but must be updated in the Clubhouse UI. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date the Epic Workflow was created. | 
**default_epic_state_id** | **int** | The unique ID of the default Epic State that new Epics are assigned by default. | 
**entity_type** | **str** | A string description of this resource. | 
**epic_states** | [**[EpicState]**](EpicState.md) | A map of the Epic States in this Epic Workflow. | 
**id** | **int** | The unique ID of the Epic Workflow. | 
**updated_at** | **datetime** | The date the Epic Workflow was updated. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


