# Example of generating authenticating codes using guard module
# To use is you have to obtain 'shared_secret' and 'identity_secret'
# From your Steamguard file

from steampy.guard import generate_confirmation_key, generate_one_time_code
shared_secret = 'jSFM+54e0U6wmyDYGTMFQyu4LCs='
identity_secret = 'LgW1o15aeJmwnRO8C/pwgO75/4Q='

one_time_authentication_code = generate_one_time_code(shared_secret)
print(one_time_authentication_code)

confirmation_key = generate_confirmation_key(identity_secret, 'conf')
print(confirmation_key)
