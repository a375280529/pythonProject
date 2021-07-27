#!/usr/bin/python
# -*- coding: utf-8 -*-

import jpype


jvmPath=jpype.getDefaultJVMPath()
jvmArg="-Xint"
if not jpype.isJVMStarted():
    jpype.startJVM(jvmPath,jvmArg)
jpype.java.lang.System.out.println("hello world")
jpype.shutdownJVM()