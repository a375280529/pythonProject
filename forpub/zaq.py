import os
import shutil
if __name__ == '__main__':
    # 用于无网络测试报告无网络的css和js
    if not os.path.exists("bueatifulcss"):
        shutil.copytree("template/bueatifulcss", "bueatifulcss")