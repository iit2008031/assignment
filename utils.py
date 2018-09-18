from db_utils import get_storage_data


def get_fulfillment_plan_util(lines_data):
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
