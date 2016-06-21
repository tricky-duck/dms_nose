__author__ = 'anna.matveeva'

class Project:
    def __init__(self, branchName, appId=None, scope=None, root=None):
        self.branchName = branchName
        self.appId = appId
        self.scope = scope
        self.root = root

    def __repr__(self):
        return "%s;%s;%s;%s" % (self.branchName, self.appId, self.root, self.scope)

    def __eq__(self, other):
        return self.branchName == other.branchName
