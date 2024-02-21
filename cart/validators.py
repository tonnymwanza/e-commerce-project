from django.core.exceptions import ValidationError

#our validators
def email_validation(value):
    email = value
    if not '@gmail.com' in email:
        raise ValidationError('the email must have @gmail.com')
    return email