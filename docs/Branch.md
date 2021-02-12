# Branch

Branch refers to a VCS branch. Branches are feature branches associated with Clubhouse Stories.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime, none_type** | The time/date the Branch was created. | 
**deleted** | **bool** | A true/false boolean indicating if the Branch has been deleted. | 
**entity_type** | **str** | A string description of this resource. | 
**id** | **int, none_type** | The unique ID of the Branch. | 
**merged_branch_ids** | **[int]** | The IDs of the Branches the Branch has been merged into. | 
**name** | **str** | The name of the Branch. | 
**persistent** | **bool** | A true/false boolean indicating if the Branch is persistent; e.g. master. | 
**pull_requests** | [**[PullRequest]**](PullRequest.md) | An array of PullRequests attached to the Branch (there is usually only one). | 
**repository_id** | **int, none_type** | The ID of the Repository that contains the Branch. | 
**updated_at** | **datetime, none_type** | The time/date the Branch was updated. | 
**url** | **str** | The URL of the Branch. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


