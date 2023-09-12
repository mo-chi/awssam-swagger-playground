from playground.logger import log
from http import HTTPStatus
import base64
import io
import cgi


def parse_multipart(body, content_type, content_length):
    decode = base64.b64decode(body)

    fp = io.BytesIO(decode)

    fs = cgi.FieldStorage(
        fp=fp,
        headers={
            "content-type": content_type,
            "content-length": content_length,
        },
        environ={
            "REQUEST_METHOD": "POST"
        }
    )

    return fs.list


def lambda_handler(event, context):
    """POST API 用 Lambda 関数"""
    log.debug(f"event: {event}")

    try:
        # イベント情報は API Gateway の POST > 統合リクエスト > マッピングテンプレートと対にする
        body = event["body"]
        headers = event["headers"]

        parts = parse_multipart(body, headers["content-type"], headers["content-length"])
        for p in parts:
            log.debug(f"name: {p.name}, filename: {p.filename}, type: {p.type}, value: {p.value}")

        # -------------------------------------------------
        # S3 へ CSV ファイルのアップロードや DynamoDB へ登録など
        # -------------------------------------------------
    except Exception as e:
        log.error(f"failed error: {e}")
        return {
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
            "error": {
                "message": "サーバ側でエラーが発生しデータの登録に失敗しました",
            }
        }

    return None
