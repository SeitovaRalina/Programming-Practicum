"""Модуль логирования"""
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


async def log(response, method, request_body=None):
    """Логирование запросов и ответов"""
    logger.info(f"REQUEST METHOD: {method}")
    logger.info(f"REQUEST URL: {response.url}")
    logger.info(f"REQUEST HEADERS: {response.headers_array}")
    logger.info(f"REQUEST BODY: {request_body}")
    logger.info(f"STATUS CODE: {response.status}")
    logger.info(f"RESPONSE HEADERS: {response.headers}")
    logger.info(f"RESPONSE BODY: {await response.text()}\n.\n.")
