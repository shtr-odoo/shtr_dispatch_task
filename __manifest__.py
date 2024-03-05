{
    'name': 'Stock Transport',
    'depends': ['fleet',
                'stock',
                'stock_picking_batch'
                ],
    "auto_install": True,
    'data': [
        'security/ir.model.access.csv',
        'views/stock_transport_view.xml',
        'views/inventory_batch_view.xml',
        'views/stock_picking_view.xml',
        'views/batch_graph_view.xml'
    ]
}