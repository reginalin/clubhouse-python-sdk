# IterationSlim

IterationSlim represents the same resource as an Iteration, but is more light-weight. Use the [Get Iteration](#Get-Iteration) endpoint to fetch the unabridged payload for an Iteration. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Clubhouse application url for the Iteration. | 
**created_at** | **datetime** | The instant when this iteration was created. | 
**end_date** | **datetime** | The date this iteration begins. | 
**entity_type** | **str** | A string description of this resource | 
**follower_ids** | **[str]** | An array of UUIDs for any Members listed as Followers. | 
**group_ids** | **[str]** | An array of UUIDs for any Groups you want to add as Followers. Currently, only one Group association is presented in our web UI. | 
**group_mention_ids** | **[str]** | An array of Group IDs that have been mentioned in the Story description. | 
**id** | **int** | The ID of the iteration. | 
**labels** | [**[Label]**](Label.md) | An array of labels attached to the iteration. | 
**member_mention_ids** | **[str]** | An array of Member IDs that have been mentioned in the Story description. | 
**mention_ids** | **[str]** | Deprecated: use member_mention_ids. | 
**name** | **str** | The name of the iteration. | 
**start_date** | **datetime** | The date this iteration begins. | 
**stats** | [**IterationStats**](IterationStats.md) |  | 
**status** | **str** | The status of the iteration. Values are either \&quot;unstarted\&quot;, \&quot;started\&quot;, or \&quot;done\&quot;. | 
**updated_at** | **datetime** | The instant when this iteration was last updated. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


