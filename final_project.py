from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the DivorceData model
class DivorceData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    all_3544 = db.Column(db.Float)
    HS_3544 = db.Column(db.Float)
    SC_3544 = db.Column(db.Float)
    BAp_3544 = db.Column(db.Float)
    BAo_3544 = db.Column(db.Float)
    GD_3544 = db.Column(db.Float)
    poor_3544 = db.Column(db.Float)
    mid_3544 = db.Column(db.Float)
    rich_3544 = db.Column(db.Float)
    all_4554 = db.Column(db.Float)
    HS_4554 = db.Column(db.Float)
    SC_4554 = db.Column(db.Float)
    BAp_4554 = db.Column(db.Float)
    BAo_4554 = db.Column(db.Float)
    GD_4554 = db.Column(db.Float)
    poor_4554 = db.Column(db.Float)
    mid_4554 = db.Column(db.Float)
    rich_4554 = db.Column(db.Float)
    poor_all = db.Column(db.Float)
    mid_all = db.Column(db.Float)
    rich_all = db.Column(db.Float)
    HS_all = db.Column(db.Float)
    SC_all = db.Column(db.Float)
    BAp_all = db.Column(db.Float)
    BAo_all = db.Column(db.Float)
    GD_all = db.Column(db.Float)

with app.app_context():
    db.create_all()

    divorce = pd.read_csv("C:\\Users\\bella\\OneDrive\\UMass School\\DACSS 690A\\final_project\\final_project\\divorce.csv")
    divorce.fillna(0, inplace=True)

    divorce['poor_all'] = divorce['poor_3544'] + divorce['poor_4554']
    divorce['mid_all'] = divorce['mid_3544'] + divorce['mid_4554']
    divorce['rich_all'] = divorce['rich_3544'] + divorce['rich_4554']
    divorce['HS_all'] = divorce['HS_3544'] + divorce['HS_4554']
    divorce['SC_all'] = divorce['SC_3544'] + divorce['SC_4554']
    divorce['BAp_all'] = divorce['BAp_3544'] + divorce['BAp_4554']
    divorce['BAo_all'] = divorce['BAo_3544'] + divorce['BAo_4554']
    divorce['GD_all'] = divorce['GD_3544'] + divorce['GD_4554']

    for _, row in divorce.iterrows():
        data_entry = DivorceData(
            year=row['year'],
            all_3544=row['all_3544'],
            HS_3544=row['HS_3544'],
            SC_3544=row['SC_3544'],
            BAp_3544=row['BAp_3544'],
            BAo_3544=row['BAo_3544'],
            GD_3544=row['GD_3544'],
            poor_3544=row['poor_3544'],
            mid_3544=row['mid_3544'],
            rich_3544=row['rich_3544'],
            all_4554=row['all_4554'],
            HS_4554=row['HS_4554'],
            SC_4554=row['SC_4554'],
            BAp_4554=row['BAp_4554'],
            BAo_4554=row['BAo_4554'],
            GD_4554=row['GD_4554'],
            poor_4554=row['poor_4554'],
            mid_4554=row['mid_4554'],
            rich_4554=row['rich_4554'],
            poor_all=row['poor_all'],
            mid_all=row['mid_all'],
            rich_all=row['rich_all'],
            HS_all=row['HS_all'],
            SC_all=row['SC_all'],
            BAp_all=row['BAp_all'],
            BAo_all=row['BAo_all'],
            GD_all=row['GD_all']
        )
        db.session.add(data_entry)
    db.session.commit()

#Route to generate and show the plot
@app.route('/')
def index():
    records = DivorceData.query.all()
    data = [{
        'year': r.year,
        'poor_all': r.poor_all,
        'mid_all': r.mid_all,
        'rich_all': r.rich_all
    } for r in records]

    df = pd.DataFrame(data)
    df = df[df['year'].between(1960, 2012)]

    plt.figure(figsize=(10, 6))
    plt.plot(df['year'], df['poor_all'], label='Poor')
    plt.plot(df['year'], df['mid_all'], label='Middle')
    plt.plot(df['year'], df['rich_all'], label='Rich')
    plt.xlabel('Year')
    plt.ylabel('Divorce Rate')
    plt.title('Divorce Rates (Age 35–54) by Income Level, 1960–2012')
    plt.legend()
    plt.grid(True)

    plot_path = os.path.join('static', 'plot.png')
    plt.savefig(plot_path)
    plt.close()

    return render_template('index.html', plot_url=plot_path)

if __name__ == '__main__':
    app.run(debug=True)

