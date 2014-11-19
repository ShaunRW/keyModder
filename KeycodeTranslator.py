#! /usr/bin/python2.6

# KEYCODE TRANSLATOR
#-----------------------------------------#
# Filename:         KeycodeTranslator.py
# Belongs To:       keyModder
# Usage:            from KeycodeTranslator import KeycodeTranslator
# Description:      Offers function to convert key codes to the key name and vice versa.
# Created:          19 Nov 2014
# Modified:         19 Nov 2014 
# Author:           Shaun Wilesmith
# Notes:
#
#
#-----------------------------------------#

class KeycodeTranslator:

      def __init__(self):
        self.KeycodeLookup = {
            'up':126,
            'down':125,
            'left':123,
            'right':124,
            'backspace':117,
            'enter':76,
            'home':115,
            'end':119,
            'pagedown':121,
            'pageup':116,
            'return':36,
            'delete':51,
            'tab':48,
            'spacebar':49,
            'shift':56,
            'control':59,
            'menu':58,
            'escape':53,
            'capslock':57,
            'help':114,
            'f1':122,
            'f2':120,
            'f3':99,
            'f4':118,
            'f5':96,
            'f6':97,
            'f7':98,
            'f8':100,
            'f9':101,
            'f10':109,
            'f11':103,
            'f12':111,
            'fn':63,
            'option':58,
            'command':55,
            'q':12,
            'w':13,
            'e':14,
            'r':15,
            't':17,
            'y':16,
            'u':32,
            'i':34,
            'o':31,
            'p':35,
            'a':0,
            's':1,
            'd':2,
            'f':3,
            'g':5,
            'h':4,
            'j':38,
            'k':40,
            'l':37,
            'z':6,
            'x':7,
            'c':8,
            'v':9,
            'b':11,
            'n':45,
            'm':46,
            '0':29,
            '1':18,
            '2':19,
            '3':20,
            '4':21,
            '5':23,
            '6':22,
            '7':26,
            '8':28,
            '9':25,
            'period':47,
            'comma':43,
            'slash':44,
            'num0':82,
            'num1':83,
            'num2':84,
            'num3':85,
            'num4':86,
            'num5':87,
            'num6':88,
            'num7':89,
            'num8':91,
            'num9':92,
            'multiply':67,
            'add':69,
            'subtract':78,
            'divide':75,
            'decimal':65,
            'numequal':81
        }


      def KeycodeFromName(self, name):
        if name.lower() in self.KeycodeLookup:
            return self.KeycodeLookup[name.lower()]
        else:
            return False

      def NameFromKeycode(self, keycode):
            for k, v in self.KeycodeLookup.items():
                  if keycode==v:
                        return k

