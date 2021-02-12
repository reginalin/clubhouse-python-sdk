# StorySearchResults

The results of the Story search query.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**[Story]**](Story.md) | A list of search results. | 
**next** | **str, none_type** | The URL path and query string for the next page of search results. | 
**total** | **int** | The total number of matches for the search query. The first 1000 matches can be paged through via the API. | 
**cursors** | **[str]** |  | [optional] 
**any string name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


