|Build Status|\ |Documentation Status|\ |Coverage Status|

curses-menu
===========

A simple Python menu-based GUI system on the terminal using curses.
Perfect for those times when you need a GUI, but don’t want the overhead
or learning curve of a full-fledged GUI framework. However, it's also
flexible enough to do cool stuff like on-the-fly changing of menus and is extensible to
a large variety of uses.

http://curses-menu.readthedocs.org/en/latest/

.. image:: ./images/curses-menu_screenshot1.png


Installation
~~~~~~~~~~~~

Tested on Python 2.7, 3.3, 3.4, and 3.5, as well as pypy and pypy 3. Probably works on 2.6 as well.

The curses library comes bundled with python on Linux and MacOS. Windows
users can visit http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses and
get a third-party build for your platform and Python version.

Then just run

.. code:: shell

   pip install curses-menu

Usage
-----

It’s designed to be pretty simple to use. Here’s an example

.. code:: python

    # Import the necessary packages
    from cursesmenu import *
    from cursesmenu.items import *

    # Create the menu
    menu = CursesMenu("Title", "Subtitle")

    # Create some items

    # MenuItem is the base class for all items, it doesn't do anything when selected
    menu_item = MenuItem("Menu Item")

    # A FunctionItem runs a Python function when selected
    function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

    # A CommandItem runs a console command
    command_item = CommandItem("Run a console command", "touch hello.txt")

    # A SelectionMenu constructs a menu from a list of strings
    selection_menu = SelectionMenu(["item1", "item2", "item3"])

    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

    # Once we're done creating them, we just add the items to the menu
    menu.items.append(menu_item)
    menu.items.append(function_item)
    menu.items.append(command_item)
    menu.items.append(submenu_item)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

Testing Information
-------------------

Currently the platforms I'm manually testing on are MacOS in iTerm2 on zsh with and without TMUX and Windows 10\
with both powersehll and cmd.exe in and out of Windows Terminal. If a bug pops up on another configuration, \
no promises that I'll be able to reproduce it.

.. |Build Status| image:: https://github.com/pmbarrett314/curses-menu/actions/workflows/github-action-tox.yml/badge.svg
   :target: https://github.com/pmbarrett314/curses-menu/actions/workflows/github-action-tox.yml/badge.svg
.. |Documentation Status| image:: https://readthedocs.org/projects/curses-menu/badge/?version=latest
   :target: http://curses-menu.readthedocs.org/en/latest/?badge=latest
.. |Coverage Status| image:: https://coveralls.io/repos/github/pmbarrett314/curses-menu/badge.svg?branch=develop
   :target: https://coveralls.io/github/pmbarrett314/curses-menu?branch=develop
