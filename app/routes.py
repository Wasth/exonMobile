import json
from time import gmtime, strftime
from app import app, mail
from flask import render_template, request, redirect, url_for
from flask_mail import Message
from threading import Thread
from .forms import ExxonForm

threads = []


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@app.route('/en')
def en_index():
    form = ExxonForm()
    return render_template('en_index.html', form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/ru', methods=['GET', 'POST'])
def ru_index():
    form = ExxonForm()

    if form.validate_on_submit():
        print('tuta')
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

        with open('{}.json'.format(PCN + '_' + CN), 'w') as file:
            json.dump(mess_arr, file, indent=2, ensure_ascii=False)

        print('here')

        subject = 'Blank {}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        msg = Message(subject, sender=app.config['ADMINS'][0], recipients=PE.split())

        with open('{}.json'.format(PCN + '_' + CN)) as file:
            msg.attach('{}.json'.format(PCN + '_' + CN), "text/plain", file.read())

        msg.body = 'Blank {}'.format(PCN + ' ' + CN)
        msg.html = PCN + ' ' + CN
        t = Thread(target=send_async_email, args=(app, msg))
        threads.append(t)
        t.start()
        for tj in threads:
            tj.join()

    return render_template('ru_index.html', form=form)


#
# def check_recaptcha(response, remoteip):
#     return json.loads(requests.post('https://www.google.com/recaptcha/api/siteverify', data=dict(
#         secret=app.config.RECAPTCHA_PRIVATE_KEY,
#         response=response.get('g-recaptcha-response'),
#         remoteip=remoteip
#     )).text)['success']


def action_met(mess, PCN, CN, PE):
    with open('{}.json'.format(PCN + '_' + CN), 'w') as file:
        json.dump(mess, file, indent=2, ensure_ascii=False)

    print('here')

    subject = 'Blank {}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    msg = Message(subject, sender=app.config['ADMINS'][0], recipients=PE.split())

    with open('{}.json'.format(PCN + '_' + CN)) as file:
        msg.attach('{}.json'.format(PCN + '_' + CN), "text/plain", file.read())

    msg.body = 'Blank {}'.format(PCN + ' ' + CN)
    msg.html = PCN + ' ' + CN
    t = Thread(target=send_async_email, args=(app, msg))
    threads.append(t)
    t.start()
    for tj in threads:
        tj.join()


@app.route('/action', methods=['POST'])
def action():
    print('action')
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
    with open('{}.json'.format(PCN + '_' + CN), 'w') as file:
        json.dump(mess_arr, file, indent=2, ensure_ascii=False)

    subject = 'Blank {}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    msg = Message(subject, sender=app.config['ADMINS'][0], recipients=PE.split())

    with open('{}.json'.format(PCN + '_' + CN)) as file:
        msg.attach('{}.json'.format(PCN + '_' + CN), "text/plain", file.read())

    msg.body = 'Blank {}'.format(PCN + ' ' + CN)
    msg.html = PCN + ' ' + CN
    t = Thread(target=send_async_email, args=(app, msg))
    threads.append(t)
    print(t)
    t.start()
    for tj in threads:
        print(tj)
        tj.join()

    return t.join()
