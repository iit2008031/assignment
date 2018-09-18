import json
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from models import SKU, Order, Storage, OrderLine
from db_utils import get_details, post_details, put_details, get_all, delete_details
from utils import get_fulfillment_plan_util
from helper import http_response
from constants import HTTP_400_BAD_REQUEST, HTTP_200_OK

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data')


sku_key_set = set(['product_name'])
order_key_set = set(['customer_name'])
order_line_key_set = set(['quantity', 'sku_id'])
storage_key_set = set(['sku_id', 'stock'])


def validate_input(keys, key_set, operation):
    '''
        validates the input and returns True if valid else False
    '''
    common = keys.intersection(key_set)
    print(common, key_set, keys)
    if len(common) == len(keys) and operation == 'put':
        return True
    elif len(key_set) == len(common) and operation == 'post':
        return True
    return False


def prepare_request(keys, req_type):
    '''
        utility which process the input payload and validate function 
        returns validation flag and processed data
    '''
    args = parser.parse_args()
    if not args.get('data'):
        return 'Bad Request! Invalid Input', 400
    data = str(args['data'])
    data = data.replace('\'', '"')
    data = json.loads(data)
    flag = validate_input(set(data.keys()), keys, req_type)
    return flag, data


class SKUAPI(Resource):

    '''
        RUD API for SKU
    '''

    def get(self, sku_id):
        res = get_details(SKU, sku_id)
        if res:
            return res, 200
        return 'Resource Not Found', 404

    def delete(self, sku_id):
        res = delete_details(SKU, sku_id)
        if res:
            return 'Resource Deleted', 204
        return 'Resource Not Found', 404

    def put(self, sku_id):
        flag, data = prepare_request(sku_key_set, 'put')
        if flag:
            res = put_details(SKU, sku_id, data)
            if res:
                return 'Operation Succesful', 200
            return 'Operation Failed', 500
        return 'Bad Request! Invalid Input', 400


class SKUAll(Resource):

    '''
        Create and get all API for SKU
    '''

    def get(self):
        res = get_all(SKU)
        if res:
            return res, 200
        return "Not Found", 404

    def post(self):
        flag, data = prepare_request(sku_key_set, 'post')
        if flag:
            res = post_details(SKU, data)
            if res:
                return 'Operation Succesful', 200
            return 'Operation Failed', 500
        return 'Bad Request! Invalid Input', 400


class OrderApi(Resource):

    '''
        RUD API for Order
    '''

    def get(self, order_id):
        res = get_details(Order, order_id)
        if res:
            return res, 200
        return 'Resource Not Found', 404

    def delete(self, order_id):
        res = delete_details(Order, order_id)
        if res:
            return 'Resource Deleted', 204
        return 'Resource Not Found', 404

    def put(self, order_id):
        flag, data = prepare_request(order_key_set, 'put')
        if flag:
            res = put_details(Order, order_id, data)
            if res:
                return 'Operation Succesful', 200
            return 'Operation Failed', 500
        return 'Bad Request! Invalid Input', 400


class OrderAll(Resource):

    '''
        Create and get all API for Order
    '''

    def get(self):
        res = get_all(Order)
        if res:
            return res, 200

    def post(self):
        flag, data = prepare_request(order_key_set, 'post')
        if flag:
            res = post_details(Order, data)
            if res:
                return 'Operation Succesful', 200
            return 'Operation Failed', 500
        return 'Bad Request! Invalid Input', 400


class StorageApi(Resource):

    '''
        RUD API for Storage
    '''

    def get(self, storage_id):
        res = get_details(Storage, storage_id)
        if res:
            return res, 200
        return 'Resource Not Found', 404

    def delete(self, storage_id):
        res = delete_details(Storage, storage_id)
        if res:
            return 'Resource Deleted', 204
        return 'Resource Not Found', 404

    def put(self, storage_id):
        flag, data = prepare_request(storage_key_set, 'put')
        if flag:
            res = put_details(Storage, storage_id, data)
            if res:
                return 'Operation Succesful', 200
            return 'Operation Failed', 500
        return 'Bad Request! Invalid Input', 400


class StorageAll(Resource):

    '''
        Create and get all API for Storage
    '''

    def get(self):
        res = get_all(Storage)
        if res:
            return res, 200

    def post(self):
        flag, data = prepare_request(storage_key_set, 'post')
        if flag:
            res = post_details(Storage, data)
            if res:
                return 'Operation Succesful', 200
            return 'Operation Failed', 500
        return 'Bad Request! Invalid Input', 400


class OrderLineApi(Resource):

    '''
        RUD API for Order Line
    '''

    def get(self, order_id):
        res = get_details(Order, order_id)
        if res:
            return res, 200
        return 'Resource Not Found', 404

    def delete(self, order_id):
        res = delete_details(OrderLine, order_id)
        if res:
            return 'Resource Deleted', 204
        return 'Resource Not Found', 404

    def put(self, order_id):
        flag, data = prepare_request(order_line_key_set, 'put')
        if flag:
            res = put_details(OrderLine, order_id, data)
            if res:
                return 'Operation Succesful', 200
            return 'Operation Failed', 500
        return 'Bad Request! Invalid Input', 400


class OrderLineAll(Resource):

    '''
        Create and get all API for Order Line
    '''

    def get(self):
        res = get_all(OrderLine)
        if res:
            return res, 200

    def post(self):
        flag, data = prepare_request(order_line_key_set, 'post')
        if flag:
            res = post_details(OrderLine, data)
            if res:
                return 'Operation Succesful', 200
            return 'Operation Failed', 500
        return 'Bad Request! Invalid Input', 400


@app.route('/fulfillment', methods=['POST'])
def get_fulfillment_plan():
    '''
        handler for fulfillment endpoint
    '''
    try:
        payload = request.get_json()
        data = payload.get('lines')
    except ValueError as e:
        return http_response(HTTP_400_BAD_REQUEST, 'Bad Request! Invalid Input')
    if not data:
        return http_response(HTTP_400_BAD_REQUEST, 'Bad Request! Invalid Input')
    res = get_fulfillment_plan_util(data)
    return http_response(HTTP_200_OK, res)

api.add_resource(SKUAPI, '/sku/<sku_id>')
api.add_resource(OrderApi, '/order/<order_id>')
api.add_resource(OrderLineApi, '/order_line/<order_line_id>')
api.add_resource(StorageApi, '/storage/<storage_id>')

api.add_resource(SKUAll, '/skus')
api.add_resource(OrderAll, '/orders')
api.add_resource(OrderLineAll, '/order_lines')
api.add_resource(StorageAll, '/storages')


if __name__ == '__main__':
    app.run(debug=True)
