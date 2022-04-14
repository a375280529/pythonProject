import logging.handlers
import logging


def init_log_config(filename, when='midnight', interval=1, backup_count=7):

    # 1. 创建日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 3. 创建处理器对象
    # 输出到控制台
    st = logging.StreamHandler()
    # 输出到日志文件
    # when 是一个字符串，定义了日志切分的间隔时间单位
    # interval 是间隔时间单位的个数，指等待多少个 when 的时间后继续进行日志记录
    # backupCount 是保留日志的文件个数
    fh = logging.handlers.TimedRotatingFileHandler(filename,
                                                   when=when,
                                                   interval=interval,
                                                   backupCount=backup_count,
                                                   encoding='utf-8')

    # 4. 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 5. 给处理器设置格式化器
    st.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 6. 给日志器添加处理器
    logger.addHandler(st)
    logger.addHandler(fh)

