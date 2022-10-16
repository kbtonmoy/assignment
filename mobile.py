mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'}
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
for single_data in mobile_data['data']:
    name = single_data['name']
    price = single_data['price']
    made = single_data['made']
    bdt_price = round(float(single_data['price'].split()[0]) * mobile_data['exchnage_rate'])
    template_variation = [
        f'{name} is made in {made}. The price is {price} which is equivalent  to {bdt_price} BDT',
        f'Newly Released {name} is manufactured in {made}. You can buy it for {price} or {bdt_price} BDT',
    ]
    for template in template_variation:
        print(template)

