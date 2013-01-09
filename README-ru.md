python-dikbm-adapter
=========================


Установка
----------------

Процесс установки очень простой

    easy_install python-dikbm-adapter

или

    pip install python-dikbm-adapter

или

    pip install git+https://github.com/suvit/python-dikbm-adapter


Настройки
-----------------------

Пожалуйста, создайте ``settings.ini`` файл в той же папке где и был установлен скрипт dikbm_main

Или можете создать другой исполняемый скрипт, который вызывает dikbm_main, тогда файл с настройками надо положить рядом

Пример минимального файла настроек

    [DiKBM]
    username = my_secret_username
    password = my_secret_password

Другие настройки(и их значения по умолчанию)

    [DiKBM]

    incomingDir = incoming
    outgoingDir = outgoing
    errorDir = error
    logDir = log
    #statusDir = status
    #tempStatus = tempStatus

    kbmToServiceUrl = http://172.19.3.9/dkbm-ws-1.0/services/kbmToServiceNoMtom?wsdl
    PolicyLossServiceUrl = http://172.19.3.9/dkbm-ws-1.0/services/policyLossService?wsdl
    historyServiceUrl = http://172.19.3.9/dkbm-ws-1.0/services/historyService?wsdl

Так же в этом же файле настроек можно положить настроики для системы логирования

Пример настроек для логирования

    [loggers]
    keys=root, suds

    [handlers]
    keys=console, default

    [formatters]
    keys=simple, advanced, verbose

    [logger_root]
    level=DEBUG
    #handlers=console
    handlers=default

    [logger_suds]
    level=INFO
    #handlers=console
    handlers=default
    qualname=suds
    propagate=0

    [handler_console]
    class=StreamHandler
    level=DEBUG
    formatter=advanced
    args=(sys.stdout,)

    [handler_default]
    class=FileHandler
    level=INFO
    formatter=advanced
    filename=main.log
    args=('log/main.log', 'a')

    [formatter_simple]
    format = %(levelname)s - %(message)s

    [formatter_advanced]
    format = %(asctime)s - %(levelname)s - %(name)s - %(message)s

    [formatter_verbose]
    format = %(asctime)s - %(levelname)s - %(name)s - %(module)s - %(process)d - %(thread)d - %(message)s

Для запуска просто запустить скрипт.
``virtualenv/bin/dikbm_main`` или ``virtualenv/Scripts/dikbm_main.exe``

Вы так же можете добавить запуск скрипта в cron-задачу или windows-задание
