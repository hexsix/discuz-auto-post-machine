# -*- coding: utf-8 -*-

import abc

class usermgr:

    def __init__(self):
        self.users = [] # todo : replace this line with your own code

    def getUserNum(self):
        file_user = open('users','r')
        count=0
        try:
             lines  = file_user.readlines( )
             count=-1
             for line in lines:
                count=count+1
                print(line)
        finally:
             file_user.close( )
        return count

    def addUser(self, uname, pwd):
        """
        :uname type: string
        :pwd type: string
        :rtype: int
        """
        # todo
        return 0

    def post(self, title, message):
        """
        :title type: string
        :message type: string
        :rtype: bool
        """
        # todo
        return True

    def preContent(self, type):
        """
        :type type: int
        :rtype: string
        """
        # todo
        return ""

    def writeContent(self, content):
        """
        :content type: string
        :rtype: None
        """
        # todo
        return None

    def up(self, pid, userNum):
        """
        :pid type: string
        :userNum type: int
        :rtype: None
        """
        # todo
        return None

    def upShow(self):
        """
        :rtype: string
        """
        # todo
        return None
