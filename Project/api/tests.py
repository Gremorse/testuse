from django.test import TestCase

# Create your tests here.
from api.models import NewUser
import logging

class NewUserTestCase(TestCase):

    def setUp(self):
        pass

    def testA(self):
        newUser = NewUser(name='gaojb',age=18)
        name = newUser.__getattribute__('name')
        print(name)
        # LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        # DATE_FORMAT = "%Y/%d/%m %H:%M:%S %p"

        # logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
        logger = logging.getLogger('mylog')
        logger.debug("This is a debug log.")
        logger.info("This is a info log.")
        logger.warning("This is a warning log.")
        logger.error("This is a error log.")
        logger.critical("This is a critical log.")
        self.assertEqual('gaojb',name)