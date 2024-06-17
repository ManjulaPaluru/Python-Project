import pytest
from BaseClass import BaseClass
@pytest.mark.usefixtures("dataload")
class TestExample(BaseClass):

    def test_editProfileDemo(self,dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[1])


    #print(dataload[0])
    #print(dataload[1])
    #print(dataload[2])
