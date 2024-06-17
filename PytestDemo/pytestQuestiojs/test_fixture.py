import pytest

# How to run a specific method before each test method run in a class using fixture
class Test:

    @pytest.fixture(scope= 'function', autouse = True)
    def mytestfixture(self,request):
        print("setup, fixture called: ")
        def teardown():
            print("teardown")
        request.addfinalizer(teardown)

    def test_method1(self):
        print("method 1 ")
    def test_method2(self):
        print("method 2")
