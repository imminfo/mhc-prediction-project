#!/usr/bin/env python3


import os
from mhcpredict import mhcpredict, MHC_LIST


from flask import Flask, render_template, request
app = Flask('mhcpred')


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', mhc_list=MHC_LIST)

@app.route("/predict", methods=['POST'])
def predict():
    peptides = request.form['peptides'].splitlines()
    predictions = []
    for peptide, pred in zip(peptides, mhcpredict(request.form['mhc'], peptides)):
        predictions.append(dict(peptide=peptide, prediction=(pred>0.5)))
    return render_template('predict.html', predictions=predictions)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 48258))
    app.run(port=port)
