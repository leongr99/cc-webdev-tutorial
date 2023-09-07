from flask import Flask, render_template, jsonify

JOBS = [
    {
        'id' : 1,
    'title' : 'Data Analyst',
    'location': 'Hamburg',
    'salary' : '50.000€',
    },
        {
        'id' : 2,
    'title' : 'Frontend Engineer',
    'location': 'Kiel',
    'salary' : '55.000€',
    },
        {
        'id' : 3,
    'title' : 'Data Analyst Senior',
    'location': 'Remote',
    'salary' : '130.000€',
    },
            {
        'id' : 4,
    'title' : 'Backend Engineer',
    'location': 'Los Angeles',
    }
]


app = Flask(__name__)

@app.route("/")
def jovian_home():
    return render_template('home.html', jobs = JOBS, company_name = 'Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)