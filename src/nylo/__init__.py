# This file is a part of nylo
#
# Copyright (c) 2018 The nylo Authors (see AUTHORS)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from collections import defaultdict
from .parser import Parser
from .token import Token
from .interpreter import interprete
from .builtins import If
from .tokens.keyword import Keyword
import time

builtins = {
    'classes': defaultdict(list),
    'types': {},
    'arguments': defaultdict(list, {
        (Keyword('if'),): [(Keyword('if'), Keyword('cond')),
                           (Keyword('if'), Keyword('then')),
                           (Keyword('if'), Keyword('else'))]
    }),
    (Keyword('if'),): (Keyword('placeholder'),),
    (Keyword('if'), Keyword('self')): If(),
    }

__author__ = 'Veggero il Veggente'
__url__ = 'https://github.com/veggero/nylo'
__license__ = 'GNU GENERAL PUBLIC LICENSE'
__version__ = '0.0.0'
