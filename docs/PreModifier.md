# PreModifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast POS. | 
**entity_type** | **str** | The type of object this is. | 
**name** | **str** | The name of the pre modifier that appears in the Toast POS. | [optional] 
**scale_price** | **bool** | True if this multiplies the modifier price, false if it adds to the modifier price. | [optional] 
**base_price** | **float** | Amount to add to the modifier price, if scalePrice is false. Otherwise not used. | [optional] 
**scale_factor** | **float** | Amount to multiply the modifier price, if scalePrice is true. Otherwise not used. | [optional] 
**display_mode** | **str** | Where this premodifier should be displayed relative to the modifier name. PREFIX - before the modifier name SUFFIX - after the modifier name  | [optional] 
**parent** | [**ToastReference**](ToastReference.md) | The pre modifier group the premodifier belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


