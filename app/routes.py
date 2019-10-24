import json
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from socket import gaierror
from time import gmtime, strftime
from app import app
from flask import render_template, request, redirect, url_for
from .forms import ExxonForm


@app.route('/<lang>', methods=['GET', 'POST'])
def index(lang='ru'):
    form = ExxonForm()
    return render_template(lang + '_index.html', form=form)


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

    mess_arr = [fields_values]

    filename = '{}.json'.format(fields_values['PrimaryContactPhone'] + '_' + fields_values['CompanyName'])

    with open(filename, 'w') as file:
        json.dump(mess_arr, file, indent=2, ensure_ascii=False)

    sender = app.config['ADMINS'][0]
    receiver = fields_values['PrimaryEMail'].split()[0]

    message = MIMEMultipart()
    message["From"] = receiver
    message["To"] = sender
    message["Subject"] = 'Blank {}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    body = 'Blank {}'.format(fields_values['PrimaryContactPhone'] + ' ' + fields_values['CompanyName'])
    message.attach(MIMEText(body, "plain"))

    with open(filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
        message.attach(part)

    try:
        with smtplib.SMTP("smtp.googlemail.com", 587) as server:
            server.starttls()
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            server.sendmail(sender, receiver, message.as_string())
    except (gaierror, ConnectionRefusedError):
        print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
    else:
        print('Sent')

    return redirect(url_for('index'))
