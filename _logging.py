#!/user/bin/python3
#_*_coding:utf-8 _*_

import logging
#第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)   #设置等级，只有大于Debug的日志才能呗logger处理

#第二步，创建一个handler,用于写入日志
file_handler = logging.FileHandler("test.log",mode="w")
file_handler.setLevel(logging.INFO)
#创建该handler的formatter
file_handler.setFormatter(
    logging.Formatter(
        fmt='%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s',
        datefmt= "%Y-%m-%d %H:%M:%S")
    )
#添加handle到logger中
logger.addHandler(file_handler)

#第三步，创建一个handler，用于输出控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL)

#创建该handler的formatter
console_handler.setFormatter(
    logging.Formatter(
        fmt="%(asctime)s-%(levelname)s:%(message)s",
        datefmt= "%Y-%m-%d %H:%M:%S")
)

logger.addHandler(console_handler)
#日志
logger.debug("这是一个调试bug")
logger.info("这是一个错误信息")
logger.warn("这是一个警告")
logger.error("这是一个错误")
logger.critical("这是一个危险通知")