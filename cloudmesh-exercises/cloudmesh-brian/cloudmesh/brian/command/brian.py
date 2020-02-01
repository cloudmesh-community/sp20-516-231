from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.brian.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

from cloudmesh.common.Shell import Shell

class BrianCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_brian(self, args, arguments):
        """
        ::

          Usage:
                brian --file=FILE

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        arguments.FILE = arguments['--file'] or None

        VERBOSE(arguments)

        if arguments.FILE:
            result=Shell.execute('grep',['-i','brian',arguments.FILE])
            print(result)
        else:
            Console.error("provide a file")

        return ""
