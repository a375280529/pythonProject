#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyclass import forLogger as lo

def dolog(log,logerror):
    log.logger.debug("debug222222")
    log.logger.info("info222222")
    log.logger.warning("warning222222")
    log.logger.critical("critical222222")
    logerror.logger.error("error222222")


if __name__ == '__main__':
    log = lo.Logger(level='debug')
    logerror = lo.Logger(level='error')
    dolog(log,logerror)