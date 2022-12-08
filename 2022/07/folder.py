#!/usr/bin/env python3

import fileinput

class Folder:
    root = None

    def createRoot():
        Folder.root= Folder()
        Folder.root.parent = Folder.root

    def __init__(self, parent=None):
        self.parent = parent
        self.subfolders = {}
        self.documents = {}
        self.cachedSize = 0

    def mkdir(self, name):
        self.subfolders[name] = Folder(self)

    def getdir(self, name):
        if name not in self.subfolders:
            self.mkdir(name)
        return self.subfolders[name]

    def touch(self, name, size):
        self.documents[name] = size

    def size(self):
        if self.cachedSize > 0:
            return self.cachedSize
        for ignore, folder in self.subfolders.items():
            self.cachedSize += folder.size()
        for ignore, size in self.documents.items():
            self.cachedSize += size
        return self.cachedSize

    def walk(self):
        for ignore, subfolder in self.subfolders.items():
            for item in subfolder.walk():
                yield item
        yield self

def parse(args):
    Folder.createRoot()
    cwd = Folder.root
    for line in fileinput.input(args):
        if line[0:4] == '$ ls':
            pass
        elif line[0:4] == '$ cd':
            dir_name = line[5:-1]
            if dir_name == '/':
                cwd = Folder.root
            elif dir_name == '..':
                cwd = cwd.parent
            else:
                cwd = cwd.getdir(dir_name)
        elif line[0] == 'd':
            cwd.mkdir(line[4:-1])
        else:
            space = line.find(' ')
            size = int(line[0:space])
            name = line[space+1:-1]
            cwd.touch(name, size)
