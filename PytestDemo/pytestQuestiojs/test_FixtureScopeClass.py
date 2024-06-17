import pytest
#How to run a specific method before running all the test methods in a class using fixture ,
# setup and tear down will execute once.

class Test:
   @pytest.fixture(scope='class',autouse=True)
   def myfixture(self):
       print(" setup fixture")
   def test_method1(self):
      print("method1")
   def test_method2(self):
       print("method 2")

   def test_method3(self):
       print("method 3")