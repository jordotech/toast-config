# ServiceChargeCriteria

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_check_amount** | **float** | The service charge is only applicable if the pre-discount check is at least this amount. | [optional] 
**delivery** | **bool** | True if the service charge is only applicable for deliveries. | [optional] 
**max_check_amount** | **float** | The service charge is waived if the pre-discount check amount is more than this amount. A &#x60;null&#x60; value means this criteria is inapplicable. | [optional] 
**min_delivery_distance** | **float** | The service charge is only applicable to deliveries that are at least this distance. A &#x60;null&#x60; value means this criteria is inapplicable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


