#!/usr/bin/python
# -*- coding: utf-8 -*-

from zbar import Processor

device = '/dev/video0'


def readCode():
    try:
        # create a Processor
        proc = Processor()
        # configure the Processor
        proc.parse_config('enable')
        # initialize the Processor
        proc.init(device)
        proc.visible = True
        proc.process_one()
        proc.visible = False
    except:
        return "Error! Could not capture figure!"
    # extract results
    result = ""
    for symbol in proc.results:
        # do something useful with results
        result += symbol.data + '\n'
        # print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
    if not result: result = "Error! Could not recognize code!"
    return result

if __name__ == "__main__":
    print "Content-Type: text/html\r\n"
    print readCode()