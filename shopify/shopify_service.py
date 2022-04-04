from typing import Optional, Union
import os

from compose import compose

from shopify import shopify, shopify_repo, orders
from db.bigquery import get_last_timestamp, load

pipelines = {
    i.table: i
    for i in [
        orders.orders,
    ]
}

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


def pipeline_service(
    pipeline: shopify.Pipeline,
    shop: shopify.Shop,
    start: Optional[str],
    end: Optional[str],
) -> dict[str, Union[str, int]]:
    return compose(
        lambda x: {
            "table": pipeline.table,
            "shop_url": shop.shop_url,
            "start": start,
            "end": end,
            "output_rows": x,
        },
        load(
            pipeline.table,
            pipeline.schema,
            pipeline.id_key,
            pipeline.cursor_key,
        ),
        pipeline.transform,
        shopify_repo.get(pipeline.resource, shop),
        get_last_timestamp(pipeline.table, pipeline.cursor_key),
    )((start, end))
