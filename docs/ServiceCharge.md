# ServiceCharge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast POS. | 
**entity_type** | **str** | The type of object this is. | 
**external_id** | **str** | External identifier string, prefixed by the naming authority. | [optional] 
**name** | **str** | The name of this service charge. | [optional] 
**amount_type** | **str** | The type of service charge. | [optional] 
**amount** | **float** | Amount in USD to be applied for &#x60;FIXED&#x60; type service charges. | [optional] 
**percent** | **float** | Percent fee to be applied for &#x60;PERCENT&#x60; type service charges, based on pre-discount check amount. Must be a number between 0 and 100.  | [optional] 
**criteria** | [**ServiceChargeCriteria**](ServiceChargeCriteria.md) | A reference to the ServiceChargeCriteria to determine if this service charge is applicable to a given check. See each ServiceChargeCriteria for details. | [optional] 
**gratuity** | **bool** | True if the service charge is a gratuity and is assigned to the owner of the check. | [optional] 
**taxable** | **bool** | True if tax should be applied to the service charge. | [optional] 
**applicable_taxes** | [**list[TaxRate]**](TaxRate.md) | A reference to the taxes applied to the service charge, if the service charge is taxable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


