import getpass

# dictionary of profile
def confirm_password():
    """

    make password invisible on terminal
    
    password = str(getpass.getpass("Please enter your Password: \n >"))
    confirm = str(getpass.getpass("Please confirm your password: \n >"))
    if password != confirm:
        confirm = str(getpass.getpass("Please confirm your password again: \n >"))
        if password != confirm:
            confirm_password()
    """
    password = str(input("Please enter your Password: \n >"))
    confirm = str(input("Please confirm your password: \n >"))
    if password != confirm:
        confirm = str(input("Please confirm your password again: \n >"))
        if password != confirm:
            confirm_password()

    else:
        return password


profile_dict = {'id':[],'password':[]
                }
def sign_up(profiles):
    id = str(input("Please enter your ID: \n >"))
    password = confirm_password()
    profiles['id'].append(id)
    profiles['password'].append(password)
    print("Sign Up successful!")
    print(profile)

def print_users(profiles):
    for i in range(0,len(profiles[id])):
        print("User \t Password")
        print(profiles["id"][i] + "\t" + profiles["password"][i])
        
profile_dict['id'].append('ljin0906')
profile_dict['id'].append('ljin')
profile_dict['id'].append('ljin950906')
profile_dict['password'].append('wkddnjs12')
profile_dict['password'].append('wkddnjs')
profile_dict['password'].append('Wkddnjs12')

