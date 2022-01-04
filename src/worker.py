from control import Control
import time



class CryptoBombWorker(object):
    control = None

    def __init__(self):
        self.control = Control([
            ['close', '../assets/close.png'],
            ['menu', '../assets/menu.png'],
            ['start', '../assets/start.png'],
            ['work', '../assets/work.png'],
        ])

class Worker(CryptoBombWorker):
    def execute(self):
        print('executing...')
        self.control.click('menu')
        time.sleep(2)
        self.control.click('work')
        time.sleep(1)
        self.control.click('close')

    def restart(self):
        print('restarting...')
        self.control.click('start')
