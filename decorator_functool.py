import functools

user=dict(username="senol",access_level="guest")



def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"]=="admin":
            return func()
        else:
            return f"access level of {user['username']} is {user['access_level']}. No permission granted"
    return secure_function





@make_secure
def get_admin_password():
    """
    gives admin passport
    """
    return "1234"


print(get_admin_password())
print(get_admin_password.__name__)
help(get_admin_password)
#when used with functools it will correctley adress get_admin_password.
"""
output:
access level of senol is guest. No permission granted
get_admin_password
Help on function get_admin_password in module __main__:

get_admin_password()
    gives admin passport

if you dont use decorator @functools.wraps(func). get_admin_password is not cerrectly addressed.
output:
    
access level of senol is guest. No permission granted
secure_function
Help on function secure_function in module __main__:

secure_function()

"""