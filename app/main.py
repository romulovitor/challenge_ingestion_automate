from flask import Flask

from assessment.run import verify_data_status

app = Flask(__name__)

def db_connection():
    import sqlalchemy
    engine = sqlalchemy.create_engine("mysql://datatest:alligator@database/datatestdb")
    return engine

@app.route('/')
def hello_world():
    return "hello world"


@app.route('/status')
def city():
    result = verify_data_status()
    return str(result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
