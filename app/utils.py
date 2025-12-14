from pwdlib import PasswordHash  #not recommended
from passlib.context import CryptContext # recommended

# variables for hashing
# pwd_context = CryptContext(schemes=["bcrypt"] ,deprecated ="auto" , bcrypt__truncate_error=False)
# password_hash = PasswordHash.recommended()

# hashing function
def hashing_password(user_password : str):

    pwd = PasswordHash.recommended()

    hashed = pwd.hash(user_password)

    return hashed


def verify_hashing(plain_password: str , hashed_password: str):

    pwd = PasswordHash.recommended()

    return pwd.verify(plain_password , hashed_password)
