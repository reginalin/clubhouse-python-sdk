# File

A File is any document uploaded to your Clubhouse. Files attached from a third-party service can be accessed using the Linked Files endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | Free form string corresponding to a text or image file. | 
**created_at** | **datetime** | The time/date that the file was created. | 
**description** | **str, none_type** | The description of the file. | 
**entity_type** | **str** | A string description of this resource. | 
**external_id** | **str, none_type** | This field can be set to another unique ID. In the case that the File has been imported from another tool, the ID in the other tool can be indicated here. | 
**filename** | **str** | The name assigned to the file in Clubhouse upon upload. | 
**group_mention_ids** | **[str]** | The unique IDs of the Groups who are mentioned in the file description. | 
**id** | **int** | The unique ID for the file. | 
**member_mention_ids** | **[str]** | The unique IDs of the Members who are mentioned in the file description. | 
**mention_ids** | **[str]** | Deprecated: use member_mention_ids. | 
**name** | **str** | The optional User-specified name of the file. | 
**size** | **int** | The size of the file. | 
**story_ids** | **[int]** | The unique IDs of the Stories associated with this file. | 
**thumbnail_url** | **str, none_type** | The url where the thumbnail of the file can be found in Clubhouse. | 
**updated_at** | **datetime, none_type** | The time/date that the file was updated. | 
**uploader_id** | **str** | The unique ID of the Member who uploaded the file. | 
**url** | **str, none_type** | The URL for the file. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


