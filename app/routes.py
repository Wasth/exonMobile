import json
from time import gmtime, strftime
from app import app, mail
from flask import render_template, request, redirect, url_for
from flask_mail import Message
from threading import Thread


@app.route('/<lang>')
def index(lang='ru'):
    return render_template(lang + '_index.html')


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@app.route('/action', methods=['POST'])
def action():

    fields_names = (
        'IndividualTaxNumber',
        'TypeOfEntity',
        'CompanyName',
        'AddressLegal',
        'AddressActual',
        'CountryOfIncorporationName',
        'RussianGovernment',
        'RussiansCitizens',
        'OtherRussianLegalEntity',
        'TotalRussian',
        'Website',
        'GoodsServicesCommentsName',
        'GoodsServicesListName',
        'ServiceAreaAvailableName',
        'AnnualCashflowName',
        'PrimaryContactName',
        'PrimaryJobTitle',
        'PrimaryContactPhone',
        'PrimaryEMail',
        'SecondaryContactName',
        'SecondaryJobTitle',
        'SecondaryContactPhone',
        'SecondaryEMail',
    )

    fields_values = {}

    for field in fields_names:
        fields_values.update(field, request.form.get(field, None))

    fields_values['Date'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    message = json.dumps(fields_values)

    subject = 'Your blank {}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    msg = Message(
        subject,
        sender=app.config['ADMINS'][0],
        recipients=fields_values['PrimaryEMail'].split()
    )
    msg.body = 'Your blank'
    msg.html = message
    Thread(target=send_async_email, args=(app, msg)).start()
    return redirect(url_for('index'))
