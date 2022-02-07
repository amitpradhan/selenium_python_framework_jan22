import logging


class Log_Gen:
    @staticmethod
    def generate_log():
        logging.basicConfig(filename='../logs/automation1.log', format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.INFO, force=True)
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logging.getLogger()
