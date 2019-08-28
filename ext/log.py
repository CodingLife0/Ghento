from datetime import datetime
import logging
import random
import string
import os


def id_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

logging.basicConfig(
    filename=os.path.join('data', open(datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f[')+str(id_generator(3))+'].rcb.log', 'w').name),
    filemode='a',
    format='%(asctime)s %(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%%H:%M:%S',
    level=logging.DEBUG
    )

logger = logging.getLogger('Core')

logger.info('test')
