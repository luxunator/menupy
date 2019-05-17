import curses


class Menu:

    """
        **A Base class. Not to be used directly.**
    """

    colors = {
        'black': curses.COLOR_BLACK,
        'red': curses.COLOR_RED,
        'green': curses.COLOR_GREEN,
        'yellow': curses.COLOR_YELLOW,
        'blue': curses.COLOR_BLUE,
        'magenta': curses.COLOR_MAGENTA,
        'cyan': curses.COLOR_CYAN,
        'white': curses.COLOR_WHITE
        }

    def __init__(self, title, title_color='white', title_bg_color='black'):
        self.title = title
        self.title_color = title_color
        self.title_bg_color = title_bg_color
        self.menu_list = {}


class OptionMenu(Menu):

    """
        **Menu With Options to Select**

        Create menu and add options for selection

        :param title: Title to display on menu
        :type title: str
        :param cur: Menu cursor look
        :type cur: str
        :param title_color: Color for title text
        :type title_color: color
        :param title_bg_color: Color for title background
        :type title_bg_color: color
        :param cur_color: Color for cursor
        :type cur_color: color
        :param cur_bg_color: Color for cursor background
        :type cur_bg_color: color
    """

    def __init__(self, title, cur='->', title_color='white',
                 title_bg_color='black', cur_color='white',
                 cur_bg_color='black'):
        super().__init__(title, title_color, title_bg_color)
        self.cur = cur
        self.cur_color = cur_color
        self.cur_bg_color = cur_bg_color

    def _print_screen(self, screen, selected):
        screen.erase()
        screen.attron(curses.color_pair(1))
        screen.addstr(0, 1, self.title)
        screen.attroff(curses.color_pair(1))
        for index, (option, _) in enumerate(self.menu_list.items()):
            x = len(self.cur) + 1
            y = index + 2
            option_color = index + 3
            if index == selected:
                screen.attron(curses.color_pair(2))
                screen.addstr(y, 0, self.cur)
                screen.attroff(curses.color_pair(2))
                screen.attron(curses.color_pair(option_color))
                screen.addstr(y, x, option)
                screen.attroff(curses.color_pair(option_color))
            else:
                screen.attron(curses.color_pair(option_color))
                screen.addstr(y, x, option)
                screen.attroff(curses.color_pair(option_color))

        screen.refresh()

    def add_option(self, option, color='white', bg_color='black', ret=None):

        """
            Add option to your OptionMenu object

            :param option: Option to be displayed
            :type option: str
            :param color: Color for option text
            :type color: color
            :param bg_color: Color for option background
            :type bg_color: color
            :param ret: Custom Return value
            :type ret: Any
        """

        self.menu_list.update({option: {'color': color,
                                        'bg_color': bg_color,
                                        'ret': ret}})

    def _run(self, screen):
        curses.curs_set(0)
        curses.init_pair(1, self.colors[self.title_color],
                         self.colors[self.title_bg_color])
        curses.init_pair(2, self.colors[self.cur_color],
                         self.colors[self.cur_bg_color])

        for index, (_, settings) in enumerate(self.menu_list.items()):
            index += 3
            curses.init_pair(index, self.colors[settings['color']],
                             self.colors[settings['bg_color']])

        selected = 0

        while True:
            self._print_screen(screen, selected)

            key = screen.getch()

            if key == curses.KEY_UP and selected > 0:
                selected -= 1
            elif key == curses.KEY_DOWN and selected < len(self.menu_list)-1:
                selected += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                for index, (option,
                            settings) in enumerate(self.menu_list.items()):
                    if index == selected:
                        return settings['ret'] if settings['ret'] else option
                break

    def run(self):

        """
            Display Option Menu

            :return: Selected Option
            :rtype: str

        """

        selected_option = curses.wrapper(self._run)
        return selected_option


class InputMenu(Menu):

    """
        **Menu With Input Labels and Fields**

        Create menu and add input label

        :param title: Title to display on menu
        :type title: str
        :param cur: Menu cursor look
        :type cur: str
        :param submit: Text to display for submit button
        :type submit: str
        :param title_color: Color for title text
        :type title_color: color
        :param title_bg_color: Color for title background
        :type title_bg_color: color
        :param cur_color: Color for cursor
        :type cur_color: color
        :param cur_bg_color: Color for cursor background
        :type cur_bg_color: color
        :param submit_color: Color for submit button text
        :type submit_color: color
        :param submit_bg_color: Color for submit button background
        :type submit_bg_color: color
    """

    def __init__(self, title, cur='->', submit='Submit',
                 title_color='white', title_bg_color='black',
                 cur_color='white', cur_bg_color='black',
                 submit_color='white', submit_bg_color='black'):
        super().__init__(title, title_color, title_bg_color)
        self.cur = cur
        self.cur_color = cur_color
        self.cur_bg_color = cur_bg_color
        self.submit = submit
        self.submit_color = submit_color
        self.submit_bg_color = submit_bg_color

    def _print_screen(self, screen, selected, edit=False):
        screen.erase()
        screen.attron(curses.color_pair(1))
        screen.addstr(0, 1, self.title)
        screen.attroff(curses.color_pair(1))

        for index, (option, settings) in enumerate(self.menu_list.items()):
            x = len(self.cur) + 1
            y = index + 2
            option_color = (index * 2) + 3
            screen.attron(curses.color_pair(option_color))
            screen.addstr(y, x, option + ':')
            x += len(option) + 2
            screen.addstr(y, x, settings['input_text'])
            screen.attroff(curses.color_pair(option_color))

        screen.attron(curses.color_pair((len(self.menu_list)*2)+3))
        screen.addstr(len(self.menu_list)+3, len(self.cur) + 1, self.submit)
        screen.attroff(curses.color_pair((len(self.menu_list)*2)+3))

        for index, (option, settings) in enumerate(self.menu_list.items()):
            x = len(self.cur) + 1
            y = index + 2
            option_color = (index * 2) + 3
            if index == selected:
                curses.curs_set(2)
                curses.echo()
                screen.attron(curses.color_pair(2))
                screen.addstr(y, 0, self.cur)
                screen.attroff(curses.color_pair(2))
                screen.attron(curses.color_pair(option_color))
                screen.addstr(y, x, option + ':')
                screen.attron(curses.color_pair(option_color))
                x += len(option) + 2
                screen.addstr(y, x, settings['input_text'])
                if edit is True:
                    screen.attron(curses.color_pair(option_color+1))
                    new_text = screen.getstr(y, x, settings['input_length'])
                    if new_text != b'':
                        new_text = new_text.decode('utf-8')
                        settings['input_text'] = new_text
                    screen.attroff(curses.color_pair(option_color+1))

                curses.curs_set(0)
            else:
                screen.attron(curses.color_pair(option_color))
                screen.addstr(y, x, option + ':')
                x += len(option) + 2
                screen.addstr(y, x, settings['input_text'])
                screen.attroff(curses.color_pair(option_color))

        if len(self.menu_list) == selected:
            screen.attron(curses.color_pair(2))
            screen.addstr(len(self.menu_list)+3, 0, self.cur)
            screen.attroff(curses.color_pair(2))
            screen.attron(curses.color_pair((len(self.menu_list)*2)+3))
            screen.addstr(len(self.menu_list)+3,
                          len(self.cur) + 1, self.submit)
            screen.attroff(curses.color_pair((len(self.menu_list)*2)+3))

        screen.refresh()

    def add_input(self, option, input_text='', color='white',
                  bg_color='black', input_color='white',
                  input_bg_color='black', input_length=20):

        """
            Add option to your InputMenu object

            :param option: Label for input to be displayed
            :type option: str
            :param input_text: Default text to be displayed in input field
            :type input_text: str
            :param color: Color for label text
            :type color: color
            :param bg_color: Color for label background
            :type bg_color: color
            :param input_color: Color for input text
            :type input_color: color
            :param input_bg_color: Color for input background
            :type input_bg_color: color
            :param input_length: Length of input field
            :type input_length: int
        """

        self.menu_list.update({option: {'input_text': input_text,
                                        'color': color,
                                        'bg_color': bg_color,
                                        'input_color': input_color,
                                        'input_bg_color': input_bg_color,
                                        'input_length': input_length}})

    def _run(self, screen):
        curses.curs_set(0)
        curses.init_pair(1, self.colors[self.title_color],
                         self.colors[self.title_bg_color])
        curses.init_pair(2, self.colors[self.cur_color],
                         self.colors[self.cur_bg_color])
        curses.init_pair((len(self.menu_list)*2)+3,
                         self.colors[self.submit_color],
                         self.colors[self.submit_bg_color])

        for index, (_, settings) in enumerate(self.menu_list.items()):
            index = (index * 2) + 3
            curses.init_pair(index, self.colors[settings['color']],
                             self.colors[settings['bg_color']])
            index += 1
            curses.init_pair(index, self.colors[settings['input_color']],
                             self.colors[settings['input_bg_color']])

        selected = 0

        while True:
            self._print_screen(screen, selected)

            key = screen.getch()

            if key == curses.KEY_UP and selected > 0:
                selected -= 1
            elif key == curses.KEY_DOWN and selected < len(self.menu_list):
                selected += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if len(self.menu_list) == selected:
                    return {option: keys['input_text']
                            for option, keys in self.menu_list.items()}
                    break
                else:
                    self._print_screen(screen, selected, edit=True)

    def run(self):

        """
            Display Input Menu

            :return: Input Labels and Fields
            :rtype: dict

        """

        selected_option = curses.wrapper(self._run)
        return selected_option
