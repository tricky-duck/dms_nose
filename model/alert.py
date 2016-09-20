# -*- coding: utf-8 -*-

# class Alert():
#
#     def __init__(self, message):
#         self.message = message
#
#     def __repr__(self):
#         return "%s" % (self.message)


class Alert:

    def __init__(self, message=None, popup=None, lang=None):
        self.message = message
        self.popup = popup
        self.lang = lang

    def __repr__(self):
        return "%s:%s:%s" % (self.text, self.popup, self.lang)

    # def __eq__(self, other):
    #     return self.lang == other.lang and self.text == other.text