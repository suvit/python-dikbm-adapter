python-dikbm-adapter
=========================


Installation
----------------

installation is simple

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

other settings and theire default values

    [DiKBM]

    incomingDir = incoming
    outgoingDir = outgoing
    statusDir = status
    errorDir = error
    tempStatus = tempStatus
    logDir = log

    kbmToServiceUrl = http://172.19.3.9/dkbm-ws-1.0/services/kbmToServiceNoMtom?wsdl
    PolicyLossServiceUrl = http://172.19.3.9/dkbm-ws-1.0/services/policyLossService?wsdl
    historyServiceUrl = http://172.19.3.9/dkbm-ws-1.0/services/historyService?wsdl

in the same ini file may be placed logging settings

to run use ``virtualenv/bin/dikbm_main`` or ``virtualenv/Scripts/dikbm_main.exe``



