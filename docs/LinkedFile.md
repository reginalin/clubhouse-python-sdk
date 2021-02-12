# LinkedFile

Linked files are stored on a third-party website and linked to one or more Stories. Clubhouse currently supports linking files from Google Drive, Dropbox, Box, and by URL.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str, none_type** | The content type of the image (e.g. txt/plain). | 
**created_at** | **datetime** | The time/date the LinkedFile was created. | 
**description** | **str, none_type** | The description of the file. | 
**entity_type** | **str** | A string description of this resource. | 
**group_mention_ids** | **[str]** | The groups that are mentioned in the description of the file. | 
**id** | **int** | The unique identifier for the file. | 
**member_mention_ids** | **[str]** | The members that are mentioned in the description of the file. | 
**mention_ids** | **[str]** | Deprecated: use member_mention_ids. | 
**name** | **str** | The name of the linked file. | 
**size** | **int, none_type** | The filesize, if the integration provided it. | 
**story_ids** | **[int]** | The IDs of the stories this file is attached to. | 
**thumbnail_url** | **str, none_type** | The URL of the file thumbnail, if the integration provided it. | 
**type** | **str** | The integration type (e.g. google, dropbox, box). | 
**updated_at** | **datetime** | The time/date the LinkedFile was updated. | 
**uploader_id** | **str** | The UUID of the member that uploaded the file. | 
**url** | **str** | The URL of the file. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


