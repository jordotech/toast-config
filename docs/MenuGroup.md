# MenuGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast POS. | 
**entity_type** | **str** | The type of object this is. | 
**external_id** | **str** | External identifier string, prefixed by the naming authority. | [optional] 
**name** | **str** | The name of the menu group as it appears in the Toast POS. | [optional] 
**menu** | [**ExternalReference**](ExternalReference.md) | The Toast GUID or external identifier of the menu that this group belongs to.  | [optional] 
**orderable_online** | **str** | Indicates the orderableOnline status of this group | [optional] 
**visibility** | **str** | The visibility of this group. ALL: Visible to everyone (servers and customers) POS_ONLY: Only visible to servers NONE: Hidden from everyone  | [optional] 
**parent** | [**ExternalReference**](ExternalReference.md) | The Toast GUID or external identifier of the menu group that is the direct parent of the current menu group. This value is &#x60;null&#x60; if direct parent of the menu group is a menu.  | [optional] 
**items** | [**list[ExternalReference]**](ExternalReference.md) | An array of &#x60;ExternalReference&#x60; objects containing the identifiers of the &lt;a href&#x3D;\&quot;#/definitions/MenuItem\&quot;&gt;&#x60;MenuItem&#x60;s&lt;/a&gt; in the menu group.  | [optional] 
**subgroups** | [**list[ExternalReference]**](ExternalReference.md) | An array of &#x60;ExternalReference&#x60; objects containing the identifiers of the child &lt;a href&#x3D;\&quot;#/definitions/MenuGroup\&quot;&gt;&#x60;MenuGroup&#x60;s&lt;/a&gt; in the menu group. Empty if the menu group does not include any child menu groups.  | [optional] 
**option_groups** | [**list[ExternalReference]**](ExternalReference.md) | An array of &#x60;ExternalReference&#x60; objects containing the identifiers of the child &lt;a href&#x3D;\&quot;#/definitions/MenuOptionGroup\&quot;&gt;&#x60;MenuOptionGroup&#x60;s&lt;/a&gt; that contain modifiers applicable to the group, its subgroups and its items. Does not include &#x60;MenuOptionGroup&#x60;s inherited from its parent &#x60;MenuGroup&#x60;.  | [optional] 
**inherit_option_groups** | **bool** | True if this &#x60;MenuGroup&#x60; inherits &lt;a href&#x3D;\&quot;#/definitions/MenuOptionGroup\&quot;&gt;&#x60;MenuOptionGroup&#x60;s&lt;/a&gt; from its parent &#x60;MenuGroup&#x60;.    | [optional] 
**images** | [**list[Image]**](Image.md) | An array of &lt;a href&#x3D;\&quot;#/definitions/Image\&quot;&gt;&#x60;Image&#x60;&lt;/a&gt; objects associated with with the &#x60;MenuGroup&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


