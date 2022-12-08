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
        self.fileSize = 0
        self.subfolderSize = 0

    def mkdir(self, name):
        self.subfolders[name] = Folder(self)

    def getdir(self, name):
        if name not in self.subfolders:
            self.mkdir(name)
        return self.subfolders[name]

    def addFileSize(self, size):
        self.fileSize += size

    def size(self):
        if self.subfolderSize == 0:
            for ignore, folder in self.subfolders.items():
                self.subfolderSize += folder.size()
        return self.subfolderSize + self.fileSize

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
            cwd.addFileSize(int(line[0:line.find(' ')]))
