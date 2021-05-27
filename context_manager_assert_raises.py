import traceback
import contextlib

# Some helper code to demonstrate the kinds of errors you might encounter.
@contextlib.contextmanager
def assert_raises(error_class):
  try:
    yield
  except error_class as e:
    print('Caught expected exception \n  {}:'.format(error_class))
    traceback.print_exc(limit=2)
  except Exception as e:
    raise e
  else:
    raise Exception('Expected {} to be raised but no error was raised!'.format(
        error_class))
    
def test_me(a,b):
  return a+b

with assert_raises(TypeError):
  test_me("abcbds",5)
  

"""
Caught expected exception 
  <class 'TypeError'>:
Traceback (most recent call last):
  File "<ipython-input-19-73d0ca52e838>", line 8, in assert_raises
    yield
  File "<ipython-input-23-cbc9c1260e5a>", line 2, in <module>
    test_me("abcbds",5)
TypeError: can only concatenate str (not "int") to str
"""

  
