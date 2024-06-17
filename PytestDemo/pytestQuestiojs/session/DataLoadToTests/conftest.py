import pytest
#we can run fixture file once in session, common fixture method will write in conftest file.
# in this example conftest file have fixture method setup, remaining 2 files have few methods,
# when we run through command prompt "pytest -v -s" all test methods will run from test class1 and test class 2 ,
# before that once for session conftest fixture method will run.
#how to execute a fixture automataclly while running any file . by using autouse =True.
# otherwise fixture method won't execute

@pytest.fixture(scope='session',autouse=True)
def myfixture():
    print("conftest fixture method called:   ")


@pytest.fixture()
def dataload():
    print("user profile data is being created: ")
    return ["Param-1", "Param-2", "QA"]
