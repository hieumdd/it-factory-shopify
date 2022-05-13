from shopify.pipeline import orders


pipelines = {
    i.table: i
    for i in [
        j.pipeline # type: ignore
        for j in [
            orders,
        ]
    ]
}
