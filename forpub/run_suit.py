import logging
import time
from log_config import init_log_config

if __name__ == '__main__':
    # 1:获取当前时间戳并整理格式(获取实时日志)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 初始化日志
    log_path='../logFile/' + now + '.log'
    init_log_config(log_path)

    logging.info(f"税号【】表一未执行测试用例表前的最新一条时间=")

