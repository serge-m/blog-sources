Title: Mocking in Python
Author: SergeM
Date: 2017-03-06 00:01:00
Slug: mocking-in-python
Tags: python, testing, unittests


Let's consider  how python standard unittest module suppose to use mocks.

Assume we want to test a method that creates and uses objects of other classes:

```python
# content of module.py

# classes that we want to mock
class ClassName1: 
  pass
  
class ClassName2:
  pass

# class that we want to test
class ProductionClass:
  def foo(self, parameter1, parameter2):
    object1 = module.ClassName1("some_initial_parameter1")
    intermediate_result = object1.run(parameter1)
    
    object2 = module.ClassName2("some_initial_parameter2")
    final_result = object2.run(intermediate_result, parameter2)
    
    return final_result
    
```

Here is how we can test object creation (Snippet is taken from [official documentation](https://docs.python.org/3/library/unittest.mock.html)):
```python
from unittest.mock import patch
@patch('module.ClassName2')
@patch('module.ClassName1')
def test(MockClass1, MockClass2):
    module.ClassName1()
    module.ClassName2()
    assert MockClass1 is module.ClassName1
    assert MockClass2 is module.ClassName2
    assert MockClass1.called
    assert MockClass2.called

test()
```

I would say that in our case we need also to check that each object (`object1` and `object2`) were instanciated and called with correct parameters. Then we can use `assert_called_once_with` like this (example from [official documentation](https://docs.python.org/3/library/unittest.mock.html#quick-guide)):
```python
with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, 2, 3)

mock_method.assert_called_once_with(1, 2, 3)
```

Combining things together:

```python

mocked_intermediate_result = "some-intermediate-result"
mocked_final_result = "some-final-result"

from unittest.mock import patch
@patch('module.ClassName2')
@patch('module.ClassName1')
def test_foo(MockClass1, MockClass2):
    MockClass1.return_value.run.return_value = mocked_intermediate_result
    MockClass2.return_value.run.return_value = mocked_final_result
    
    actual_result = module.ProductionClass().foo("parameter1", "parameter2")
    
    assert actual_result == mocked_final_result
    MockClass1.assert_called_once_with("some_initial_parameter1")
    MockClass1.return_value.run.assert_called_once_with("parameter1")
    MockClass2.assert_called_once_with("some_initial_parameter2")
    MockClass2.return_value.run.assert_called_once_with(mocked_intermediate_result, "parameter2")
    
```




https://github.com/kaste/mockito-python

