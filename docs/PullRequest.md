# PullRequest

Corresponds to a VCS Pull Request attached to a Clubhouse story.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **int** | The ID of the branch for the particular pull request. | 
**branch_name** | **str** | The name of the branch for the particular pull request. | 
**closed** | **bool** | True/False boolean indicating whether the VCS pull request has been closed. | 
**created_at** | **datetime** | The time/date the pull request was created. | 
**draft** | **bool** | True/False boolean indicating whether the VCS pull request is in the draft state. | 
**entity_type** | **str** | A string description of this resource. | 
**id** | **int** | The unique ID associated with the pull request in Clubhouse. | 
**num_added** | **int** | Number of lines added in the pull request, according to VCS. | 
**num_commits** | **int, none_type** | The number of commits on the pull request. | 
**num_modified** | **int, none_type** | Number of lines modified in the pull request, according to VCS. | 
**num_removed** | **int** | Number of lines removed in the pull request, according to VCS. | 
**number** | **int** | The pull requests unique number ID in VCS. | 
**target_branch_id** | **int** | The ID of the target branch for the particular pull request. | 
**target_branch_name** | **str** | The name of the target branch for the particular pull request. | 
**title** | **str** | The title of the pull request. | 
**updated_at** | **datetime** | The time/date the pull request was created. | 
**url** | **str** | The URL for the pull request. | 
**build_status** | **str** | The status of the Continuous Integration workflow for the pull request. | [optional] 
**review_status** | **str** | The status of the review for the pull request. | [optional] 
**vcs_labels** | [**[PullRequestLabel], none_type**](PullRequestLabel.md) | An array of PullRequestLabels attached to the PullRequest. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


