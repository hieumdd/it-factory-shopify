from shopify.shop import shops
from shopify.pipeline import pipelines
from tasks import cloud_tasks


def tasks_service(body: dict[str, str]):
    return {
        "tasks": cloud_tasks.create_tasks(
            [
                {
                    "resource": p,
                    "shop": s,
                    "start": body.get("start"),
                    "end": body.get("end"),
                }
                for p in pipelines.keys()
                for s in shops.keys()
            ],
            lambda x: f"{x['resource']}-{x['shop']}",
        )
    }
