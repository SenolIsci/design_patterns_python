import cProfile, pstats
import functools
def profile_me(func):
  """Print the runtime of the decorated function"""
  @functools.wraps(func)
  def wrapper_profiler(*args, **kwargs):
    profiler = cProfile.Profile()
    profiler.enable()
    value=func(*args, **kwargs)
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()
    return value
  return wrapper_profiler

def create_array():
  arr=[]
  for i in range(0,400000):
    arr.append(i)

def print_statement():
  print('Array created successfully')

@profile_me
def main():
  create_array()
  print_statement()



main()



"""
output:
Array created successfully
         400039 function calls in 0.102 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.102    0.102 <ipython-input-16-d0bdc409dd39>:24(main)
        1    0.064    0.064    0.097    0.097 <ipython-input-16-d0bdc409dd39>:16(create_array)
   400000    0.033    0.000    0.033    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.001    0.001 <ipython-input-16-d0bdc409dd39>:21(print_statement)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.print}
        2    0.000    0.000    0.001    0.000 /usr/local/lib/python3.7/dist-packages/ipykernel/iostream.py:382(write)
        3    0.000    0.000    0.001    0.000 /usr/local/lib/python3.7/dist-packages/ipykernel/iostream.py:195(schedule)
        3    0.001    0.000    0.001    0.000 /usr/local/lib/python3.7/dist-packages/zmq/sugar/socket.py:438(send)
        2    0.000    0.000    0.000    0.000 /usr/local/lib/python3.7/dist-packages/ipykernel/iostream.py:320(_schedule_flush)
        3    0.000    0.000    0.000    0.000 /usr/lib/python3.7/threading.py:1092(is_alive)
        3    0.000    0.000    0.000    0.000 /usr/lib/python3.7/threading.py:1050(_wait_for_tstate_lock)
        2    0.000    0.000    0.000    0.000 /usr/local/lib/python3.7/dist-packages/ipykernel/iostream.py:307(_is_master_process)
        3    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.lock' objects}
        3    0.000    0.000    0.000    0.000 /usr/local/lib/python3.7/dist-packages/ipykernel/iostream.py:93(_event_pipe)
        2    0.000    0.000    0.000    0.000 {built-in method posix.getpid}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        3    0.000    0.000    0.000    0.000 /usr/lib/python3.7/threading.py:507(is_set)
        3    0.000    0.000    0.000    0.000 {method 'append' of 'collections.deque' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
