from typing import Optional, Union

from compose import compose

from shopify import shopify_repo
from db.bigquery import get_last_timestamp, load
from shopify.pipeline import interface


def pipeline_service(
    pipeline: interface.Pipeline,
    shop: interface.Shop,
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
