import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log/teste.log',
                    level=logging.DEBUG)
logging.debug('blabla')
logging.error('ddddddddddddddddddddd')
