import logging


class LoggingDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        logging.debug("setting %r or %r" % (key,value))
        logging.info("setting %r or %r" % (key, value))
        logging.warning("setting %r or %r" % (key, value))
        logging.error("setting %r or %r" % (key, value))
        logging.critical("setting %r or %r" % (key, value))
        pass

    pass


##logging.basicConfig(filename='logs/demo88.log', level=logging.WARNING)
logging.basicConfig(filename='logs/demo88.log', level=logging.DEBUG)
#logging.basicConfig(filename='logs/demo88.log', level=logging.INFO)

l1 = LoggingDict()
l1['mark'] = 'open source'
l1['ken'] = 'iOS'
l1['frank'] = 'oracle'
print(l1)
