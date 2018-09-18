# class SKUAPI(Resource):

#     def get(self, sku_id):
#         res = get_details(SKU, sku_id)
#         if res:
#             return res, 200
#         return 'Resource Not Found', 404

#     def delete(self, sku_id):
#         res = delete_details(SKU, sku_id)
#         if res:
#             return 'Resource Deleted', 204
#         return 'Resource Not Found', 404

#     def put(self, sku_id):
#         parser.add_argument('data')
#         args = parser.parse_args()
#         flag = validate_input(args)
#         if flag:
#             res = put_details(SKU, sku_id, args)
#             if res:
#                 return res, 200
#             return 'Resource Not Found', 404
#         return 'Bad Request', 400


# class SKUAll(Resource):

#     def get(self):
#         get_all(SKU)

#     def post(self):
#         parser.add_argument('data')
#         args = parser.parse_args()
#         flag = validate_input(args)
#         if flag:
#             res = post_details(SKU, sku_id, args)
#             if res:
#                 return 'Resource Created', 201
#             return 'Resource Not Found', 404
#         return 'Bad Request', 400


# class OrderApi(Resource):

#     def get(self, order_id):
#         res = get_details(Order, order_id)
#         if res:
#             return res, 200
#         return 'Resource Not Found', 404

#     def delete(self, order_id):
#         res = delete_details(Order, order_id)
#         if res:
#             return 'Resource Deleted', 204
#         return 'Resource Not Found', 404

#     def put(self, order_id):
#         parser.add_argument('data')
#         args = parser.parse_args()
#         flag = validate_input(args)
#         if flag:
#             res = put_details(Order, order_id, args)
#             if res:
#                 return res, 200
#             return 'Resource Not Found', 404
#         return 'Bad Request', 400


# class OrderAll(Resource):

#     def get(self):
#         res = get_all(Order)
#         if res:
#             return res, 200

#     def post(self):
#         parser.add_argument('data')
#         args = parser.parse_args()
#         flag = validate_input(args)
#         if flag:
#             res = post_details(Order, args)
#             if res:
#                 return 'Resource Created', 201
#             return 'Resource Not Found', 404
#         return 'Bad Request', 400


# class StorageApi(Resource):

#     def get(self, storage_id):
#         res = get_details(Storage, storage_id)
#         if res:
#             return res, 200
#         return 'Resource Not Found', 404

#     def delete(self, storage_id):
#         res = delete_details(Storage, order_id)
#         if res:
#             return 'Resource Deleted', 204
#         return 'Resource Not Found', 404

#     def put(self, storage_id):
#         parser.add_argument('data')
#         args = parser.parse_args()
#         flag = validate_input(args)
#         if flag:
#             res = put_details(Storage, storage_id, args)
#             if res:
#                 return res, 200
#             return 'Resource Not Found', 404
#         return 'Bad Request', 400


# class StorageAll(Resource):

#     def get(self):
#         res = get_all(Order)
#         if res:
#             return res, 200

#     def post(self):
#         parser.add_argument('data')
#         args = parser.parse_args()
#         flag = validate_input(args)
#         if flag:
#             res = post_details(Order, args)
#             if res:
#                 return 'Resource Created', 201
#             return 'Resource Not Found', 404
#         return 'Bad Request', 400


# class OrderLineApi(Resource):

#     def get(self, order_id):
#         res = get_details(Order, order_id)
#         if res:
#             return res, 200
#         return 'Resource Not Found', 404

#     def delete(self, order_id):
#         res = delete_details(Order, order_id)
#         if res:
#             return 'Resource Deleted', 204
#         return 'Resource Not Found', 404

#     def put(self, order_id):
#         parser.add_argument('data')
#         args = parser.parse_args()
#         flag = validate_input(args)
#         if flag:
#             res = post_details(Order, order_id, args)
#             if res:
#                 return res, 200
#             return 'Resource Not Found', 404
#         return 'Bad Request', 400


# class OrderLineAll(Resource):

#     def get(self):
#         res = get_all(Order)
#         if res:
#             return res, 200

#     def post(self):
#         parser.add_argument('data')
#         args = parser.parse_args()
#         flag = validate_input(args)
#         if flag:
#             res = post_details(Order, args)
#             if res:
#                 return 'Resource Created', 201
#             return 'Resource Not Found', 404
#         return 'Bad Request', 400
