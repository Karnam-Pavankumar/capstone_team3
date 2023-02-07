import os
import time
class SearchFile:

    def __init__(self):
        pass

    def FindFile( self ,filename,filepath):
        files = []
        self.filename = filename
        self.filepath = filepath

        for root,dir,file in os.walk(filepath): #
            if filename in file:
                files.append(os.path.join(root,filename))
        return files

