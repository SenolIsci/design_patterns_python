#DECORATORS WITH PARAMETERS



import functools

user=dict(username="senol",access_level="user")



def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function():
            if user["access_level"]==access_level:
                return func()
            else:
                return f"access level of {user['username']} is {user['access_level']}. No permission granted for {access_level}"
        return secure_function
    return decorator




@make_secure("admin")
def get_admin_password():
    """
    gives admin passport
    """
    return "admin:password_admin"

@make_secure("user")
def get_dashboard_password():
    """
    gives admin passport
    """
    return "user:1234"



print(get_admin_password())
print(get_dashboard_password())