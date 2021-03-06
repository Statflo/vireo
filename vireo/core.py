from .helper import log


class Core(object):
    def __init__(self, driver):
        self._driver = driver

    def emit(self, event_name, data = None, options = None):
        """ Emit a message.

            .. code-block:: python

                app.emit('security.alert.intrusion', {'ip': '127.0.0.1'})

        """
        log('debug', 'Publishing "{}" with {}'.format(event_name, data))

        self._driver.publish(event_name, data, options or {})

        log('debug', 'Published "{}" with {}'.format(event_name, data))
