# -*- coding: utf-8 -*-
{
    "name": """POS Mobile UI""",
    "summary": """Your Point of Sale in the Mobile Version""",
    "category": "Point of Sale",
    # "live_test_url": "http://apps.it-projects.info/shop/product/pos-mobile-ui?version=10.0",
    "images": ["images/pos_mobile.png"],
    "version": "10.0.1.2.0",
    "application": False,
    "author": "IT-Projects LLC, Dinar Gabbasov",
    "support": "pos@it-projects.info",
    "website": "https://it-projects.info/team/GabbasovDinar",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["point_of_sale", "pos_debranding"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/pos_mobile_template.xml", "views/pos_mobile_view.xml"],
    "qweb": ["static/src/xml/pos.xml"],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
    "demo_title": "POS Mobile UI",
    "demo_addons": ["pos_mobile_restaurant"],
    "demo_addons_hidden": [],
    "demo_url": "pos-mobile-ui",
    "demo_summary": "Mobile screen support for POSes and Restaurants",
    "demo_images": ["images/pos_mobile.png"],
}
