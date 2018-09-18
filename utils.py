from db_utils import get_storage_data


def get_fulfillment_plan_util(lines_data):
    '''
        utility function for fulfillment
        takes in lines as a input and returns storage with quantity as an output

        Steps:
        1) get all sku_ids from payload
        2) query storage for those skuids
        3) model data from storaga in ({sku_id: [(quantity, storage_id),()]}) format
        4) Iterate ove payload and look for sku_id in the model
        5) update quantity by reducing the amount from storage value and when quantity <= 0
        6) create result in the format mentioned

        Input:
        {
          "lines": [
            {
              "sku": "f9ec224d-d374-4368-bcc2-f165d017083b",
              "quantity": 12
            },
            {
              "sku": "ea215953-f842-4b6d-a128-d1b67e6dbb47",
              "quantity": 2
            }
          ]
        }

        Output:
        [
            {
                "id": "a0dfc5fc-3fac-49d0-ad82-e98b2d273c50",
                "quantity": 5
            },
            {
                "id": "a1c9e240-451f-4dbe-9ea8-e42202d77a3b",
                "quantity": 7
            },
            {
                "id": "a2444030-f96b-4585-9bc5-444214a921ca",
                "quantity": 2
            }
        ]
    '''
    res = []
    sku_ids = [line.get('sku') for line in lines_data]
    storage_data = get_storage_data(sku_ids)
    for line in lines_data:
        sku_id = line.get('sku')
        if sku_id:
            quanity = line.get('quantity')
            storage_sku_data = storage_data[sku_id]
            print(storage_sku_data)
            for d in storage_sku_data:
                print(d)
                res_dict = {}
                if d[0] >= quanity:
                    res_dict['id'] = d[1]
                    res_dict['quantity'] = quanity
                    res.append(res_dict)
                    break
                else:
                    quanity -= d[0]
                    res_dict['id'] = d[1]
                    res_dict['quantity'] = d[0]
                    res.append(res_dict)
    return res
