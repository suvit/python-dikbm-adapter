python-dikbm-adapter
=========================

[Русская документация](python-dikbm-adapter/blob/master/README-ru.md)


Installation
----------------

installation is simple

    easy_install python-dikbm-adapter

or

    pip install python-dikbm-adapter

or

    pip install git+https://github.com/suvit/python-dikbm-adapter

Settings
-----------------------

Please, create ``settings.ini`` file in the same dir as dikbm_main script installed

Sample of ini file

    [DiKBM]
    username = my_secret_username
    password = my_secret_password

other settings and their default values

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

in the same ini file may be placed logging settings

Example of logging settings

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

to run use ``virtualenv/bin/dikbm_main`` or ``virtualenv/Scripts/dikbm_main.exe``

you may add ``dikbm_main`` script to cron job or windows task
