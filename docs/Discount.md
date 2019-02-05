# Discount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast POS. | 
**entity_type** | **str** | The type of object this is. | 
**name** | **str** | The human-readable name of the discount. | [optional] 
**active** | **bool** | True if this discount is currently usable. | [optional] 
**type** | **str** | * &#x60;PERCENT&#x60; - the discount reduces the price by a percentage. * &#x60;FIXED&#x60; - the discount reduces the price by a specific amount.  | [optional] 
**percentage** | **float** | Percent discount applied when the &#x60;amountType&#x60; is &#x60;PERCENT&#x60;. This value will be greater than 0 and at most 100.  | [optional] 
**amount** | **float** | The currency amount of the discount when the &#x60;amountType&#x60; is &#x60;FIXED&#x60;. This value will be greater than 0.  | [optional] 
**selection_type** | **str** | * &#x60;CHECK&#x60; - the discount can be applied to a check. * &#x60;BOGO&#x60; - a buy one get one (BOGO) discount. * &#x60;ITEM&#x60; - the discount can be applied to an item selection in a check.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


