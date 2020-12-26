# -*- coding: utf-8 -*-
# Copyright 2018 Artyom Losev
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """POS: Pay SO & Invoices""",
    "summary": """Handle the payment process for Sale Orders/Invoices over Point of Sale""",
    "category": "Point of Sale",
    # "live_test_url": "http://apps.it-projects.info/shop/product/pos-invoice-pay?version=10.0",
    "images": ["images/pos_invoice_pay_main.png"],
    "version": "10.0.1.0.5",
    "application": False,
    "author": "IT-Projects LLC, Artyom Losev",
    "support": "apps@itpp.dev",
    "website": "https://it-projects.info/team/ArtyomLosev",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["sale", "pos_longpolling", "base_action_rule"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data.xml",
        "actions/ir_action_server.xml",
        "actions/base_action_rules.xml",
        "report/report.xml",
        "views.xml",
    ],
    "qweb": ["static/src/xml/pos.xml"],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
    "demo_title": "Pay Sale Orders & Invoices over POS",
    "demo_addons": [],
    "demo_addons_hidden": [],
    "demo_url": "pos-invoice-pay",
    "demo_summary": "Handle the payment process for Sale Orders/Invoices over Point of Sale",
    "demo_images": ["images/pos_invoice_pay_main.png"],
}
