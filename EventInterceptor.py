#! /usr/bin/python2.6

import Quartz
import time
from KeycodeTranslator import KeycodeTranslator
import os

class EventInterceptor:

    def __init__(self):
        self.KeyTranslator = KeycodeTranslator()
        self.exitCount = 0

    def SetProfile(self,profile):
        self.profile = profile

    def SetEmulators(self,keyboard,mouse):
        self.KeyboardEmulator = keyboard
        self.MouseEmulator = mouse

    def Start(self):
        self.addListenerKeydownEvent();

    def addListenerKeydownEvent(self):
        eventMask = (1 << Quartz.kCGEventKeyDown) #(1 << kCGEventKeyDown) | (1 << kCGEventKeyUp)
        eventTap = Quartz.CGEventTapCreate(Quartz.kCGSessionEventTap,Quartz.kCGHeadInsertEventTap,0,eventMask,self.KeydownEvent,None);
        if not eventTap:
            print "ERROR: failed to create event tap."
        else:
            runLoopSource = Quartz.CFMachPortCreateRunLoopSource(Quartz.kCFAllocatorDefault,eventTap,0)
            Quartz.CFRunLoopAddSource(Quartz.CFRunLoopGetCurrent(),runLoopSource,Quartz.kCFRunLoopCommonModes);
            Quartz.CGEventTapEnable(eventTap, True);
            Quartz.CFRunLoopRun();

    def KeydownEvent(self, proxy, etype, event, refcon):
        # Get Keycode and Keyboard Type (for identification)
        keycode = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
        # 43 = Mac Inbuilt Keyboard; 40 = PC-Style External Keyboard
        keyboardType = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeyboardType)

        # hard coded exit
        if keycode!=51: self.exitCount = 0
        if keycode==51: self.exitCount = self.exitCount+1
        if self.exitCount==10: exit()

        for interception in self.profile.Events["keydown"]:
            condition = True
            if "type" in self.profile.Events["keydown"][interception]:
                if int(self.profile.Events["keydown"][interception]["type"])!=keyboardType:
                    condition = False
            if "key" in self.profile.Events["keydown"][interception]:
                if self.KeyTranslator.KeycodeFromName(self.profile.Events["keydown"][interception]["key"])!=keycode:
                    condition = False

            
            if condition==True:
                self.profile.RunMacro(self.profile.Events['keydown'][interception]['macro'])
                event = None

        return event
