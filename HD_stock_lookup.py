import requests
from bs4 import BeautifulSoup
import csv
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0'}

stores = ['7073', '7129', '7012', '7013', '7134', '7107',
          '7080', '7027', '7078', '7114', '7301', '7006',
          '7130', '7132', '7011', '7112', '7003', '7253',
          '7106', '7161', '7004', '7269', '7241', '7157',
          '7115', '7021', '7007', '7256', '7008',
          '7136', '7238', '7109', '7005', '7249', '7123']

skus = [str(
    input("Enter the SKU number (seperate them by comma, space for multiple): "))]


def stock_get():

  for store in stores:

    for sku in skus:

      product_url = "https://www.homedepot.ca/homedepotcacommercewebservices/v2/homedepotca/products/{}/localized/{}?fields=BASIC_SPA".format(
          sku.strip(), store)

      session = requests.Session()

      product_url_response = session.get(product_url, headers=headers)

      jsn_resp = product_url_response.json()

      store_id = jsn_resp['aisleBay']['storeDisplayName']

      stock_level = jsn_resp['storeStock']['stockLevel']

      print(store, store_id, sku, stock_level)

    print("")


stock_get()

