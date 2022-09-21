#!/usr/bin/env python3
"""tests for jump.py"""

import os
from subprocess import getstatusoutput

prg = './jump_word.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')



# --------------------------------------------------
def test_02():
    """test"""

    rv, out = getstatusoutput(f'{prg} "That number to call out is 12345."')
    assert rv == 0
    assert out.rstrip() == 'That number to call out is onetwothreefourfive.'
