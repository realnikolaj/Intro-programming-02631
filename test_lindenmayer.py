#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:56:00 2018

@author: nik
"""

import unittest
import linditer

class TestLindenmayer(unittest.TestCase):
    
    def test_string(self):
        S = 'SLSRSLS'
        self.assertIs(LindIter('Korch', 0), '')
        self.assertIs(LindIter('Korch', 1), S)
        self.assertIs(LindIter('Korch', 2), S+'L'+S)
        self.assertIs(LindIter('Korch', 3), S+'L'+S+'R'+S+)

    def test_string(self):
        A = 'BRARB'
        B = 'ALBLA'
        self.assertIs(LindIter('Sierpinski', 0), '')
        self.assertIs(LindIter('Sierpinski', 1), A)
        self.assertIs(LindIter('Sierpinski', 2), B+'R'+A+'R'+B)
        #self.assertIs(LindIter('Korch', 3), S+'L'+S+'R'+S)
        
if __name__ == '__main__':
    unittest.main()