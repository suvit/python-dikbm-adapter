# -*- coding: utf-8 -*-
import logging

from lockfile import FileLock, AlreadyLocked, LockFailed

from client import DiKBMClient
from settings import settings

logger = logging.getLogger(__name__)


def main():
    logger.info('Starting DiKBM python client')

    lock = FileLock("dikbm")
    try:
        lock.acquire(0)
    except AlreadyLocked:
        logger.info('lock %s already locked' % lock.unique_name)
    except LockFailed:
        logger.error('lock %s cant be locked' % lock.unique_name)
    else:
        logger.debug('lock %s acquired' % lock.unique_name)

        try:
            client = DiKBMClient()
        except:
            logger.exception('Connect Error')
        else:
            try:
                client.proceed_in()
                client.proceed_status()
            except:
                logger.exception('Proceed Error')
        finally:
            lock.release()
            logger.debug('lock %s released' % lock.unique_name)
    finally:
        logger.info('Finished DiKBM python client')

if __name__ == '__main__':
    main()
