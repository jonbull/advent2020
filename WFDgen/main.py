# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# menu = prompt, default input, [allowed input]
class wfd():
    def __init__(self):
        self.menu_main = {
            "prompt": 'Enter Log Number to edit, or "N" to create new Log',
            "default": "N",
            "range": ["n", "q"]
        }

    def getinput(self, menu):
        def bloop(menu_selection):
            this_selection = input(menu["prompt"] + " (" + menu["default"] + "):")
            if this_selection == '':
                this_selection = menu["default"]
            return this_selection

        menu_selection = ''
        menu_selection = bloop(menu_selection)
        while menu_selection.lower() not in menu["range"]:
            print(f'Invalid option - {menu_selection}')
            menu_selection = bloop(menu_selection)
        return menu_selection


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    log = wfd()
    selection = ''
    while selection.lower() != 'q':
        selection = log.getinput(log.menu_main)
        print(f'You selected {selection}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
