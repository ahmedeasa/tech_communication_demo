from hello import toyou, add, subtract


def setup_function(function):
    print("running Setup: %s" % {function.__name__})
    function.x = 10


def teardown_function(function):
    print("tearing down : %s" % {function.__name__})
    del function


def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9
