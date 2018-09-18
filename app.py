from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from constants import *

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_STRING
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# logger = settings.BaseConfig.logger
# REDIS_JOB_PREFIX = 'UAID:JOB:'

# @app.route('/uaid/submit', methods=['POST'])
# @helper.authenticate
# def submit():
#     try:
#         payload = request.get_json()
#     except Exception as e:
#         msg = "Bad Request. Error while decoding json: {}".format(e)
#         return helper.http_response(constants.HTTP_400_BAD_REQUEST, msg)

#     logger.info("Submit Payload: {}".format(payload))
#     resp, job_id = app_helper.submit_job(payload, logger, REDIS_JOB_PREFIX)
#     if resp.status_code == constants.HTTP_202_ACCEPTED:
#         # Added countdown (2 minutes) so that addfix has time to run for that
#         # particular wbn
#         task_generate_uaid.apply_async(
#             (payload['data'], payload['callback_details'], job_id, REDIS_JOB_PREFIX),  # nopep8
#             queue=CELERY_GENERATE_QUEUE,
#             countdown=120)

#     return resp


@app.route('/sku', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def sku():
    if request.method == 'GET':
        sku_id = request.args.get('id')
        if not sku_id:
            msg = "Bad request. id missing"
            return helper.http_response(HTTP_400_BAD_REQUEST, msg)
        else:
            msg = get_sku_details(sku_id)
            if data:
                return helper.http_response(HTTP_200_OK, msg)
            msg = "Data not found with id {}".format(sku_id)
            return helper.http_response(HTTP_404_NOT_FOUND, msg)

    elif request.method == 'POST':
        try:
            payload = request.get_json()
        except Exception as e:
            msg = "Bad Request. Error while decoding json: {}".format(e)
            return helper.http_response(HTTP_400_BAD_REQUEST, msg)

        http_code, msg = post_sku_data(payload)
        return helper.http_response(http_code, msg)

    elif request.method == 'PATCH':
        try:
            payload = request.get_json()
        except Exception as e:
            msg = "Bad Request. Error while decoding json: {}".format(e)
            return helper.http_response(HTTP_400_BAD_REQUEST, msg)

        http_code, msg = post_sku_data(payload)
        return helper.http_response(http_code, msg)


@app.route('/order', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def order():


@app.route('/storage', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def storage():


@app.route('/order_line', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def order_line():


@app.route('/ping', methods=['GET'])
def ping():
    return "pong"


if __name__ == '__main__':
    app.run(debug=True)
