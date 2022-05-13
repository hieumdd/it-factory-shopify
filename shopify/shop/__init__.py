import os

from shopify.pipeline import interface


shops = {
    i.shop_url: i
    for i in [
        interface.Shop(
            "ItFactory",
            "itfactoryca",
            os.getenv("IT_FACTORY_TOKEN", ""),
        ),
    ]
}
