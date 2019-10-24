from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField, StringField, validators, ValidationError
from wtforms.fields.html5 import EmailField, IntegerField
import phonenumbers


class ExxonForm(FlaskForm):
    PrimaryContactName = StringField('Имя контакта', [validators.DataRequired()])
    PrimaryJobTitle = StringField('Должность контакта', [validators.DataRequired()])
    PrimaryContactPhone = StringField('Телефон контакта', [validators.DataRequired()])
    PrimaryEMail = EmailField('Почта контакта', [validators.DataRequired(), validators.Email()])
    SecondaryContactName = StringField('Имя контакта')
    SecondaryJobTitle = StringField('Должность контакта')
    SecondaryContactPhone = StringField('Телефон контакта')
    SecondaryEMail = EmailField('Почта контакта', [validators.Email()])
    IndividualTaxNumber = StringField('ИНН', [validators.DataRequired(), validators.Length(max=12)])
    CompanyName = StringField('ИНН', [validators.DataRequired()])
    AddressLegal = StringField('ИНН', [validators.DataRequired()])
    AddressActual = StringField('ИНН', [validators.DataRequired()])
    RussianGovernment = IntegerField('ИНН', [validators.DataRequired(), validators.NumberRange(min=1, max=100)])
    RussiansCitizens = IntegerField('ИНН', [validators.DataRequired(), validators.NumberRange(min=1, max=100)])
    OtherRussianLegalEntity = IntegerField('ИНН', [validators.DataRequired(), validators.NumberRange(min=1, max=100)])
    TotalRussian = IntegerField('ИНН', [validators.DataRequired(), validators.NumberRange(min=1, max=100)])
    Website = StringField('ИНН', [validators.DataRequired()], default='https://')
    GoodsServicesComments = TextAreaField('ИНН', [validators.DataRequired()])
    recaptcha = RecaptchaField()

    def validate_phone(self, field):
        if len(field) > 16:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse(field)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
