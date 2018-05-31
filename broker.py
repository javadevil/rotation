class Broker(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Broker:{}'.format(self.name)