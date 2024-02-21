
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["pbkdf2_sha256", "des_crypt"], deprecated="auto")
def hash_password(password : str):
    return pwd_context.hash(password)

def verify(new_password, hashed_password):
    return pwd_context.verify(new_password, hashed_password)

# print(hash_password("preqsy"))
# print(pwd_context.hash("Hello"))