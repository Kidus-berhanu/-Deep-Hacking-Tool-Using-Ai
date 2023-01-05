# coding=utf-8
import os
import sys
import webbrowser
from platform import system
from traceback import print_exc
from typing import Any
from typing import Callable
from typing import List
from typing import Tuple


def clear_screen() -> None:
    os.system("cls" if system() == "Windows" else "clear")


def validate_input(ip: str, val_range: List[int]) -> int:
    if ip.isdigit() and int(ip) in val_range:
        return int(ip)
    return None


class HackingTool:
    # About the HackingTool
    TITLE: str = ""  # used to show info in the menu
    DESCRIPTION: str = ""

    INSTALL_COMMANDS: List[str] = []
    INSTALLATION_DIR: str = ""

    UNINSTALL_COMMANDS: List[str] = []

    RUN_COMMANDS: List[str] = []

    OPTIONS: List[Tuple[str, Callable]] = []

    PROJECT_URL: str = ""

    def __init__(self, options: List[Tuple[str, Callable]] = None, installable: bool = True, runnable: bool = True):
        self.OPTIONS = []
        if installable:
            self.OPTIONS.append(('Install', self.install))
        if runnable:
            self.OPTIONS.append(('Run', self.run))
        self.OPTIONS.extend(options or [])

    def show_info(self) -> None:
        desc = self.DESCRIPTION
        if self.PROJECT_URL:
            desc += '\n\t[*] '
            desc += self.PROJECT_URL
        os.system(f'echo "{desc}"|boxes -d boy | lolcat')

    def show_options(self, parent=None) -> Any:
        clear_screen()
        self.show_info()
        for index, option in enumerate(self.OPTIONS):
            print(f"[{index + 1}] {option[0]}")
        if self.PROJECT_URL:
            print(f"[{98}] Open project page")
        print(f"[{99}] Back to {parent.TITLE if parent else 'Exit'}")
        option_index = input("Select an option: ")
        option_index = validate_input(option_index, list(range(1, len(self.OPTIONS) + 1)))
        if option_index:
            try:
                ret_code = self.OPTIONS[option_index - 1][1]()
                if ret_code != 99:
                    input("\n\nPress ENTER to continue:")
            except Exception:
                print_exc()
                input("\n\nPress ENTER to continue:")
        elif option_index == 98:
            self.show_project_page()
        elif option_index == 99:
            if parent is None:
                sys.exit()
            return 99
        return self.show_options(parent=parent)

    def before_install(self) -> None:
        pass

    def install(self) -> None:
        self.before_install
        
   class HackingToolsCollection(object):
    TITLE: str = ""  # used to show info in the menu
    DESCRIPTION: str = ""
    TOOLS = []  # type: List[Any[HackingTool, HackingToolsCollection]]

    def __init__(self):
        pass

    def show_info(self):
        os.system("figlet -f standard -c {} | lolcat".format(self.TITLE))
        # os.system(f'echo "{self.DESCRIPTION}"|boxes -d boy | lolcat')
        # print(self.DESCRIPTION)

    def show_options(self, parent = None):
        clear_screen()
        self.show_info()
        for index, tool in enumerate(self.TOOLS):
            print(f"[{index} {tool.TITLE}")
        print(f"[{99}] Back to {parent.TITLE if parent is not None else 'Exit'}")
        tool_index = input("Choose a tool to proceed: ")
        try:
            tool_index = int(tool_index)
            if tool_index in range(len(self.TOOLS)):
                ret_code = self.TOOLS[tool_index].show_options(parent = self)
                if ret_code != 99:
                    input("\n\nPress ENTER to continue:")
            elif tool_index == 99:
                if parent is None:
                    sys.exit()
                return 99
        except (TypeError, ValueError):
            print("Please enter a valid option")
            input("\n\nPress ENTER to continue:")
        except Exception:
            print_exc()
            input("\n\nPress ENTER to continue:")
        return self.show_options(parent = parent)
