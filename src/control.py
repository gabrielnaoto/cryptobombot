import pyautogui

class NeedsRestartException(Exception):
    pass

class Control(object):
    objects = {}

    # @param objects - [[foo, path/to/foo], [bar, path/to/bar]]
    def __init__(self, objects):
        for object in objects:
            name, path_to_image = object
            self.objects[name] = path_to_image

    def click(self, name, action='click'):
        image = self.objects.get(name)
        if image is not None:
            location = pyautogui.locateOnScreen(image, confidence=0.5)
            if location is not None:
                x, y = pyautogui.center(location)
                exec(f'pyautogui.{action}(x, y)')
            else:
                if name != 'start':
                    raise NeedsRestartException
                else:
                    print('The image was not found')
        else:
            print('The image was not provided')
