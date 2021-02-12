# Epic

An Epic is a collection of stories that together might make up a release, a milestone, or some other large initiative that your organization is working on.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Clubhouse application url for the Epic. | 
**archived** | **bool** | True/false boolean that indicates whether the Epic is archived or not. | 
**comments** | [**[ThreadedComment]**](ThreadedComment.md) | A nested array of threaded comments. | 
**completed** | **bool** | A true/false boolean indicating if the Epic has been completed. | 
**completed_at** | **datetime, none_type** | The time/date the Epic was completed. | 
**completed_at_override** | **datetime, none_type** | A manual override for the time/date the Epic was completed. | 
**created_at** | **datetime, none_type** | The time/date the Epic was created. | 
**deadline** | **datetime, none_type** | The Epic&#39;s deadline. | 
**description** | **str** | The Epic&#39;s description. | 
**entity_type** | **str** | A string description of this resource. | 
**epic_state_id** | **int** | The ID of the Epic State. | 
**external_id** | **str, none_type** | This field can be set to another unique ID. In the case that the Epic has been imported from another tool, the ID in the other tool can be indicated here. | 
**external_tickets** | [**[ExternalTicket]**](ExternalTicket.md) |  | 
**follower_ids** | **[str]** | An array of UUIDs for any Members you want to add as Followers on this Epic. | 
**group_id** | **str, none_type** |  | 
**group_mention_ids** | **[str]** | An array of Group IDs that have been mentioned in the Epic description. | 
**id** | **int** | The unique ID of the Epic. | 
**labels** | [**[Label]**](Label.md) | An array of Labels attached to the Epic. | 
**member_mention_ids** | **[str]** | An array of Member IDs that have been mentioned in the Epic description. | 
**mention_ids** | **[str]** | Deprecated: use member_mention_ids. | 
**milestone_id** | **int, none_type** | The ID of the Milestone this Epic is related to. | 
**name** | **str** | The name of the Epic. | 
**owner_ids** | **[str]** | An array of UUIDs for any members you want to add as Owners on this new Epic. | 
**planned_start_date** | **datetime, none_type** | The Epic&#39;s planned start date. | 
**position** | **int** | The Epic&#39;s relative position in the Epic workflow state. | 
**project_ids** | **[int]** | The IDs of Projects related to this Epic. | 
**requested_by_id** | **str** | The ID of the Member that requested the epic. | 
**started** | **bool** | A true/false boolean indicating if the Epic has been started. | 
**started_at** | **datetime, none_type** | The time/date the Epic was started. | 
**started_at_override** | **datetime, none_type** | A manual override for the time/date the Epic was started. | 
**state** | **str** | &#x60;Deprecated&#x60; The workflow state that the Epic is in. | 
**stats** | [**EpicStats**](EpicStats.md) |  | 
**support_tickets** | [**[SupportTicket]**](SupportTicket.md) |  | 
**updated_at** | **datetime, none_type** | The time/date the Epic was updated. | 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


