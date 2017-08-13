import logging
# create logger
logger_name = "statistics"
file_log = "public/logs/record.log"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)
# create file handler
fh = logging.FileHandler(file_log)
fh.setLevel(logging.DEBUG)
# create formatter
log_format = "%(asctime)s %(levelname)s %(lineno)d %(process)d %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(log_format, date_format)
# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)


def my_logger(level, path, username, message):
    if level == 'debug':
        logger.debug('{} {} {}'.format(path, username, message))
    elif level == 'info':
        logger.info('{} {} {}'.format(path, username, message))
    elif level == 'warning':
        logger.warning('{} {} {}'.format(path, username, message))
    elif level == 'error':
        logger.error('{} {} {}'.format(path, username, message))
    elif level == 'critical':
        logger.critical('{} {} {}'.format(path, username, message))