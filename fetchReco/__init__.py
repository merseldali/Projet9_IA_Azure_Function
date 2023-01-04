import logging
import json

import azure.functions as func


def main(req: func.HttpRequest, recos: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not recos or len(recos) == 0:
        logging.warning("User not found")
        return func.HttpResponse(
            "User not found",
            status_code=422,
        )

    return func.HttpResponse(
        json.dumps(json.loads(recos[0].to_json())["articles"]),
        mimetype="application/json",
        status_code=200,
    )
