import json
from time import gmtime, strftime
from app import app, mail
from flask import render_template, request, redirect, url_for
from flask_mail import Message
from threading import Thread


@app.route('/en')
def en_index():
    return render_template('en_index.html')


@app.route('/')
@app.route('/ru')
def ru_index():
    return render_template('ru_index.html')


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@app.route('/action', methods=['POST'])
def action():
    ITN = request.form.get('IndividualTaxNumber', None)
    TOE = request.form.get('TypeOfEntity', None)
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

    message = json.dumps({
        'PrimaryContactName': PCN,
        'PrimaryJobTitle': PJT,
        'PrimaryContactPhone': PCP,
        'PrimaryEMail': PE,

        'SecondaryContactName': SCN,
        'SecondaryJobTitle': SJT,
        'SecondaryContactPhone': SCP,
        'SecondaryEMail': SE,

        'IndividualTaxNumber': ITN,
        'TypeOfEntity': TOE,
        'CompanyName': CN,
        'AddressLegal': AL,
        'AddressActual': AA,
        'CountryOfIncorporationName': COIN,
        'RussianGovernment': RG,
        'RussiansCitizens': RC,
        'OtherRussianLegalEntity': ORLE,
        'TotalRussian': TR,
        'Website': WEB,
        'GoodsServicesCommentsName': GSCN,
        'GoodsServicesListName': GSLN,
        'ServiceAreaAvailableName': SAAN,
        'AnnualCashflowName': ACN,
        'Date': strftime("%Y-%m-%d %H:%M:%S", gmtime())
    })

    subject = 'Your blank {}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    msg = Message(subject, sender=app.config['ADMINS'][0], recipients=PE.split())
    msg.body = 'Your blank'
    msg.html = message
    Thread(target=send_async_email, args=(app, msg)).start()
    return redirect(url_for('ru_index'))
