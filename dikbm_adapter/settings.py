# -*- coding: utf-8 -*-
import ConfigParser
import logging
import logging.config
import os

logger = logging.getLogger(__name__)

config = ConfigParser.ConfigParser()
config.read('settings.ini')


def config_get(config=config, *args):
    try:
        config.get('DiKBM', *args[:-1])
    except:
        return args[-1]


class Settings:
    username = config.get('DiKBM', 'username')
    password = config.get('DiKBM', 'password')

    in_dir = config_get('DiKBM', 'incomingDir', 'incoming')
    out_dir = config_get('DiKBM', 'outgoingDir', 'outgoing')
    status_dir = config_get('DiKBM', 'statusDir', 'status')
    error_dir = config_get('DiKBM', 'errorDir', 'error')
    temp_dir = config_get('DiKBM', 'tempStatus', 'tempStatus')
    log_dir =  config_get('DiKBM', 'logDir', 'log')

    kbmto_url = config_get('DiKBM',
                           'kbmToServiceUrl',
        'http://172.19.3.9/dkbm-ws-1.0/services/kbmToServiceNoMtom?wsdl'
    )
    policyloss_url = config_get('DiKBM',
                                'PolicyLossServiceUrl',
        'http://172.19.3.9/dkbm-ws-1.0/services/policyLossService?wsdl'
    )
    history_url = config_get('DiKBM',
                             'historyServiceUrl',
        'http://172.19.3.9/dkbm-ws-1.0/services/historyService?wsdl'
    )

    def __init__(self):
        for dir in (settings.in_dir, settings.out_dir,
                    settings.status_dir, settings.error_dir,
                    settings.log_dir):
            try:
                os.mkdir(dir)
            except (IOError, WindowsError):
                pass

settings = Settings()
logging.config.fileConfig('settings.ini')
