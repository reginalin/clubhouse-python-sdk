# Member

Details about individual Clubhouse user within the Clubhouse organization that has issued the token.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime, none_type** | The time/date the Member was created. | 
**created_without_invite** | **bool** | Whether this member was created as a placeholder entity. | 
**disabled** | **bool** | True/false boolean indicating whether the Member has been disabled within this Organization. | 
**entity_type** | **str** | A string description of this resource. | 
**group_ids** | **[str]** | The Member&#39;s group ids | 
**id** | **str** | The Member&#39;s ID in Clubhouse. | 
**profile** | [**Profile**](Profile.md) |  | 
**role** | **str** | The Member&#39;s role in the Clubhouse organization. | 
**updated_at** | **datetime, none_type** | The time/date the Member was last updated. | 
**replaced_by** | **str** | The id of the member that replaces this one when merged. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


