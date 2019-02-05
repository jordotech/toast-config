# MenuItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast POS. | 
**entity_type** | **str** | The type of object this is. | 
**external_id** | **str** | External identifier string, prefixed by the naming authority. | [optional] 
**name** | **str** | The name of the menu item as it appears in the Toast POS.  | [optional] 
**sku** | **str** | The stock keeping unit (SKU) code for the item. | [optional] 
**plu** | **str** | The price look up (PLU) code for the item. | [optional] 
**orderable_online** | **str** | Indicates the orderableOnline status of this item | [optional] 
**visibility** | **str** | The visibility of this item. ALL: Visible to everyone (servers and customers) POS_ONLY: Only visible to servers NONE: Hidden from everyone  | [optional] 
**type** | **str** | Specifies whether this item is a special request or other off-menu transaction. * &#x60;NONE&#x60; - a normal menu item or modifier. * &#x60;OPEN_ITEM&#x60; - an item that is not on a menu. * &#x60;SPECIAL_REQUEST&#x60; - a selection that is not an item. * &#x60;PORTION&#x60; - a division of a menu item used to apply modifiers separately to separate parts of an item. For example, one half of a pizza.  | [optional] 
**option_groups** | [**list[ExternalReference]**](ExternalReference.md) | An array of &#x60;ExternalReference&#x60; objects containing the identifiers of the &lt;a href&#x3D;\&quot;#/definitions/MenuOptionGroup\&quot;&gt;&#x60;MenuOptionGroup&#x60;s&lt;/a&gt; that contain modifiers applicable to this item. Does not include those inherited from the parent &#x60;MenuGroup&#x60;.  | [optional] 
**inherit_option_groups** | **bool** | True if this menu item inherits &lt;a href&#x3D;\&quot;#/definitions/MenuOptionGroup\&quot;&gt;&#x60;MenuOptionGroup&#x60;s&lt;/a&gt; from its parent &lt;a href&#x3D;\&quot;#/definitions/MenuGroup\&quot;&gt;&#x60;MenuGroup&#x60;&lt;/a&gt;.  | [optional] 
**images** | [**list[Image]**](Image.md) | An array of &lt;a href&#x3D;\&quot;#/definitions/Image\&quot;&gt;&#x60;Image&#x60;&lt;/a&gt; objects that are associated with the &#x60;MenuItem&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


