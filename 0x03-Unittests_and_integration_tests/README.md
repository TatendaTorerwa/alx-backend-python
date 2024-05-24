# 0x03. Unittests and Integration Tests

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with:

$ python -m unittest path/to/test_file.py


## Resources
- Read or watch:
    - [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
    - [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
    - [How to mock a readonly property with mock?](https://stackoverflow.com/questions/383738/using-properties-on-python-mock-objects)
    - [parameterized](https://pypi.org/project/parameterized/)
    - [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Learning Objectives
- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
    - The difference between unit and integration tests.
    - Common testing patterns such as mocking, parametrizations and fixtures

## Requirements
### General
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Required Files
- [utils.py (or download)](utils.py)
- [client.py (or download)](client.py)
- [fixtures.py (or download)](fixtures.py)


## Tasks
### 0. Parameterize a unit test
- **mandatory**
- Familiarize yourself with the `utils.access_nested_map` function and understand its purpose. Play with it in the Python console to make sure you understand.
- In this task you will write the first unit test for `utils.access_nested_map`.
- Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.
- Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to.
- Decorate the method with `@parameterized.expand` to test the function for following inputs:
    - `nested_map={"a": 1}, path=("a",)`
    - `nested_map={"a": {"b": 2}}, path=("a",)`
    - `nested_map={"a": {"b": 2}}, path=("a", "b")`
- For each of these inputs, test with `assertEqual` that the function returns the expected result.
- The body of the test method should not be longer than 2 lines.

### 1. Parameterize a unit test
- **mandatory**
- Implement `TestAccessNestedMap.test_access_nested_map_exception`. Use the `assertRaises` context manager to test that a `KeyError` is raised for the following inputs (use `@parameterized.expand`):
    - `nested_map={}, path=("a",)`
    - `nested_map={"a": 1}, path=("a", "b")`
- Also make sure that the exception message is as expected.

### 2. Mock HTTP calls
- **mandatory**
- Familiarize yourself with the `utils.get_json` function.
- Define the `TestGetJson(unittest.TestCase)` class and implement the `TestGetJson.test_get_json` method to test that `utils.get_json` returns the expected result.
- We don’t want to make any actual external HTTP calls. Use `unittest.mock.patch` to patch `requests.get`. Make sure it returns a `Mock` object with a `json` method that returns `test_payload` which you parametrize alongside the `test_url` that you will pass to `get_json` with the following inputs:
    - `test_url="http://example.com", test_payload={"payload": True}`
    - `test_url="http://holberton.io", test_payload={"payload": False}`
- Test that the mocked get method was called exactly once (per input) with `test_url` as argument.
- Test that the output of `get_json` is equal to `test_payload`.

### 3. Parameterize and patch
- **mandatory**
- Read about memoization and familiarize yourself with the `utils.memoize` decorator.
- Implement the `TestMemoize(unittest.TestCase)` class with a `test_memoize` method.
- Inside `test_memoize`, define following class:
    ```python
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()
    ```
- Use `unittest.mock.patch` to mock `a_method`. Test that when calling `a_property` twice, the correct result is returned but `a_method` is only called once using `assert_called_once`.

### 4. Parameterize and patch as decorators
- **mandatory**
- Familiarize yourself with the `client.GithubOrgClient` class.
- In a new `test_client.py` file, declare the `TestGithubOrgClient(unittest.TestCase)` class and implement the `test_org` method.
- This method should test that `GithubOrgClient.org` returns the correct value.
- Use `@patch` as a decorator to make sure `get_json` is called once with the expected argument but make sure it is not executed.
- Use `@parameterized.expand` as a decorator to parametrize the test with a couple of org examples to pass to `GithubOrgClient`, in this order:
    - `google`
    - `abc`
