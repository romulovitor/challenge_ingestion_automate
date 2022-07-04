from flask import Flask

from assessment.run import *

app = Flask(__name__)

def db_connection():
    import sqlalchemy
    engine = sqlalchemy.create_engine("mysql://datatest:alligator@database/datatestdb")
    return engine

@app.route('/')
def hello_world():
    return "hello world"


@app.route('/status')
def status():
    result = verify_data_status()
    return str(result)

@app.route('/group_by_three_way')
def status():
    result = group_by_three_way()
    return str(result)

@app.route('/group_by_week')
def status():
    result = group_by_week()
    return str(result)

@app.route('sql_cheap_mobile')
def group_by_three_way():
    """
    SELECT region
    FROM coordinate
    WHERE datasource = 'cheap_mobile'
    """


@app.route('sql_rank_by_region')
def group_by_three_way():
    """
        SELECT * FROM (
        SELECT region,
    RANK() OVER (
        PARTITION BY regions
        ORDER BY datetime DESC
    ) RANK_BY_REGION
    FROM  coordinate)
    ORDER BY RANK_BY_REGION
    LIMIT 2"""
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
