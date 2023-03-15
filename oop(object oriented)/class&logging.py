import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s: %(name)s: %(message)s')


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info(" Created Employee fullname {self.fullname}-- email {self.email} ")

    @property
    def email(self):
        return f'{self.first}{self.last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


name1 = Employee('jinnny', 'han')
