# ExternalTicket

A External Ticket allows you to create a link between an external system, like Zendesk, and a Clubhouse story.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The ID used in the external system. | 
**id** | **str** | A unique ID internal to Clubhouse. | 
**story_ids** | **[float]** | The Clubhouse Story ids associated with this External Ticket. | 
**external_url** | **str** | The full qualified url of the external ticket. | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


