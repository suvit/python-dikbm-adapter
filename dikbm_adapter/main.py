# -*- coding: utf-8 -*-
import logging

from lockfile import FileLock, AlreadyLocked, LockFailed

from client import DiKBMClient
from settings import settings

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Starting DiKBM python client')
    try:
        client = DiKBMClient()
    except:
        logger.exception('Connect Error')
    else:
        lock = FileLock("dikbm")
        try:
            lock.acquire(0)
        except AlreadyLocked:
            logger.info('lock %s already locked' % lock)
        except LockFailed:
            logger.info('lock %s cant be locked' % lock)
        else:
            logger.info('lock %s acquired' % lock)
            try:
                client.proceed_in()
                client.proceed_status()
            except:
                logger.exception('Proceed Error')
            finally:
                lock.release()
                logger.info('lock %s released' % lock)
    finally:
        logger.info('Finished DiKMM python client')
