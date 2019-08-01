from app import app
from flask import render_template, flash, request, redirect, url_for


@app.route('/en')
def en_index():
    return render_template('en_index.html')


@app.route('/')
@app.route('/ru')
def ru_index():
    return render_template('ru_index.html')


@app.route('/action', methods=['POST'])
def action():
    ITN = request.form.get('IndividualTaxNumber', None)
    flash('Принял')
    print(ITN)
    return redirect(url_for('ru_index'))
