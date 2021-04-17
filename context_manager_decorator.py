##Implementing a Context Manager as a Generator


from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    except:
        #to catch exceptions here
        raise
    finally:
        f.close()
        
        


with open_file('some_file') as f:
    f.write('hola!')
