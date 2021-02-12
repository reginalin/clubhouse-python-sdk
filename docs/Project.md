# Project

Projects typically map to teams (such as Frontend, Backend, Mobile, Devops, etc) but can represent any open-ended product, component, or initiative.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviation** | **str, none_type** | The Project abbreviation used in Story summaries. Should be kept to 3 characters at most. | 
**app_url** | **str** | The Clubhouse application url for the Project. | 
**archived** | **bool** | True/false boolean indicating whether the Project is in an Archived state. | 
**color** | **str, none_type** | The color associated with the Project in the Clubhouse member interface. | 
**created_at** | **datetime, none_type** | The time/date that the Project was created. | 
**days_to_thermometer** | **int** | The number of days before the thermometer appears in the Story summary. | 
**description** | **str, none_type** | The description of the Project. | 
**entity_type** | **str** | A string description of this resource. | 
**external_id** | **str, none_type** | This field can be set to another unique ID. In the case that the Project has been imported from another tool, the ID in the other tool can be indicated here. | 
**follower_ids** | **[str]** | An array of UUIDs for any Members listed as Followers. | 
**id** | **int** | The unique ID of the Project. | 
**iteration_length** | **int** | The number of weeks per iteration in this Project. | 
**name** | **str** | The name of the Project | 
**show_thermometer** | **bool** | Configuration to enable or disable thermometers in the Story summary. | 
**start_time** | **datetime** | The date at which the Project was started. | 
**stats** | [**ProjectStats**](ProjectStats.md) |  | 
**team_id** | **int** | The ID of the team the project belongs to. | 
**updated_at** | **datetime, none_type** | The time/date that the Project was last updated. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


