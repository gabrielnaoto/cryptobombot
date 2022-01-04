from control import Control

class CryptoBombWorker(object):
    control = None

    def __init__(self):
        self.control = Control([
            ['settings', '../assets/settings.png'],
        ])

class Worker(CryptoBombWorker):
    def execute(self):
        self.control.click('settings')

    def restart(self):
        raise Exception('Not implemented')
