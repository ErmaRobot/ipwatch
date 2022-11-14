#
#  Read the coniguration file and set parametes for operation
#  Parameters:
#              - Log file locations
#              - IP determination method
#              - Determination methods directory location
#

previousIPDir = '/home/artemis/ipwatch/src/'
previousIP = 'previous_ip'

logDir = '/home/artemis/ipwatch/log/'

logFile = 'log'
logLine = '[{day}:{hr}:{min}:{sec}] {event}\n'

errorLogFile = 'error'
errorLine = '[{day}:{hr}:{min}:{sec}] {event}\n'

methodsDir = '/home/artemis/ipwatch/method/'
method = 'HUMAX_BGW320-500_3-19-7'

import sys
sys.path.insert(1, methodsDir)

import importlib
network = importlib.import_module(method)

