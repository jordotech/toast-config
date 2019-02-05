# TaxRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast POS. | 
**entity_type** | **str** | The type of object this is. | 
**name** | **str** | The name of this tax rate. | [optional] 
**is_default** | **bool** | True if this tax rate is the default tax rate. | [optional] 
**rate** | **float** | The tax rate, which could be a fixed amount, a percentage, or null if the tax rate type is &#x60;NONE&#x60;. | [optional] 
**type** | **str** | The type of the tax rate. | [optional] 
**rounding_type** | **str** | The method used to round fractional currency amounts to non-fractional currency amounts. If a tax rate is not a &#x60;PERCENT&#x60; type, this value is null. | [optional] 
**tax_table** | [**list[TaxTableRow]**](TaxTableRow.md) | An array of &#x60;TaxTableRow&#x60; objects that define a set of tax amounts that apply to specific sale amount ranges. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


