# Commit

Commit refers to a VCS commit and all associated details.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_email** | **str** | The email address of the VCS user that authored the Commit. | 
**author_id** | **str, none_type** | The ID of the Member that authored the Commit, if known. | 
**author_identity** | [**Identity**](Identity.md) |  | 
**created_at** | **datetime** | The time/date the Commit was created. | 
**entity_type** | **str** | A string description of this resource. | 
**hash** | **str** | The Commit hash. | 
**id** | **int, none_type** | The unique ID of the Commit. | 
**merged_branch_ids** | **[int]** | The IDs of the Branches the Commit has been merged into. | 
**message** | **str** | The Commit message. | 
**repository_id** | **int, none_type** | The ID of the Repository that contains the Commit. | 
**timestamp** | **datetime** | The time/date the Commit was pushed. | 
**updated_at** | **datetime, none_type** | The time/date the Commit was updated. | 
**url** | **str** | The URL of the Commit. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


