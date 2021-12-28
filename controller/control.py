import pyautogui

# This class is responsible for creating click functions to locate objects.
class Control(object):
    objects = {}

    def __init__(self, objects):
        for object in objects:
            name, image = object
            self.objects[name] = self.add_object(self, image=image)

    def add_object(*args, **kwargs):
        def template(*args, **kwargs):
            image = kwargs.pop('image', None)
            if image is not None:
                location = pyautogui.locateOnScreen(image, confidence=0.75)
                pyautogui.click(**pyautogui.center(location))
            else:
                print('The image was not provided')

        return template

    def click_object(self, name):
        click = self.objects[name]
        click()

    # TODO: Create `click_all_objects` function that receives an object an it uses `locateAllOnScreen`,
    # iterates over all objects and scrolls to the bottom
