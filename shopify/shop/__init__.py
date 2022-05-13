import os

from shopify import shopify


shops = {
    i.shop_url: i
    for i in [
        shopify.Shop(
            "ItFactory",
            "itfactoryca",
            os.getenv("IT_FACTORY_TOKEN", ""),
        ),
    ]
}
