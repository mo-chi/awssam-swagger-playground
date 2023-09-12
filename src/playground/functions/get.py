from playground.logger import log
from http import HTTPStatus
import json


def lambda_handler(event, context):
    """GET API 用 Lambda 関数"""
    log.debug(f"event: {event}")

    # -------------------------------------------------
    # DynamoDB からのデータ取得など
    # -------------------------------------------------

    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps({
            "message": "successful"
        }),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "isBase64Encoded": False
    }
