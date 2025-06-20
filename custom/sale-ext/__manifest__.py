{
    'name': 'Hello World Sale Extension',
    'version': '1.0',
    'summary': 'Adds a transaction number to sale orders',
    'depends': ['sale', 'sale_management'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
}
