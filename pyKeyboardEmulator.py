#! /usr/bin/python2.6

# pyKeyboardEmulator
#-----------------------------------------#
# Filename:         pyKeyboardEmulator.py
# Belongs To:       keyModder
# Usage:            from pyKeyboardEmulator import KeyboardEmulator
# Description:      This module is used to send keyboard events to the Operating System.
# Created:          19 Nov 2014
# Modified:         19 Nov 2014 
# Author:           Shaun Wilesmith
# Notes:
#
#
#-----------------------------------------#

import time
import Quartz
from KeycodeTranslator import KeycodeTranslator

class KeyboardEmulator:

    def __init__(self):
        self.KeyTranslator = KeycodeTranslator()
        self.pykb = PyKeyboard()


    def TapKey(self, name, modifierList=None, times=1, interval=0):
        keycode = self.KeyTranslator.KeycodeFromName(name)
        self.TapKeycode(keycode,modifierList,times,interval)


    def TapKeycode(self,keycode, modifierList=None, times=1, interval=0):
        mod = self.CreateModifierFlag(modifierList)
        for i in range(times):
            self.ChangeKeyState(keycode,True,mod)
            self.ChangeKeyState(keycode,False,mod)
            time.sleep(interval)


    def ChangeKeyState(self,keycode, isDown, modifiers=None):
        src = Quartz.CGEventSourceCreate(Quartz.kCGEventSourceStateHIDSystemState)
        event = Quartz.CGEventCreateKeyboardEvent(src, keycode, isDown)

        if modifiers!=None:
            Quartz.CGEventSetFlags(event,modifiers)

        Quartz.CGEventPost(Quartz.kCGSessionEventTap, event)


    def CreateModifierFlag(self, modifierList):
        if modifierList==None:
            return None
        else:
            approvedModifiers = ['Shift','Command','Control','Alternate']
            modStr = ''
            isFirst = True

            for modifier in modifierList:
                if modifier in approvedModifiers:
                    if isFirst!=True:
                        modStr = modStr + ' ^ '
                    modStr = modStr + 'Quartz.kCGEventFlagMask'+modifier
                    isFirst=False
                else:
                    print "ERROR: Modifier "+modifier+" does not exist."
                    exit();

            return eval(modStr)
