for store in stores:
    for sku in input_skus:
        product_url = "https://www.homedepot.ca/homedepotcacommercewebservices/v2/homedepotca/products/{}/localized/{}?fields=BASIC_SPA".format(sku, store)
        session = requests.Session()
        product_url_response = session.get(product_url, headers=headers)
        jsn_resp = product_url_response.json()
        store_id = jsn_resp['aisleBay']['storeDisplayName']
        stock_level = jsn_resp['storeStock']['stockLevel']
    return (store, store_id, stock_level)


    print('hi')