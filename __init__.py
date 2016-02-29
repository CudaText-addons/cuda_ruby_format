from cudatext import *
import sys
import os

from . import rubybeautifier
from . import format_proc

format_proc.INI = 'cuda_ruby_format.ini'
format_proc.MSG = '[Ruby Format] '

def options():
    opt = rubybeautifier.default_options()
    ini = format_proc.ini_filename()
    if os.path.isfile(ini):
        tab_is_spaces = ini_read(ini, 'format', 'tab_as_spaces', '1') == '1'
        tab_size = int(ini_read(ini, 'format', 'tab_size', '4'))
        #print('tab as spaces:', tab_is_spaces)
        #print('tab size:', tab_size)
        opt.indent_char = " " if tab_is_spaces else "\t"
        opt.indent_size = tab_size if tab_is_spaces else 1
    return opt

def do_format(text):
    return rubybeautifier.beautify(text, options())

class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        format_proc.run(do_format)
