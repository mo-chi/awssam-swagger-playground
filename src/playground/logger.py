import os
import logging


# Lambda/Python Logger について
# SEE: https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/python-logging.html
# SEE: https://docs.python.org/ja/3.9/library/logging.html
log = logging.getLogger(__name__)

name = os.environ.get("LOG_LEVEL", logging.INFO)
level = logging.getLevelName(name)
log.setLevel(level)
