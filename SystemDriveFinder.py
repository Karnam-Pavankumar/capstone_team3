
import os
class SystemDriveFinder:
   ''' to find system drives '''


   def __init__ ( self ) :
        pass


   def Find_Drive(self):
        print("this is the find drives method of system drive finder class : ")

        drives = []

        for x in range(65,91):
            if os.path.exists(chr(x) + ":"):
                drives.append(chr(x))

        return drives

if __name__ == "__main__":
    obj = SystemDriveFinder()
    print(obj.Find_Drive())






