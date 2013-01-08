# -*- coding: utf-8 -*-
import os
import base64
import logging
import shutil

from suds.client import Client
from suds.wsse import Security

from suds_passworddigest.token import UsernameDigestToken

from settings import settings

logger = logging.getLogger(__name__)

class DiKBMClient(object):
    def __init__(self):
        self.kbm_client = Client(settings.kbmto_url)

        security = Security()
        token = UsernameDigestToken(settings.username,
                                    settings.password)
        security.tokens.append(token)
        self.kbm_client.set_options(wsse=security)

    def proceed_dir(self, dirname):
        for filename in os.listdir(dirname):
            file_path = os.path.join(dirname, filename)
            if not os.path.isfile(file_path):
                logger.debug('skip not file %s' % file_path)
                continue

            name, ext = os.path.splitext(filename)
            if not ext.lower() == '.xml':
                logger.error('skip not xml file %s' % filename)
                self.proceed_error(file_path)
                continue

            try:
                operation, uid = name.split('_', 1)
            except ValueError:
                logger.error('bad file name %s' % filename)
                self.proceed_error(file_path)
                continue

            logger.info('proceed %s %s %s' % (filename, operation, uid))

            if operation in ['kbm']:
                response = self.request_kbm(file_path)
                logger.info('catch response for %s' % filename)
                self.response_kbm(filename, response)

                logger.info('delete %s' % file_path)
                os.remove(file_path)
            else:
                logger.error('unknown operation %s for %s' % (operation,
                                                              filename))
                self.proceed_error(file_path)

    def proceed_in(self):
        self.proceed_dir(settings.in_dir)

    def proceed_status(self):
        self.proceed_dir(settings.status_dir)

    def request_kbm(self, filepath):
        attachment = self.kbm_client.factory.create('ns0:attachment')
        attachment.data = base64.encodestring(open(filepath).read())

        result = self.kbm_client.service.getKbmTo(attachment)
        return result

    def response_kbm(self, filename, response):
        output = base64.decodestring(response.data)

        logger.info('save response for %s' % filename)

        f = open(os.path.join(settings.out_dir, filename), 'w')
        try:
            f.write(output)
        finally:
            f.close()

    def proceed_error(self, filepath):
        dest = os.path.join(settings.error_dir, os.path.basename(filepath))
        shutil.move(filepath, dest)
