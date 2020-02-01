from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.docopttest.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE


class DocopttestCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_docopttest(self, args, arguments):
        """

        ::
          Usage:
            docopttest [--user=USER] WORD
            docopttest (-h | --help)

          This command prints a word from a user.

          Arguments:
            WORD a word to send
          
          Options:
            --user who the message is from (default: brian)
            -h  print help message

        """
        
        print('why god')
        
        VERBOSE(arguments,verbose=-1)
        if not arguments['--user']:
            arguments['--user']='brian'
        print(arguments['--user'] + ' says:')
        print(arguments['WORD'])

        return ""

