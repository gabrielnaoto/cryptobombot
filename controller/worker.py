from controller.control import Control

class CryptoBombWorker(object):
    control = None

    # Creates a new worker with a control object with control functions.
    def __init__(self):
        control = Control([
            {'close', 'path/to/close.png'},
            {'work', 'path/to/work.png'},
            {'menu', 'path/to/menu.png'},
            {'start_game', 'path/to/start_game.png'},
        ])

# Extends a CryptoBombWorker so it implements logic to work
class Worker(CryptoBombWorker):
    # Function responsible for putting all workers to work
    def execute(self):
        self.control.click_object('menu')
        self.control.click_object('work') # TODO: replace `work` call with something like: `click_all_objects('work')`
        self.control.click_object('close')

    # Function responsible for restarting the game when it disconnects
    def restart(self):
        self.control.click_object('start_game')
