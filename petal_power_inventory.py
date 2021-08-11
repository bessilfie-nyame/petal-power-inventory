##import codecademylib
import pandas as pd

inventory = pd.read_csv("inventory.csv")
# print(inventory.head(10))
staten_island = inventory.iloc[:10]
# print(staten_island.head())

product_request = staten_island.product_description 
# print(product_request.head())

seed_request = inventory[(inventory.location == "Brooklyn") &  (inventory.product_type == "seeds")]
print(seed_request)

set_in_stock = lambda quantity: True if quantity > 0 else False 
inventory["in_stock"] = inventory.quantity.apply(set_in_stock)
print(inventory.in_stock.head())

inventory["total_value"] = inventory.price * inventory.quantity
print(inventory.total_value.head())

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory["full_description"] = inventory.apply(combine_lambda, axis=1)
print(inventory.full_description.head())

