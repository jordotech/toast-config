# swagger_client.DefaultApi

All URIs are relative to *https://localhost/config/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alternate_payment_types_get**](DefaultApi.md#alternate_payment_types_get) | **GET** /alternatePaymentTypes | Returns an array of alternative forms of payment configured for a restaurant. 
[**alternate_payment_types_guid_get**](DefaultApi.md#alternate_payment_types_guid_get) | **GET** /alternatePaymentTypes/{guid} | Returns information about an alternative form of payment configured for a restaurant. 
[**cash_drawers_get**](DefaultApi.md#cash_drawers_get) | **GET** /cashDrawers | Returns an array of information about cash drawers configured for a restaurant. 
[**cash_drawers_guid_get**](DefaultApi.md#cash_drawers_guid_get) | **GET** /cashDrawers/{guid} | Returns information about a specific cash drawer device. 
[**dining_options_get**](DefaultApi.md#dining_options_get) | **GET** /diningOptions | Returns an array of information about types of service offered by a restaurant. 
[**dining_options_guid_get**](DefaultApi.md#dining_options_guid_get) | **GET** /diningOptions/{guid} | Returns information about a specific type of service offered by a restaurant. 
[**discounts_get**](DefaultApi.md#discounts_get) | **GET** /discounts | Returns an array of information about price deductions configured for a restaurant. 
[**discounts_guid_get**](DefaultApi.md#discounts_guid_get) | **GET** /discounts/{guid} | Returns information about a price deduction configured for a restaurant. 
[**menu_groups_get**](DefaultApi.md#menu_groups_get) | **GET** /menuGroups | Returns an array of information about the sections of menus configured for a restaurant. 
[**menu_groups_guid_get**](DefaultApi.md#menu_groups_guid_get) | **GET** /menuGroups/{guid} | Returns information about a section within a menu. 
[**menu_items_get**](DefaultApi.md#menu_items_get) | **GET** /menuItems | Returns information about the items and modifiers available from a restaurant. 
[**menu_items_guid_get**](DefaultApi.md#menu_items_guid_get) | **GET** /menuItems/{guid} | Returns information about an item or modifier available from a restaurant. 
[**menu_option_groups_get**](DefaultApi.md#menu_option_groups_get) | **GET** /menuOptionGroups | Returns information about the groups of modifier menu items configured for a restaurant. 
[**menu_option_groups_guid_get**](DefaultApi.md#menu_option_groups_guid_get) | **GET** /menuOptionGroups/{guid} | Returns information about a group of modifier menu items. 
[**menus_get**](DefaultApi.md#menus_get) | **GET** /menus | Returns information about the menus configured for a restaurant. 
[**menus_guid_get**](DefaultApi.md#menus_guid_get) | **GET** /menus/{guid} | Returns information about a menu configured for a restaurant. 
[**no_sale_reasons_get**](DefaultApi.md#no_sale_reasons_get) | **GET** /noSaleReasons | Returns information about no sale reasons configured for a restaurant. 
[**no_sale_reasons_guid_get**](DefaultApi.md#no_sale_reasons_guid_get) | **GET** /noSaleReasons/{guid} | Returns information about a no sale reason configured for a restaurant. 
[**payout_reasons_get**](DefaultApi.md#payout_reasons_get) | **GET** /payoutReasons | Returns information about recurring cash expenses configured for a restaurant. 
[**payout_reasons_guid_get**](DefaultApi.md#payout_reasons_guid_get) | **GET** /payoutReasons/{guid} | Returns information about a recurring cash expense configured for a restaurant. 
[**pre_modifier_groups_get**](DefaultApi.md#pre_modifier_groups_get) | **GET** /preModifierGroups | Returns information about pre modifier groups configured for a restaurant. 
[**pre_modifier_groups_guid_get**](DefaultApi.md#pre_modifier_groups_guid_get) | **GET** /preModifierGroups/{guid} | Returns information about a pre modifier group configured for a restaurant. 
[**pre_modifiers_get**](DefaultApi.md#pre_modifiers_get) | **GET** /preModifiers | Returns information about pre modifiers configured for a restaurant. 
[**pre_modifiers_guid_get**](DefaultApi.md#pre_modifiers_guid_get) | **GET** /preModifiers/{guid} | Returns information about a pre modifier configured for a restaurant. 
[**price_groups_get**](DefaultApi.md#price_groups_get) | **GET** /priceGroups | Returns information about the variable price levels configured for items at a restaurant. 
[**price_groups_guid_get**](DefaultApi.md#price_groups_guid_get) | **GET** /priceGroups/{guid} | Returns information about a variable price level configured for items at a restaurant. 
[**printers_get**](DefaultApi.md#printers_get) | **GET** /printers | Returns information about the printer devices configured for a restaurant. 
[**printers_guid_get**](DefaultApi.md#printers_guid_get) | **GET** /printers/{guid} | Returns information about a printer device configured for a restaurant. 
[**restaurant_services_get**](DefaultApi.md#restaurant_services_get) | **GET** /restaurantServices | Returns information about the types of menu and dining offered by a restaurant. 
[**restaurant_services_guid_get**](DefaultApi.md#restaurant_services_guid_get) | **GET** /restaurantServices/{guid} | Returns information about a type of menu and dining offered by a restaurant. 
[**revenue_centers_get**](DefaultApi.md#revenue_centers_get) | **GET** /revenueCenters | Returns information about segments of restaurant income, for reporting. 
[**revenue_centers_guid_get**](DefaultApi.md#revenue_centers_guid_get) | **GET** /revenueCenters/{guid} | Returns information about a segment of restaurant income, for reporting. 
[**sales_categories_get**](DefaultApi.md#sales_categories_get) | **GET** /salesCategories | Returns information about types of menu item used to analyze purchases at a restaurant. 
[**sales_categories_guid_get**](DefaultApi.md#sales_categories_guid_get) | **GET** /salesCategories/{guid} | Returns information about a type of menu item used to analyze purchases at a restaurant. 
[**service_areas_get**](DefaultApi.md#service_areas_get) | **GET** /serviceAreas | Returns information about the physical settings that a restaurant serves customers in. 
[**service_areas_guid_get**](DefaultApi.md#service_areas_guid_get) | **GET** /serviceAreas/{guid} | Returns information about a physical setting that a restaurant serves customers in. 
[**service_charges_get**](DefaultApi.md#service_charges_get) | **GET** /serviceCharges | Returns information about the types of fees applied to restaurant sales. 
[**service_charges_guid_get**](DefaultApi.md#service_charges_guid_get) | **GET** /serviceCharges/{guid} | Returns information about a type of fee applied to restaurant sales. 
[**tables_get**](DefaultApi.md#tables_get) | **GET** /tables | Returns information about the dining tables configured for a restaurant. 
[**tables_guid_get**](DefaultApi.md#tables_guid_get) | **GET** /tables/{guid} | Returns information about a dining table configured for a restaurant. 
[**tax_rates_get**](DefaultApi.md#tax_rates_get) | **GET** /taxRates | Returns information about the forms of taxation applied to sales at a restaurant. 
[**tax_rates_guid_get**](DefaultApi.md#tax_rates_guid_get) | **GET** /taxRates/{guid} | Returns information about a form of taxation applied to sales at a restaurant. 
[**void_reasons_get**](DefaultApi.md#void_reasons_get) | **GET** /voidReasons | Returns information about the causes for making a sale invalid configured for a restaurant. 


# **alternate_payment_types_get**
> list[AlternatePaymentType] alternate_payment_types_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns an array of alternative forms of payment configured for a restaurant. 

Returns an array of <a href=\"#/definitions/AlternatePaymentType\">`AlternatePaymentType`</a> objects containing information about alternative forms of payment that are configured for a restaurant. Alternate payment types are forms of payment that are not standard in the Toast POS and that are configured for a particular restaurant. For example, a third-party service that processes payments might be configured as an alternate payment type. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns an array of alternative forms of payment configured for a restaurant. 
    api_response = api_instance.alternate_payment_types_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->alternate_payment_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[AlternatePaymentType]**](AlternatePaymentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alternate_payment_types_guid_get**
> AlternatePaymentType alternate_payment_types_guid_get(toast_restaurant_external_id, guid)

Returns information about an alternative form of payment configured for a restaurant. 

Returns an <a href=\"#/definitions/AlternatePaymentType\">`AlternatePaymentType`</a> object containing information about an alternative form of payment configured for a restaurant. Alternate payment types are forms of payment that are not standard in the Toast POS and that are configured for a particular restaurant. For example, a third-party service that processes payments might be configured as an alternate payment type. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the alternate payment type is configured for. 
guid = 'guid_example' # str | The Toast POS GUID of the alternative form of payment.

try: 
    # Returns information about an alternative form of payment configured for a restaurant. 
    api_response = api_instance.alternate_payment_types_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->alternate_payment_types_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the alternate payment type is configured for.  | 
 **guid** | **str**| The Toast POS GUID of the alternative form of payment. | 

### Return type

[**AlternatePaymentType**](AlternatePaymentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_drawers_get**
> list[CashDrawer] cash_drawers_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns an array of information about cash drawers configured for a restaurant. 

Returns an array of <a href=\"#/definitions/CashDrawer\">`CashDrawer`</a> objects containing information about the cash drawer devices for the restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns an array of information about cash drawers configured for a restaurant. 
    api_response = api_instance.cash_drawers_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cash_drawers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[CashDrawer]**](CashDrawer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_drawers_guid_get**
> CashDrawer cash_drawers_guid_get(toast_restaurant_external_id, guid)

Returns information about a specific cash drawer device. 

Returns a <a href=\"#/definitions/CashDrawer\">`CashDrawer`</a> object containing information about a specific cash drawer device. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the cash drawer.

try: 
    # Returns information about a specific cash drawer device. 
    api_response = api_instance.cash_drawers_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cash_drawers_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the cash drawer. | 

### Return type

[**CashDrawer**](CashDrawer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dining_options_get**
> list[DiningOption] dining_options_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns an array of information about types of service offered by a restaurant. 

Returns an array of <a href=\"#/definitions/DiningOption\">`DiningOption`</a> objects containing information about types of service offered by a restaurant. For example, dine in, take out, and delivery might be dining options for a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns an array of information about types of service offered by a restaurant. 
    api_response = api_instance.dining_options_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dining_options_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[DiningOption]**](DiningOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dining_options_guid_get**
> DiningOption dining_options_guid_get(toast_restaurant_external_id, guid)

Returns information about a specific type of service offered by a restaurant. 

Returns a <a href=\"#/definitions/DiningOption\">`DiningOption`</a> object containing information about a type of service offered by a restaurant. For example, dine in, take out, and delivery might be dining options for a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the dining option.

try: 
    # Returns information about a specific type of service offered by a restaurant. 
    api_response = api_instance.dining_options_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dining_options_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the dining option. | 

### Return type

[**DiningOption**](DiningOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discounts_get**
> list[Discount] discounts_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns an array of information about price deductions configured for a restaurant. 

Returns an array of <a href=\"#/definitions/Discount\">`Discount`</a> objects containing information about the price deductions configured for a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns an array of information about price deductions configured for a restaurant. 
    api_response = api_instance.discounts_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->discounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[Discount]**](Discount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discounts_guid_get**
> Discount discounts_guid_get(toast_restaurant_external_id, guid)

Returns information about a price deduction configured for a restaurant. 

Returns a <a href=\"#/definitions/Discount\">`Discount`</a> object containing information about a price deduction configured for a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the discount.

try: 
    # Returns information about a price deduction configured for a restaurant. 
    api_response = api_instance.discounts_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->discounts_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the discount. | 

### Return type

[**Discount**](Discount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **menu_groups_get**
> list[MenuGroup] menu_groups_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns an array of information about the sections of menus configured for a restaurant. 

Returns an array of <a href=\"#/definitions/MenuGroup\">`MenuGroup`</a> objects containing information about the subsections of the menus configured for a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns an array of information about the sections of menus configured for a restaurant. 
    api_response = api_instance.menu_groups_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->menu_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[MenuGroup]**](MenuGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **menu_groups_guid_get**
> MenuGroup menu_groups_guid_get(toast_restaurant_external_id, guid)

Returns information about a section within a menu. 

Returns a <a href=\"#/definitions/MenuGroup\">`MenuGroup`</a> object containing information about a section within a menu. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the menu group.

try: 
    # Returns information about a section within a menu. 
    api_response = api_instance.menu_groups_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->menu_groups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the menu group. | 

### Return type

[**MenuGroup**](MenuGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **menu_items_get**
> list[MenuItem] menu_items_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the items and modifiers available from a restaurant. 

Returns an array of <a href=\"#/definitions/MenuItem\">`MenuItem`</a> objects containing information about the items and modifiers available from a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the items and modifiers available from a restaurant. 
    api_response = api_instance.menu_items_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->menu_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[MenuItem]**](MenuItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **menu_items_guid_get**
> MenuItem menu_items_guid_get(toast_restaurant_external_id, guid)

Returns information about an item or modifier available from a restaurant. 

Returns a <a href=\"#/definitions/MenuItem\">`MenuItem`</a> object containing information about an item or modifier available from a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID for the menu item.

try: 
    # Returns information about an item or modifier available from a restaurant. 
    api_response = api_instance.menu_items_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->menu_items_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID for the menu item. | 

### Return type

[**MenuItem**](MenuItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **menu_option_groups_get**
> list[MenuOptionGroup] menu_option_groups_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the groups of modifier menu items configured for a restaurant. 

Returns an array <a href=\"#/definitions/MenuOptionGroup\">`MenuOptionGroup`</a> objects containing information about groups of modifier menu items. For example, salad dressings might be a menu option group for a salad menu item. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the groups of modifier menu items configured for a restaurant. 
    api_response = api_instance.menu_option_groups_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->menu_option_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[MenuOptionGroup]**](MenuOptionGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **menu_option_groups_guid_get**
> MenuOptionGroup menu_option_groups_guid_get(toast_restaurant_external_id, guid)

Returns information about a group of modifier menu items. 

Returns a <a href=\"#/definitions/MenuOptionGroup\">`MenuOptionGroup`</a> object containing information about a group of modifier menu items. For example, salad dressings might be a menu option group for a salad menu item. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the menu option group.

try: 
    # Returns information about a group of modifier menu items. 
    api_response = api_instance.menu_option_groups_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->menu_option_groups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the menu option group. | 

### Return type

[**MenuOptionGroup**](MenuOptionGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **menus_get**
> list[Menu] menus_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the menus configured for a restaurant. 

Returns an array of <a href=\"#/definitions/Menu\">`Menu`</a> objects containing information about menus configured for a restaurant. For example, a restaurant might have drinks, dinner, and dessert menus. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the menus configured for a restaurant. 
    api_response = api_instance.menus_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->menus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[Menu]**](Menu.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **menus_guid_get**
> Menu menus_guid_get(toast_restaurant_external_id, guid)

Returns information about a menu configured for a restaurant. 

Returns a <a href=\"#/definitions/Menu\">`Menu`</a> object containing information about a menu configured for a restaurant. For example, a restaurant might have drinks, dinner, and dessert menus. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the menu.

try: 
    # Returns information about a menu configured for a restaurant. 
    api_response = api_instance.menus_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->menus_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the menu. | 

### Return type

[**Menu**](Menu.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **no_sale_reasons_get**
> list[NoSaleReason] no_sale_reasons_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about no sale reasons configured for a restaurant. 

Returns an array of <a href=\"#/definitions/NoSaleReason\">`NoSaleReason`</a> objects containing information about no sale reasons configured for a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about no sale reasons configured for a restaurant. 
    api_response = api_instance.no_sale_reasons_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->no_sale_reasons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[NoSaleReason]**](NoSaleReason.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **no_sale_reasons_guid_get**
> NoSaleReason no_sale_reasons_guid_get(toast_restaurant_external_id, guid)

Returns information about a no sale reason configured for a restaurant. 

Returns a <a href=\"#/definitions/NoSaleReason\">`NoSaleReason`</a> object containing information about a no sale reason. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the no sale reason.

try: 
    # Returns information about a no sale reason configured for a restaurant. 
    api_response = api_instance.no_sale_reasons_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->no_sale_reasons_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the no sale reason. | 

### Return type

[**NoSaleReason**](NoSaleReason.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payout_reasons_get**
> list[PayoutReason] payout_reasons_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about recurring cash expenses configured for a restaurant. 

Returns an array of <a href=\"#/definitions/PayoutReason\">`PayoutReason`</a> objects containing information about recurring cash expenses configured for a restaurant. For example, payment for services such as window washing might be payout reasons. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about recurring cash expenses configured for a restaurant. 
    api_response = api_instance.payout_reasons_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->payout_reasons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[PayoutReason]**](PayoutReason.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payout_reasons_guid_get**
> PayoutReason payout_reasons_guid_get(toast_restaurant_external_id, guid)

Returns information about a recurring cash expense configured for a restaurant. 

Returns a <a href=\"#/definitions/PayoutReason\">`PayoutReason`</a> object containing information about a recurring restaurant expense that is paid in cash. Payout reasons are pre-configured for a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the payout reason.

try: 
    # Returns information about a recurring cash expense configured for a restaurant. 
    api_response = api_instance.payout_reasons_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->payout_reasons_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the payout reason. | 

### Return type

[**PayoutReason**](PayoutReason.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_modifier_groups_get**
> list[PreModifierGroup] pre_modifier_groups_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about pre modifier groups configured for a restaurant. 

Returns an array of <a href=\"#/definitions/PreModifierGroup\">`PreModifierGroup`</a> objects containing information about PreModifierGroup configured for a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about pre modifier groups configured for a restaurant. 
    api_response = api_instance.pre_modifier_groups_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pre_modifier_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[PreModifierGroup]**](PreModifierGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_modifier_groups_guid_get**
> PreModifierGroup pre_modifier_groups_guid_get(toast_restaurant_external_id, guid)

Returns information about a pre modifier group configured for a restaurant. 

Returns a <a href=\"#/definitions/PreModifierGroup\">`PreModifierGroup`</a> object containing information about a pre modifier group. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the pre modifier.

try: 
    # Returns information about a pre modifier group configured for a restaurant. 
    api_response = api_instance.pre_modifier_groups_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pre_modifier_groups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the pre modifier. | 

### Return type

[**PreModifierGroup**](PreModifierGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_modifiers_get**
> list[PreModifier] pre_modifiers_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about pre modifiers configured for a restaurant. 

Returns an array of <a href=\"#/definitions/PreModifier\">`PreModifier`</a> objects containing information about PreModifiers configured for a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about pre modifiers configured for a restaurant. 
    api_response = api_instance.pre_modifiers_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pre_modifiers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[PreModifier]**](PreModifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_modifiers_guid_get**
> PreModifier pre_modifiers_guid_get(toast_restaurant_external_id, guid)

Returns information about a pre modifier configured for a restaurant. 

Returns a <a href=\"#/definitions/PreModifier\">`PreModifier`</a> object containing information about a pre modifier. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the pre modifier.

try: 
    # Returns information about a pre modifier configured for a restaurant. 
    api_response = api_instance.pre_modifiers_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pre_modifiers_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the pre modifier. | 

### Return type

[**PreModifier**](PreModifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **price_groups_get**
> list[PriceGroup] price_groups_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the variable price levels configured for items at a restaurant. 

Returns an array of <a href=\"#/definitions/PriceGroup\">`PriceGroup`</a> objects containing information about the variable price levels configured for items at a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the variable price levels configured for items at a restaurant. 
    api_response = api_instance.price_groups_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->price_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[PriceGroup]**](PriceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **price_groups_guid_get**
> PriceGroup price_groups_guid_get(toast_restaurant_external_id, guid)

Returns information about a variable price level configured for items at a restaurant. 

Returns a <a href=\"#/definitions/PriceGroup\">`PriceGroup`</a> object containing information about variable price levels configured for items at a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the price level.

try: 
    # Returns information about a variable price level configured for items at a restaurant. 
    api_response = api_instance.price_groups_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->price_groups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the price level. | 

### Return type

[**PriceGroup**](PriceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **printers_get**
> list[Printer] printers_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the printer devices configured for a restaurant. 

Returns an array of <a href=\"#/definitions/Printer\">`Printer`</a> objects containing information about the printer devices configured for a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the printer devices configured for a restaurant. 
    api_response = api_instance.printers_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->printers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[Printer]**](Printer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **printers_guid_get**
> Printer printers_guid_get(toast_restaurant_external_id, guid)

Returns information about a printer device configured for a restaurant. 

Returns a <a href=\"#/definitions/Printer\">`Printer`</a> object containing information about a printer device configured for a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the printer.

try: 
    # Returns information about a printer device configured for a restaurant. 
    api_response = api_instance.printers_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->printers_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the printer. | 

### Return type

[**Printer**](Printer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restaurant_services_get**
> list[RestaurantService] restaurant_services_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the types of menu and dining offered by a restaurant. 

Returns an array of <a href=\"#/definitions/RestaurantService\">`RestaurantService`</a> objects containing information about the types of menu and dining offered by a restaurant. For example, a restaurant might offer a lunch service at some hours of the day and a dinner service at other hours of the day. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the types of menu and dining offered by a restaurant. 
    api_response = api_instance.restaurant_services_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->restaurant_services_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[RestaurantService]**](RestaurantService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restaurant_services_guid_get**
> RestaurantService restaurant_services_guid_get(toast_restaurant_external_id, guid)

Returns information about a type of menu and dining offered by a restaurant. 

Returns a <a href=\"#/definitions/RestaurantService\">`RestaurantService`</a> object containing information about a type of menu and dining offered by a restaurant. For example, a restaurant might offer a lunch service at some hours of the day and a dinner service at other hours of the day. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the service.

try: 
    # Returns information about a type of menu and dining offered by a restaurant. 
    api_response = api_instance.restaurant_services_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->restaurant_services_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the service. | 

### Return type

[**RestaurantService**](RestaurantService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revenue_centers_get**
> list[RevenueCenter] revenue_centers_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about segments of restaurant income, for reporting. 

Returns an array of <a href=\"#/definitions/RevenueCenter\">`RevenueCenter`</a> objects containing information about segments of restaurant income, for reporting. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about segments of restaurant income, for reporting. 
    api_response = api_instance.revenue_centers_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->revenue_centers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[RevenueCenter]**](RevenueCenter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revenue_centers_guid_get**
> revenue_centers_guid_get(toast_restaurant_external_id, guid)

Returns information about a segment of restaurant income, for reporting. 

Returns a <a href=\"#/definitions/RevenueCenter\">`RevenueCenter`</a> object containing information about a segment of restaurant income, for reporting. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the revenue center.

try: 
    # Returns information about a segment of restaurant income, for reporting. 
    api_instance.revenue_centers_guid_get(toast_restaurant_external_id, guid)
except ApiException as e:
    print("Exception when calling DefaultApi->revenue_centers_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the revenue center. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_categories_get**
> list[SalesCategory] sales_categories_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about types of menu item used to analyze purchases at a restaurant. 

Returns an array of <a href=\"#/definitions/SalesCategory\">`SalesCategory`</a> objects containing information about the types of menu item used to analyze purchases at a restaurant. For example, food and alcohol might be sales categories for a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about types of menu item used to analyze purchases at a restaurant. 
    api_response = api_instance.sales_categories_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sales_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[SalesCategory]**](SalesCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_categories_guid_get**
> SalesCategory sales_categories_guid_get(toast_restaurant_external_id, guid)

Returns information about a type of menu item used to analyze purchases at a restaurant. 

Returns a <a href=\"#/definitions/SalesCategory\">`SalesCategory`</a> object containing information about a type of menu item used to analyze purchases at a restaurant. For example, food and alcohol might be sales categories for a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the sales category.

try: 
    # Returns information about a type of menu item used to analyze purchases at a restaurant. 
    api_response = api_instance.sales_categories_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sales_categories_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the sales category. | 

### Return type

[**SalesCategory**](SalesCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_areas_get**
> list[ServiceArea] service_areas_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the physical settings that a restaurant serves customers in. 

Returns an array of <a href=\"#/definitions/ServiceArea\">`ServiceArea`</a> objects containing information about the physical settings that a restaurant serves customers in. For example, a restaurant might serve customers in dining room and patio service areas. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the physical settings that a restaurant serves customers in. 
    api_response = api_instance.service_areas_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->service_areas_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[ServiceArea]**](ServiceArea.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_areas_guid_get**
> ServiceArea service_areas_guid_get(toast_restaurant_external_id, guid)

Returns information about a physical setting that a restaurant serves customers in. 

Returns a <a href=\"#/definitions/ServiceArea\">`ServiceArea`</a> object containing information about a physical setting that a restaurant serves customers in. For example, a restaurant might serve customers in dining room and patio service areas. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the service area.

try: 
    # Returns information about a physical setting that a restaurant serves customers in. 
    api_response = api_instance.service_areas_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->service_areas_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the service area. | 

### Return type

[**ServiceArea**](ServiceArea.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_charges_get**
> list[ServiceCharge] service_charges_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the types of fees applied to restaurant sales. 

Returns an array of <a href=\"#/definitions/ServiceCharge\">`ServiceCharge`</a> objects containing information about the types of fee applied to restaurant sales. For example, an automatic gratuity applied to the check for a large dining party might be a type of service charge for a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the types of fees applied to restaurant sales. 
    api_response = api_instance.service_charges_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->service_charges_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[ServiceCharge]**](ServiceCharge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_charges_guid_get**
> ServiceCharge service_charges_guid_get(toast_restaurant_external_id, guid)

Returns information about a type of fee applied to restaurant sales. 

Returns a <a href=\"#/definitions/ServiceCharge\">`ServiceCharge`</a> object containing information about a type of fee applied to restaurant sales. For example, an automatic gratuity applied to the check for a large dining party might be a type of service charge for a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the service charge.

try: 
    # Returns information about a type of fee applied to restaurant sales. 
    api_response = api_instance.service_charges_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->service_charges_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the service charge. | 

### Return type

[**ServiceCharge**](ServiceCharge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tables_get**
> list[Table] tables_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the dining tables configured for a restaurant. 

Returns an array of <a href=\"#/definitions/Table\">`Table`</a> objects containing information about the dining tables configured for a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the dining tables configured for a restaurant. 
    api_response = api_instance.tables_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[Table]**](Table.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tables_guid_get**
> Table tables_guid_get(toast_restaurant_external_id, guid)

Returns information about a dining table configured for a restaurant. 

Returns a <a href=\"#/definitions/Table\">`Table`</a> object containing information about a dining table configured for a restaurant.  

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the table.

try: 
    # Returns information about a dining table configured for a restaurant. 
    api_response = api_instance.tables_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tables_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the table. | 

### Return type

[**Table**](Table.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_rates_get**
> list[TaxRate] tax_rates_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the forms of taxation applied to sales at a restaurant. 

Returns an array of <a href=\"#/definitions/TaxRate\">`TaxRate`</a> objects containing information about the forms of taxation applied to sales at a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the forms of taxation applied to sales at a restaurant. 
    api_response = api_instance.tax_rates_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tax_rates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[TaxRate]**](TaxRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_rates_guid_get**
> TaxRate tax_rates_guid_get(toast_restaurant_external_id, guid)

Returns information about a form of taxation applied to sales at a restaurant. 

Returns a <a href=\"#/definitions/TaxRate\">`TaxRate`</a> object containing information about a form of taxation applied to sales at a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
guid = 'guid_example' # str | The Toast POS GUID of the tax rate.

try: 
    # Returns information about a form of taxation applied to sales at a restaurant. 
    api_response = api_instance.tax_rates_guid_get(toast_restaurant_external_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tax_rates_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the tax rate. | 

### Return type

[**TaxRate**](TaxRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_reasons_get**
> list[VoidReason] void_reasons_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)

Returns information about the causes for making a sale invalid configured for a restaurant. 

Returns an array of <a href=\"#/definitions/VoidReason\">`VoidReason`</a> objects containing information about causes for making a sale invalid configured for a restaurant. If a `lastModified` date is specified, returns all objects that were created or modified after that date. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
page_size = 56 # int | The number of objects to return in the array. 
page = 56 # int | The sequence number of the first object to return in the array.  (optional)
last_modified = '2013-10-20' # date | Limits the return data to objects created or modified after a specific date and time. For example: `2015-12-01T00:00:00.000+0000`.  (optional)

try: 
    # Returns information about the causes for making a sale invalid configured for a restaurant. 
    api_response = api_instance.void_reasons_get(toast_restaurant_external_id, page_size, page=page, last_modified=last_modified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->void_reasons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_size** | **int**| The number of objects to return in the array.  | 
 **page** | **int**| The sequence number of the first object to return in the array.  | [optional] 
 **last_modified** | **date**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2015-12-01T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**list[VoidReason]**](VoidReason.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

