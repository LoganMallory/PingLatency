# PingLatency
Ping servers and export latency data to a csv.

This python program uses subprocesses to ping a specified server 32 times, returning the latency data and start and end times as a Pandas data frame. 

This data frame is exported to your computer in every iteration of the 'while' loop, which helps guard against memory errors or unforseen events.

The ping tests run every x number of seconds, and the program can be interrupted at any time during this sleeptime with no harmful effects on the data. 
