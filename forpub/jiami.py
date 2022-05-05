# -*- coding: utf-8 -*-
import pickle

import jpype
import os
import time
import sys

if __name__ == '__main__':
    """
    基本的开发流程如下：
    ①、使用jpype开启jvm
    ②、加载java类
    ③、调用java方法根据
    ④、关闭jvm（不是真正意义上的关闭，卸载之前加载的类）
    """
    #获取执行文件得路径用于更改成exe执行方式后获取文件
    exepath=os.path.realpath(sys.executable)
    endpath=exepath.split(exepath.split("\\")[-1])[0]
    # ①、使用jpype开启虚拟机（在开启jvm之前要加载类路径）
    #exe方式时的jar文件路径获取
    jarpath = os.path.join(os.path.abspath('.'), endpath+"jiajiemi.jar")
    # 加载刚才打包的jar文件
    jarpath = os.path.join(os.path.abspath('.'), 'F:/zxc/jiajiemi.jar')

    # 获取jvm.dll的文件路径
    jvmPath = jpype.getDefaultJVMPath()
    # 开启jvm
    jpype.startJVM(jvmPath, '-ea', '-Djava.class.path=%s' % (jarpath))
    # 加载java类（参数名是java的长类名）
    javaClass = jpype.JClass('CryptionUtil')

    # 实例化java对象
    javaInstance = javaClass()
    
    # # 实例化调用方法
    # javaInstance.sh()
    # # 使用类调用静态方法
    # javaClass.show()

    fd=javaClass.decryptNsrsbh("sayjyywlpiuwjoro","0s9sef0EVcfD1SDmieqeBzUSCjeWm36J_bU2u0Jg5Ac")
    print(fd)
    # 关闭jvm
    jpype.shutdownJVM()

    time.sleep(1)

    pickle.load()