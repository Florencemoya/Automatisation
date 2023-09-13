import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from data_new import data_new

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def show_form():
    return render_template('form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    print(type(request.form['dt_quadsupg']))
    dt_quadsupg = float(request.form['dt_quadsupg'])
    dt_quadinfg = float(request.form['dt_quadinfg'])
    dt_quadsupd = float(request.form['dt_quadsupd'])
    dt_quadinfd = float(request.form['dt_quadinfd'])
    dt_dis_quadsupg = float(request.form['dt_dis_quadsupg'])
    dt_dis_quadinfg = float(request.form['dt_dis_quadinfg'])
    dt_dis_quadsupd = float(request.form['dt_dis_quadsupd'])
    dt_dis_quadinfd = float(request.form['dt_dis_quadinfd'])
    st = float(request.form['st'])
    dt_centrale = float(request.form['dt_centrale'])
    dt_dis_centrale = float(request.form['dt_dis_centrale'])

    data = pd.DataFrame({
            'DT_quadsupg': [dt_quadsupg],
            'DT_quadinfg': [dt_quadinfg],
            'DT_quadsupd': [dt_quadsupd],
            'DT_quadinfd': [dt_quadinfd],
            'DT_dis_quadsupg': [dt_dis_quadsupg],
            'DT_dis_quadinfg': [dt_dis_quadinfg],
            'DT_dis_quadsupd': [dt_dis_quadsupd],
            'DT_dis_quadinfd': [dt_dis_quadinfd],
            'ST': [st],
            'DT_centrale': [dt_centrale],
            'DT_dis_centrale': [dt_dis_centrale]
        })

    result = data_new(data)

    dt_gauche = result['DT_gauche'].values[0]
    dt_droite = result['DT_droite'].values[0]
    dt_dis_gauche = result['DT_dis_gauche'].values[0]
    dt_dis_droite = result['DT_dis_droite'].values[0]
    dt_laterales = result['DT_laterales'].values[0]
    dt_dis_laterales = result['DT_dis_laterales'].values[0]
    resultat_dt_laterales = result['Resultat_DT_laterales'].values[0]
    resultat_dt_dis_laterales = result['Resultat_DT_dis_laterales'].values[0]
    resultat_st = result['Resultat_ST'].values[0]
    resultat_dt_centrale = result['Resultat_DT_centrale'].values[0]
    resultat_dt_dis_centrale = result['Resultat_DT_dis_centrale'].values[0]
    combinaison = result['Combinaison'].values[0]
    valeur_attribuee = result['Valeur_attribuée'].values[0]
       
        # Rendre le résultat dans le template HTML
    return render_template('result.html', dt_gauche=dt_gauche, dt_droite=dt_droite, dt_dis_gauche=dt_dis_gauche,
                               dt_dis_droite=dt_dis_droite, dt_laterales=dt_laterales, dt_dis_laterales=dt_dis_laterales,
                               resultat_dt_laterales=resultat_dt_laterales,
                               resultat_dt_dis_laterales=resultat_dt_dis_laterales, resultat_st=resultat_st,
                               resultat_dt_centrale=resultat_dt_centrale,
                               resultat_dt_dis_centrale=resultat_dt_dis_centrale, combinaison=combinaison,
                               valeur_attribuee=valeur_attribuee)

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)