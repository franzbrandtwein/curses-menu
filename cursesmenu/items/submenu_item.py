import curses

from cursesmenu import CursesMenu
from cursesmenu.items import MenuItem


class SubmenuItem(MenuItem):
    """
    A menu item that opens a submenu.
    """

    def __init__(self, text, submenu, menu=None, should_exit=False):
        """
        :param CursesMenu submenu: The submenu to be opened when this item is selected
        """
        super(SubmenuItem, self).__init__(text=text, menu=menu, should_exit=should_exit)

        self.submenu = submenu
        if menu:
            self.submenu.parent = menu

    def set_menu(self, menu):
        self.menu = menu
        self.submenu.parent = menu

    def set_up(self):
        self.menu.pause()
        curses.def_prog_mode()
        self.menu.clear_screen()

    def action(self):
        """
        Shows the submenu
        """
        self.submenu.start()

    def clean_up(self):
        """
        Wait on the submenu to return, then clean up and resume the parent menu
        """
        self.submenu.join()
        self.menu.clear_screen()
        curses.reset_prog_mode()
        curses.curs_set(1)  # reset doesn't do this right
        curses.curs_set(0)
        self.menu.resume()

    def get_return(self):
        return self.submenu.returned_value
