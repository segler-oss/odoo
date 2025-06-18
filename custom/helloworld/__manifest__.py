# helloworld/__manifest__.py
{
    'name': 'Hello World Route',
    'version': '1.0',
    'summary': 'Einfaches Modul mit einer /helloworld Route',
    'author': 'Dein Name',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'views/actions.xml'
    ],
    'installable': True,
    'application': True,
}
