#!/usr/bin/env python
# coding=utf-8
"""
logger.py - Phenny Log Module
2011, Vilson Vieira, http://automata.cc
Licensed under the GPL.

http://inamidst.com/phenny/
"""

import time
import os, sys

logdir = '/home/mov/public_html/'

def logger(phenny, input):
    phenny.say("logging...")

logger.commands = ['log']
logger.priority = 'medium'

def log(phenny, input):
    logfile = open(logdir + 'labmacambira.txt', 'a')
    line = input.group()
    line = "[" + str(time.strftime("%d-%m-%y %H:%M:%S")) + "] " + "<" + str(input.nick) + "> " + line + "\n"
    logfile.write(line.encode("utf-8"))
    logfile.close()

log.rule = r'(.*)'
log.priority = 'medium'



