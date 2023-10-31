from pweb import PWebForm, fields
from pweb_form_rest.common.pweb_custom_field import BaseEnum, EnumField

class Sex(BaseEnum):
    Male = "Male"
    Female = "Female"
    Not_Specified = "Not Specified"

class MemberForm(PWebForm):
    firstname = fields.String(required=True, error_messages={"required": "Please enter first name"})
    lastname = fields.String(allow_none=True)
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    password = fields.String(required=True, error_messages={"required": "Please enter password"})
    dob = fields.Date(required=True, error_messages={"required": "Please enter date of birth"})
    sex = EnumField(Sex, allow_none=True, placeholder="Select Sex")