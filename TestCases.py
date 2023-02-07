import pytest
from level1.SearchFile import SearchFile
from level1.SystemDriveFinder import SystemDriveFinder
class Test_Drive:
    def test_DriveCase( self ):
        obj = SystemDriveFinder()
        self.expected = obj.Find_Drive() #['C']
        self.actual = ['C']
        assert self.expected == self.actual
    def test_SearchFile( self ):
        obj = SearchFile()
        d = obj.FindFile('file.txt','C:\\')
        expt=['C:\\hcl\\file.txt', 'C:\\hclvijayawada\\file.txt']
        self.expected_filename = d
        self.actual_res =expt
        assert self.expected_filename == self.actual_res
