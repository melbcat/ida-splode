#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Indirect Trace Generated By Pin
import pymongoloader
# Symbol path: .;SRV*D:\Symbols*http://msdl.microsoft.com/download/symbols
# Looking for routine main
# CheckHeap            0x1
# CheckStack           0x1
# CheckSymbols         0x1
# CheckText            0
# CheckWhitelistSymbols0
# InstrumentIndirect   0x1
# InstrumentMov        0x1
time_begin=[2013,11,4,17,19,1]
now      ='-'.join([str(i) for i in time_begin])
dbName   = 'IdaSplode-test-py-' + now
if __name__ == '__main__':
  pymongoloader.ProcessFileIntoCollectition(__file__ + '.modules.py', dbName, 'modules')
  pymongoloader.ProcessFileIntoCollectition(__file__ + '.traces.py', dbName, 'traces')

# Whitelisting C:\workspace\pin\src\ida-splode\demo\test.exe based on test
time_end=[2013,11,4,17,19,13]
# Time Elapsed: 0 hours, 0 minutes, 11 seconds
# eof
