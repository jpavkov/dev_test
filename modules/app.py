from ecommerce.shopping import sales
import sys
# print(sys.path)

print(dir(sales))

print(sales.__name__)
print(sales.__package__)
print(sales.__file__)


# from sales import calc_shipping, calc_tax

# # import sales
# # sales.calc_shipping
# # sales.calc_tax

# calc_shipping()
# calc_tax()

# if in different folder:
# from modules.ecommerce.shipping.salesimport calc_tax, calc_shipping
# from modules.ecommerce.shipping import sales

# sales.calc_tax
