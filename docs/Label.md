# Label

A Label can be used to associate and filter Stories and Epics, and also create new Workspaces.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Clubhouse application url for the Label. | 
**archived** | **bool** | A true/false boolean indicating if the Label has been archived. | 
**color** | **str, none_type** | The hex color to be displayed with the Label (for example, \&quot;#ff0000\&quot;). | 
**created_at** | **datetime, none_type** | The time/date that the Label was created. | 
**description** | **str, none_type** | The description of the Label. | 
**entity_type** | **str** | A string description of this resource. | 
**external_id** | **str, none_type** | This field can be set to another unique ID. In the case that the Label has been imported from another tool, the ID in the other tool can be indicated here. | 
**id** | **int** | The unique ID of the Label. | 
**name** | **str** | The name of the Label. | 
**updated_at** | **datetime, none_type** | The time/date that the Label was updated. | 
**stats** | [**LabelStats**](LabelStats.md) |  | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


