from enum import Enum
from typing import Optional
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from pydantic import BaseModel


class Roles(str, Enum):
    CUSTOMER = "customer"
    VENDOR = "vendor"
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None

class PhoneNumber(str):
    supported_country_codes = {234}

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @staticmethod
    def validate(v: str):
        if not v:
            raise ValueError("Phone number cannot be empty")

        if v.startswith("0"):
            # Add the country code for Nigeria (234) if the number starts with "0"
            v = "+234" + v[1:]

        if not v.startswith("+"):
            raise ValueError("Phone number must start with '+'")

        try:
            parsed_number = phonenumbers.parse(v)
        except NumberParseException:
            raise ValueError("Invalid phone number format")

        if not phonenumbers.is_valid_number(parsed_number):
            raise ValueError("Invalid phone number")

        return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
