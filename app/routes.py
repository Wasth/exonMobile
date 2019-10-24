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


@app.route('/en')
def en_index():
    form = ExxonForm()
    return render_template('en_index.html', form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/ru', methods=['GET', 'POST'])
def ru_index():
    form = ExxonForm()
    return render_template('ru_index.html', form=form)


@app.route('/action', methods=['POST'])
def action():
    ITN = request.form.get('IndividualTaxNumber', None)
    CN = request.form.get('CompanyName', None)
    AL = request.form.get('AddressLegal', None)
    AA = request.form.get('AddressActual', None)
    COIN = request.form.get('CountryOfIncorporationName', None)
    RG = request.form.get('RussianGovernment', None)
    RC = request.form.get('RussiansCitizens', None)
    ORLE = request.form.get('OtherRussianLegalEntity', None)
    TR = request.form.get('TotalRussian', None)
    WEB = request.form.get('Website', None)
    GSCN = request.form.get('GoodsServicesCommentsName', None)
    GSLN = request.form.get('GoodsServicesListName', None)
    SAAN = request.form.get('ServiceAreaAvailableName', None)
    ACN = request.form.get('AnnualCashflowName', None)

    PCN = request.form.get('PrimaryContactName', None)
    PJT = request.form.get('PrimaryJobTitle', None)
    PCP = request.form.get('PrimaryContactPhone', None)
    PE = request.form.get('PrimaryEMail', None)

    SCN = request.form.get('SecondaryContactName', None)
    SJT = request.form.get('SecondaryJobTitle', None)
    SCP = request.form.get('SecondaryContactPhone', None)
    SE = request.form.get('SecondaryEMail', None)

    mess_arr = [{
        'PrimaryContactName': PCN,
        'PrimaryJobTitle': PJT,
        'PrimaryContactPhone': PCP,
        'PrimaryEMail': PE,

        'SecondaryContactName': SCN,
        'SecondaryJobTitle': SJT,
        'SecondaryContactPhone': SCP,
        'SecondaryEMail': SE,

        'IndividualTaxNumber': ITN,
        'CompanyName': CN,
        'AddressLegal': AL,
        'AddressActual': AA,
        'CountryOfIncorporationName': COIN,
        'RussianGovernment': RG,
        'RussiansCitizens': RC,
        'OtherRussianLegalEntity': ORLE,
        'OwnershipByNonRussian': TR,
        'Website': WEB,
        'GoodsServicesCommentsName': GSCN,
        'GoodsServicesListName': GSLN,
        'ServiceAreaAvailableName': SAAN,
        'AnnualCashflowName': ACN,
        'Date': strftime("%Y-%m-%d %H:%M:%S", gmtime())
    }]
    filename = '{}.json'.format(PCN + '_' + CN)

    with open(filename, 'w') as file:
        json.dump(mess_arr, file, indent=2, ensure_ascii=False)

    sender = app.config['ADMINS'][0]
    receiver = PE.split()[0]

    message = MIMEMultipart()
    message["From"] = receiver
    message["To"] = sender
    message["Subject"] = 'Blank {}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    body = 'Blank {}'.format(PCN + ' ' + CN)
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

    return redirect(url_for('ru_index'))
