# -*- coding: utf-8 -*-
import logging
from client import DiKBMClient
from settings import settings

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    try:
        client = DiKBMClient()

        client.proceed_in()
        client.proceed_status()
    except:
        logger.error('error')
        raise
