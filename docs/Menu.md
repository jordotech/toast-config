# Menu

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast POS. | 
**entity_type** | **str** | The type of object this is. | 
**external_id** | **str** | External identifier string, prefixed by the naming authority. | [optional] 
**name** | **str** | The name of the menu as it appears in the Toast POS.  | [optional] 
**orderable_online** | **str** | Indicates whether restaurant customers can order the menu online. | [optional] 
**visibility** | **str** | Indicates where the menu is displayed and who can see it. ALL: Visible to everyone (servers and customers) POS_ONLY: Only visible to servers NONE: Hidden from everyone  | [optional] 
**groups** | [**list[ExternalReference]**](ExternalReference.md) | An array of the &lt;a href&#x3D;\&quot;#/definitions/MenuGroup\&quot;&gt;&#x60;MenuGroup&#x60;&lt;/a&gt; objects that are part of this menu.  | [optional] 
**images** | [**list[Image]**](Image.md) | A collection of images associated with the menu. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


